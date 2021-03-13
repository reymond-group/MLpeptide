from AbstractRequest import AbstractRequest

class RankingSearchRequest(AbstractRequest):

    sequence_length = ""
    n_terminus_id = ""
    c_terminus_id = ""
    bond_id = ""
    unusual_amino_acid_id = ""
    synthesis_type = ""
    kingdom_id = ""
    target_species_id = ""
    activity_measure_id = ""
    operation = ""
    activity = ""
    complexity = ""
    medium_id = ""
    cfu = ""
    complexity = "monomer"

    def query_type(self):
        return "ranking_search"

    def get_parameters(self):
        dict = {}

        dict["sequence_length"] = self.sequence_length
        dict["n_terminus_id"] = self.n_terminus_id
        dict["c_terminus_id"] = self.c_terminus_id
        dict["bond_id"] = self.bond_id
        dict["unusual_amino_acid_id"] = self.unusual_amino_acid_id
        dict["synthesis_type"] = self.synthesis_type
        dict["kingdom_id"] = self.kingdom_id
        dict["target_species_id"] = self.target_species_id
        dict["activity_measure_id"] = self.activity_measure_id
        dict["operation"] = self.operation
        dict["activity"] = self.activity
        dict["complexity"] = self.complexity
        dict["medium_id"] = self.medium_id
        dict["cfu"] = self.cfu

        return dict