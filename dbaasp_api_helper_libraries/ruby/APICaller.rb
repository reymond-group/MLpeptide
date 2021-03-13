 require "./request/AbstractRequest.rb"
 require './request/LookupRequest.rb' 
 require './request/PeptideCardRequest.rb' 
 require './request/SearchRequest.rb' 
 require './request/RankingSearchRequest.rb' 
 require './LookupType.rb' 
 require './FormatType.rb' 
 require './MathOperationTypes.rb' 
 require './Complexity.rb' 
 
#  lookupRequest = LookupRequest.new
#  lookupRequest.lookupType = LookupType::KINGDOM;
#  lookupRequest.format = FormatType::XML;
#  p lookupRequest.request()


#  peptideCardRequest = PeptideCardRequest.new
#  peptideCardRequest.peptide_id = 1
#  peptideCardRequest.format = FormatType::XML;
#  p (peptideCardRequest.request())


#  searchRequest = SearchRequest.new
#  searchRequest.name = "a"
#  searchRequest.format = FormatType::JSON;
#  p (searchRequest.request())


#  rankingSearchRequest = RankingSearchRequest.new
#  rankingSearchRequest.target_species_id = 3232
#  rankingSearchRequest.activity_measure_id = 72
#  rankingSearchRequest.activity = 100;
#  rankingSearchRequest.operation = MathOperationTypes::GREATER;
#  rankingSearchRequest.format = FormatType::FASTA;
#  p (rankingSearchRequest.request())
