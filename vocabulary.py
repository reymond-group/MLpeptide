import torch
from sklearn.feature_extraction.text import CountVectorizer

class Vocabulary():
    def __init__(self, vocabulary):
        if "<pad>" not in vocabulary:
            vocabulary = { character: value+1 for character, value in vocabulary.items() }
            vocabulary['<pad>'] = 0    
        if "<start>" not in vocabulary:
            vocabulary["<start>"] = len(vocabulary)
        if "<end>" not in vocabulary:
            vocabulary["<end>"] = len(vocabulary)
        self.inv_vocabulary = {v: k for k, v in vocabulary.items()}
        self.vocabulary = vocabulary
    
    def letter_to_index(self, letter):
        return self.vocabulary[letter]

    def index_to_letter(self, index):
        return self.inv_vocabulary[index]
    
    def tensor_to_seq(self, tensor, debug=False):
        seq = ''
        for element in tensor:
            new_char = self.inv_vocabulary[element.item()]
            if not debug:
                if new_char == "<pad>" or new_char == "<start>" or new_char == "<end>":
                    new_char = ''
            seq = seq + new_char
        return seq
    
    def __len__(self):
        return len(self.vocabulary)
    
    def seq_to_tensor(self, seq):
        tensor = torch.zeros(len(seq)+2, dtype=torch.long)
        tensor[0] = torch.tensor(self.vocabulary["<start>"])
        for i, letter in enumerate(seq):
            tensor[i+1] = torch.tensor(self.vocabulary[letter])
        tensor[-1] = torch.tensor(self.vocabulary["<end>"])
        return tensor
    
    @classmethod
    def get_vocabulary_from_sequences(cls, seq):
        # returns vocabolary class initialized with the vocabulary of the give X_seq
        count_vect = CountVectorizer(lowercase = False, analyzer = "char")
        count_vect.fit(seq)
        char_voc = count_vect.vocabulary_
        char_voc_ = {}
        for k,v in char_voc.items():
            char_voc_[k] = v + 1
        char_voc_['<pad>'] = 0
        return Vocabulary(char_voc_)