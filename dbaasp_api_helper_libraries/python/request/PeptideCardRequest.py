from AbstractRequest import AbstractRequest

class PeptideCardRequest(AbstractRequest):

    peptide_id = 1;

    def query_type(self):
        return "peptide_card"

    def get_parameters(self):
        dict = {}
        dict["peptide_id"] = self.peptide_id;
        return dict
