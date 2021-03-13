import torch
from torch import nn
from torch.nn import functional as F

class ClassifierRNN(nn.Module):
    def __init__(self, input_size, embedding_size, hidden_size, num_layers, output_size, dropout=0.0):
        super(ClassifierRNN, self).__init__()

        self.embedding = torch.nn.Embedding(input_size, embedding_size)
        self.rnn = torch.nn.GRU(embedding_size, hidden_size, num_layers, batch_first=True, bidirectional=False, dropout=dropout)
        self.output_layer = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)
        
        self.debug_print = False
        
        
    def forward(self, sequences, lengths):
        output = self.embedding(sequences)
        
        #we pack the output together to minimize the compute with th rnn
        output = torch.nn.utils.rnn.pack_padded_sequence(output, lengths, batch_first=True, enforce_sorted=False)
        
        all_outputs, hidden = self.rnn(output)
        
        # we can now grab the last hidden state or the last output and give it to the output layer. for RNN and GRU the last output and the last hidden are the same,
        # for LSTM the last output and the last hidden are different
        
        # the hidden tensor has the shape (num_layers * directions, batch_size, hidden_size)
        # to grab the hidden state from the last layer we can just do this (needs to be adjusted if we have bidirectional layers, because we want the output of both directions [last 2 layer])
        hidden = hidden[-1]
        
        if self.debug_print:
            # to grab the last output we pad the output again
            all_outputs, _ = torch.nn.utils.rnn.pad_packed_sequence(all_outputs, batch_first=True)

            # and the shape is now (batch_size, max_sequence_length, hidden_size)
            # we can grab the last output before each sequence stops

            last_output = torch.stack([all_outputs[seq,seq_length-1,:] for seq,seq_length in enumerate(lengths)])

            # and now we can check if hidden and output are the same (for RNN and GRU)

            print("is the last hidden state the same as the output?", torch.all(hidden.data == last_output.data))

        output = self.output_layer(hidden)

        # softmax does the squishing so the numbers are between 0 and 1 and their sum is always = 1
        output = self.softmax(output)

        return output, hidden
    
class Classifier:
    def __init__(self, embedding_size, hidden_size, num_layers, vocabulary, dropout=0.0):
        self.embedding_size = embedding_size
        self.num_layers = num_layers
        self.hidden_size = hidden_size
        self.dropout = dropout
        self.vocabulary = vocabulary
        
        self.model = ClassifierRNN(len(self.vocabulary), embedding_size, hidden_size, num_layers, 2, dropout)

    def training_mode(self):
        self.model.train()
    def prediction_mode(self):
        self.model.eval()
    
    @classmethod
    def load_from_file(cls, file_path: str):
        """
        Loads a model from a single file
        :param file: filpath as string
        :return: new instance of the RNN or None if it was not possible to load
        """
        
        if torch.cuda.is_available():
            device = torch.device("cuda")
            map_location = "cuda:0"
        else:
            device = torch.device("cpu")
            map_location = "cpu"         

        save_dict = torch.load(file_path, map_location=map_location)
        
        vocabulary = save_dict["vocabulary"]
        hidden_size = save_dict["hiddend_size"]
        embedding_size = save_dict["embedding_size"]
        num_layers = save_dict["num_layers"]
        if "dropout" in save_dict.keys():
            dropout = save_dict["dropout"]
        else:
            dropout = 0.0
        #(self, input_size, embedding_size, hidden_size, num_layers, output_size)
        model = ClassifierRNN(len(vocabulary), embedding_size, hidden_size, num_layers, 2, dropout)
        model.load_state_dict(save_dict["model"])
        #model.to(device)
        
        loaded_model = Classifier(embedding_size, hidden_size, num_layers, vocabulary, dropout)
        loaded_model.model = model
        
        return loaded_model
        
    def save(self, file):
        """
        Saves the model into a file
        :param file: Filepath as string
        :return: None
        """
        save_dict = {
            'dropout':self.dropout,
            'vocabulary': self.vocabulary,
            'hiddend_size': self.hidden_size,
            'embedding_size' : self.embedding_size,
            'num_layers' : self.num_layers,
            'model' : self.model.state_dict()
        }
        torch.save(save_dict, file)
    
    @torch.no_grad()
    def predict_proba(self, sequences, lengths):
        output, _ = self.model(sequences.to(self.device, non_blocking=True), lengths.to(self.device, non_blocking=True))
        return torch.exp(output).cpu().numpy()
    
    def evaluate(self, sequences, lengths):
        output, _ = self.model(sequences.to(self.device, non_blocking=True), lengths.to(self.device, non_blocking=True))
        return output
    
    def to(self, device):
        return self.model.to(device, non_blocking=True)
    
    def predict_peptide_sequence(self, seq):
        
        if isinstance(seq, str):
            tensor = [self.vocabulary.seq_to_tensor(seq)]
        else: 
            tensor = [self.vocabulary.seq_to_tensor(s) for s in seq]
        
        packed_seq = torch.nn.utils.rnn.pack_sequence(tensor, enforce_sorted=False)
        padded_seq = torch.nn.utils.rnn.pad_packed_sequence(packed_seq,batch_first=True)
        sequences = padded_seq[0]
        length = padded_seq[1]

        prob = self.predict_proba(sequences,length)
        return prob
    
    @property
    def device(self):
        return next(self.model.parameters()).device
    
