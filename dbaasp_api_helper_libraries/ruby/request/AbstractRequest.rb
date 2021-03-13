require 'net/https'

class AbstractRequest

	attr_accessor :format
	
	def initialize()
       @format = "json"
    end

    def query_type
        return "none"
    end

    def get_parameters
        return "none"
    end

    
    def request

        request_parameters = { "query" => self.query_type, "format" => self.format }
		
        # adding custom parameters for specific request
        parameters = self.get_parameters();
        
        parameters.each do |key, value|
          request_parameters.store(key, value);
        end
        
        p request_parameters;
    
        uri = URI("https://dbaasp.org/api/v1"+ "?" + URI.encode_www_form(request_parameters))
        response = Net::HTTP.start(
        						uri.host, 
        						uri.port, 
        						:use_ssl => uri.scheme == 'https',
                				:verify_mode => OpenSSL::SSL::VERIFY_NONE) do |http|
           request = Net::HTTP::Get.new uri.request_uri
           http.request request # Net::HTTPResponse object
        end
        return response.body
    end
end
