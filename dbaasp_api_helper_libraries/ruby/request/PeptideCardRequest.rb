class PeptideCardRequest  < AbstractRequest

    attr_accessor :peptide_id

    def initialize()
       super();
       @peptide_id = 1
    end
    
	def query_type
        return "peptide_card";
    end

    def get_parameters
       dictionary = { "peptide_id" => self.peptide_id}
       return dictionary
    end

end


