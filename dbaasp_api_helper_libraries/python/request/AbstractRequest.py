import urllib


class AbstractRequest :

    base_url = "https://dbaasp.org/api/v1"
    format = "json";

    def query_type(self):
        return "none";

    def get_parameters(self):
        return "none";

    def request(self):
        request_parameters = {};
        request_parameters["query"] = self.query_type()
        request_parameters["format"] = self.format

        # adding custom parameters for specific request
        parameters = self.get_parameters();
        for name in parameters:
            request_parameters[name]= parameters[name]

        url_values = urllib.parse.urlencode(request_parameters)
        url = "https://dbaasp.org/api/v1";

        contents = urllib.request.urlopen(url + "?" + url_values).read();
        return contents;