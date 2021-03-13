class LookupRequest  < AbstractRequest

    attr_accessor :lookupType

    def initialize()
       super();
       @lookupType = "n_terminus"
    end
    
	def query_type
        return "lookup"
    end

    def get_parameters
       dictionary = { "lookup_type" => self.lookupType}
       return dictionary
    end
    
end