class GeneratorRNN(nn.Module):
    def __init__(self, input_size, embedding_size, hidden_size, num_layers):
        super(GeneratorRNN, self).__init__()
        self.embedding = torch.nn.Embedding(input_size, embedding_size)
        self.rnn = torch.nn.GRU(embedding_size, hidden_size, num_layers, batch_first=True, bidirectional=False)
        self.output_layer = nn.Linear(hidden_size, input_size)
        self.softmax = nn.LogSoftmax(dim=-1)
        
        self.debug_print = False
        
        
    def forward(self, sequences, lengths, hidden=None):
        output = self.embedding(sequences)

        #we pack the output together to minimize the compute with th rnn
        output = torch.nn.utils.rnn.pack_padded_sequence(output, lengths, batch_first=True, enforce_sorted=False)
        
        all_outputs, hidden = self.rnn(output, hidden)
        
        # we can now grab the last hidden state or the last output and give it to the output layer. for RNN and GRU the last output and the last hidden are the same,
        # for LSTM the last output and the last hidden are different
        
        # the hidden tensor has the shape (num_layers * directions, batch_size, hidden_size)

        # to grab the last output we pad the output again
        all_outputs, _ = torch.nn.utils.rnn.pad_packed_sequence(all_outputs, batch_first=True)

        # and the shape is now (batch_size, max_sequence_length, hidden_size)

        output = self.output_layer(all_outputs)

        # softmax does the squishing so the numbers are between 0 and 1 and their sum is always = 1
        output = self.softmax(output)

        return output, hidden

class Generator:
    def __init__(self, embedding_size, hidden_size, num_layers, vocabulary):
        self.embedding_size = embedding_size
        self.num_layers = num_layers
        self.hidden_size = hidden_size

        self.vocabulary = vocabulary
        
        self.model = GeneratorRNN(len(self.vocabulary), embedding_size, hidden_size, num_layers)
    
    @classmethod
    def load_from_file(cls, file_path: str):
        """
        Loads a model from a single file
        :param file: filpath as string
        :return: new instance of the RNN or None if it was not possible to load
        """
        
        if torch.cuda.is_available():
            device = torch.device("cuda")
            map_location = "cuda:0"
        else:
            device = torch.device("cpu")
            map_location = "cpu"         

        save_dict = torch.load(file_path, map_location=map_location)
        
        vocabulary = save_dict["vocabulary"]
        hidden_size = save_dict["hiddend_size"]
        embedding_size = save_dict["embedding_size"]
        num_layers = save_dict["num_layers"]
        #(self, input_size, embedding_size, hidden_size, num_layers, output_size)
        model = GeneratorRNN(len(vocabulary), embedding_size, hidden_size, num_layers)
        model.load_state_dict(save_dict["model"])
        #model.to(device)
        
        loaded_model = Generator(embedding_size, hidden_size, num_layers, vocabulary)
        loaded_model.model = model
        
        return loaded_model
        
    def save(self, file):
        """
        Saves the model into a file
        :param file: Filepath as string
        :return: None
        """
        save_dict = {
            'vocabulary': self.vocabulary,
            'hiddend_size': self.hidden_size,
            'embedding_size' : self.embedding_size,
            'num_layers' : self.num_layers,
            'model' : self.model.state_dict()
        }
        torch.save(save_dict, file)
    
    @torch.no_grad()
    def predict_proba(self, sequences, lengths):
        output, _ = self.rnn(sequences, lengths)
        return torch.exp(output).cpu().numpy()
    
    def likelihood(self, sequences, lengths):
        # return the NLL for a sequence, while training we want to minize this
        # sequences is a tensor of shape (batch_size, max_legths), it includes sequences with paddings
        # lengths is the length of each sequence in shape (batch_size)
        output, _ = self.model(sequences, lengths)
        tensor_expected = torch.zeros_like(sequences)
        tensor_expected[:, :-1] = sequences[:, 1:]
        negativeloglikelihoods = torch.zeros(sequences.size()[0], device=sequences.device)
        
        for j, lenght in enumerate(lengths):
            negativeloglikelihoods[j] = F.nll_loss(output[j, : lenght-1], tensor_expected[j, : lenght-1], reduction="sum", ignore_index=0)
        
        return negativeloglikelihoods
    
    
    @torch.no_grad()
    def sample(self, batch_size, max_length=200):
        """
        Sample a batch of sequences
        :param batch_size: Number of sequences to sample
        :param max_length: Maximum length of the sequences
        return:
            seqs: (batch_size, seq_length) The sampled sequences.
            log_probs : (batch_size) Negative Log likelihood for each sequence.
        """
        start_token = torch.zeros(batch_size, device = self.device, dtype=torch.long)
        start_token[:] = self.vocabulary.vocabulary["<start>"]
        start_token = start_token.unsqueeze(dim=1)
        
        end_token = torch.zeros_like(start_token)
        end_token[:] = self.vocabulary.vocabulary["<end>"]
        
        hidden = None  # creates zero tensor by default
        
        lengths = torch.ones(batch_size, dtype=torch.long, device = self.device) # we do 1 character at a time
        
        sequences = []
        sequences.append(start_token)

        log_probs = torch.zeros(batch_size, device = self.device)
        
        unfinished = torch.ones_like(start_token)
        
        for step in range(max_length):

            log_prob, hidden = self.model(sequences[-1], lengths, hidden)
                
            prob = torch.exp(log_prob)            
            sampled_characters = torch.multinomial(prob.view(-1, log_prob.size()[-1]), 1)
            
            sampled_characters = sampled_characters * unfinished
            sequences.append(sampled_characters)
            
            unfinished[(sampled_characters == end_token)] = 0
            
            if unfinished.sum() == 0:
                break
            
        sequences = torch.cat(sequences, 1)
        return sequences
    
    
    def to(self, device):
        return self.model.to(device, non_blocking=True)
    
    @property
    def device(self):
        return next(self.model.parameters()).device