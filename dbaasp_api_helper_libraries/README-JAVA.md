
# DBAASP API Java Library



## Examples

####  1.lookup 

| Parameter | Description |
| --- | --- |
| lookup_type | available types: target_object, target_group, n_terminus, c_terminus, synthesis_type, complexity, kingdom, intra_chain_bond, unusual_amino_acid, unit, activity_measure, author, journal, target_species, mammalian_cell, medium |
| format | xml,json,tab |

```
LookupRequest lookupRequest = new LookupRequest(); 
lookupRequest.setLookupType(LookupType.C_TERMINUS); 
lookupRequest.setFormatType(FormatType.XML);
String response = lookupRequest.request() ;
```

#### 2.peptide_card 

| Parameter | Description |
| --- | --- |
| peptide_id | peptide card id |
| format | xml,json,fasta |


```
PeptideCardRequest peptideCardRequest = new PeptideCardRequest();
peptideCardRequest.setPeptideId(8);
peptideCardRequest.setFormatType(FormatType.XML);
String response = peptideCardRequest.request() ;
```


#### 3.search 

| Parameter | Description |
| --- | --- |
| complexity | Type of Peptide. Available values : monomer (default), dimer, multi_peptide |
| name | Name of peptide |
| sequence | Sequence of peptide |
| sequence_option | Available types : part, full |
| sequence_length | Length of sequence |
| target_group_id | Identifier of target group |
| target_object_id | Identifier of target object |
| n_terminus_id | Identifier of N Terminus |
| c_terminus_id | Identifier of C Terminus |
| synthesis_type | Identifier of Synthesys Type |
| kingdom_id | Identifier of Kingdom |
| bond_id | Identifier of Bond |
| unusual_amino_acid_id | Identifier of modification type |
| author_id | Identifier of Author |
| journal_id | Identifier of Journal |
| article_year | Year of publication of Article |
| article_title | Title of Article |
| target_species_id | Identifier of target species |
| nonstandard_experimental_conditions |  |
| hemolytic_and_cytotoxic_activities |  |
| format | xml,json,fasta |


```
SearchRequest searchRequest = new SearchRequest();
searchRequest.setSynthesisType(36);
searchRequest.setTargetGroupId(790);
searchRequest.setFormatType(FormatType.XML);
String response = searchRequest.request();
```

#### 4.ranking_search 

| Parameter | Description |
| --- | --- |
| complexity | Type of Peptide. Available values : mononer(default) |
| sequence_length | Length of sequence |
| n_terminus_id | Identifier of N Terminus |
| c_terminus_id | Identifier of C Terminus |
| bond_id | Identifier of Bond |
| unusual_amino_acid_id | Identifier of modification type |
| synthesis_type | Identifier of Synthesys Type |
| kingdom_id | Identifier of Kingdom |
| target_species_id | Identifier of target species |
| activity_measure_id | Identifier of activity measure |
| medium_id | Identifier of Medium |
| cfu | CFU |
| operation | compare operation, available operation : >, < , >= , <= , = |
| format | xml,json,fasta |

```
RankingSearchRequest rankingSearchRequest = new RankingSearchRequest(); 
rankingSearchRequest.setTargetSpeciesId(3232); 
rankingSearchRequest.setActivityMeasureId(72); 
rankingSearchRequest.setActivity(100f); 
rankingSearchRequest.setFormatType(FormatType.XML);
String response = rankingSearchRequest.request();
```

