from AbstractRequest import AbstractRequest


class LookupRequest(AbstractRequest):

    lookupType = "n_terminus"

    def query_type(self):
        return "lookup"

    def get_parameters(self):
        dict = {}
        dict["lookup_type"] = self.lookupType;
        return dict


