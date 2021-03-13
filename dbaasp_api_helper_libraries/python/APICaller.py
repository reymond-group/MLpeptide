import sys
sys.path.append('./request')  

from LookupRequest import LookupRequest
from PeptideCardRequest import PeptideCardRequest
from SearchRequest import SearchRequest
from RankingSearchRequest import RankingSearchRequest

from LookupType import LookupType
from FormatType import FormatType
from Complexity import Complexity
from MathOperationTypes import MathOperationTypes

# lookupRequest = LookupRequest()
# lookupRequest.lookupType = LookupType.MEDIUM;
# print (lookupRequest.request())


# peptideCardRequest = PeptideCardRequest()
# peptideCardRequest.peptide_id = 8;
# peptideCardRequest.format = FormatType.JSON;
# print (peptideCardRequest.request())


# searchRequest = SearchRequest()
# searchRequest.name = "a"
# searchRequest.format = FormatType.JSON;
# print (searchRequest.request())


# rankingSearchRequest = RankingSearchRequest()
# rankingSearchRequest.target_species_id = 3232
# rankingSearchRequest.activity_measure_id = 72
# rankingSearchRequest.activity = 100;
# rankingSearchRequest.operation = MathOperationTypes.GREATER;
# rankingSearchRequest.format = FormatType.JSON;
# print (rankingSearchRequest.request())
