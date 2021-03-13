from AbstractRequest import AbstractRequest

class SearchRequest(AbstractRequest):

    name = ""
    sequence = ""
    sequence_option = ""
    sequence_length = ""
    n_terminus_id = ""
    c_terminus_id = ""
    target_group_id = ""
    target_object_id = ""
    synthesis_type = ""
    kingdom_id = ""
    bond_id = ""
    unusual_amino_acid_id = ""
    author_id = ""
    journal_id = ""
    article_year = ""
    article_title = ""
    complexity = "monomer"
    target_species_id = ""
    non_standart_experimental_conditions = "false"
    hemolytic_and_cytotoxic_activities = "false"

    def query_type(self):
        return "search"

    def get_parameters(self):
        dict = {}
        dict["complexity"] = self.complexity
        dict["name"] = self.name
        dict["sequence"] = self.sequence
        dict["sequence_option"] = self.sequence_option
        dict["sequence_length"] = self.sequence_length
        dict["n_terminus_id"] = self.n_terminus_id
        dict["c_terminus_id"] = self.c_terminus_id
        dict["target_group_id"] = self.target_group_id
        dict["target_object_id"] = self.target_object_id
        dict["synthesis_type"] = self.synthesis_type
        dict["kingdom_id"] = self.kingdom_id
        dict["bond_id"] = self.bond_id
        dict["unusual_amino_acid_id"] = self.unusual_amino_acid_id
        dict["author_id"] = self.author_id
        dict["journal_id"] = self.journal_id
        dict["article_year"] = self.article_year
        dict["article_title"] = self.article_title
        dict["target_species_id"] = self.target_species_id
        dict["non_standart_experimental_conditions"] = self.non_standart_experimental_conditions
        dict["hemolytic_and_cytotoxic_activities"] = self.hemolytic_and_cytotoxic_activities
        return dict