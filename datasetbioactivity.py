import torch
from vocabulary import Vocabulary

class Dataset(torch.utils.data.Dataset):
    """Custom PyTorch Dataset that takes a file containing \n separated SMILES"""

    def __init__(self, dataset, vocabulary : Vocabulary, with_activity=True):
        self.vocabulary = vocabulary
        self.dataset = dataset
        self.category = with_activity
    
    def __getitem__(self, i):
        seq_str = self.dataset.iloc[i]["Sequence"]
        tensor = self.vocabulary.seq_to_tensor(seq_str)
        if self.category:
            category_tensor = torch.tensor(self.dataset.iloc[i]["activity"], dtype=torch.long)
            return tensor, category_tensor
        else:
            return tensor

    def __len__(self):
        return len(self.dataset)

    
def collate_fn(arr):
    """Function to take a list of encoded sequences and turn them into a batch"""
    arr_seq = [element[0] for element in arr]
    cat_seq = [element[1] for element in arr]
    packed_seq = torch.nn.utils.rnn.pack_sequence(arr_seq, enforce_sorted=False)
    padded_seq = torch.nn.utils.rnn.pad_packed_sequence(packed_seq,batch_first=True)
    return padded_seq, torch.tensor(cat_seq)

            
def collate_fn_no_activity(arr):
    """Function to take a list of encoded sequences and turn them into a batch"""
    packed_seq = torch.nn.utils.rnn.pack_sequence(arr, enforce_sorted=False)
    padded_seq = torch.nn.utils.rnn.pad_packed_sequence(packed_seq,batch_first=True)

    return padded_seq