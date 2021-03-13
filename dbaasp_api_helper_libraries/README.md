
# DBAASP API Helper Libraries

#### Please see documentations for following Programing languages

* [Java](https://github.com/dbaasp/dbaasp_api_helper_libraries/blob/master/README-JAVA.md)
* [Phyton](https://github.com/dbaasp/dbaasp_api_helper_libraries/blob/master/README-PYTHON.md)
* [Ruby](https://github.com/dbaasp/dbaasp_api_helper_libraries/blob/master/README-RUBY.md)


#### In case you are not programmer, please see *CURL* and *GET* examples bellow


###  1.lookup 

| Parameter | Description |
| --- | --- |
| lookup_type | available types: target_object, target_group, n_terminus, c_terminus, synthesis_type, complexity, kingdom, intra_chain_bond, unusual_amino_acid, unit, activity_measure, author, journal, target_species, mammalian_cell, medium |
| format | xml,json,tab |


#### GET
```
https://dbaasp.org/api/v1?query=lookup&lookup_type=target_group&format=xml
```
#### CURL
```
curl -v -L -d "query=lookup&lookup_type=target_group&format=json" https://dbaasp.org/api/v1
```




###  2.peptide_card 

| Parameter | Description |
| --- | --- |
| peptide_id | peptide card id |
| format | xml,json,fasta |


#### GET
```
https://dbaasp.org/api/v1?query=peptide_card&peptide_id=107&format=json
```
#### CURL
```
curl -v -L -d "query=peptide_card&peptide_id=107&format=json" https://dbaasp.org/api/v1
```


### 3.search 

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


#### GET
```
https://dbaasp.org/api/v1?query=search&target_group_id=790&synthesis_type=36&format=xml
```
#### CURL 
```
curl -v -L -d "query=search&target_group_id=790&synthesis_type=36&format=xml" https://dbaasp.org/api/v1
```


###  2.ranking_search 

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


#### GET
```
https://dbaasp.org/api/v1?query=ranking_search&target_species_id=3232&activity_measure_id=72&operation=<=&activity=0.5&format=json
```
#### CURL 
```
curl -v -L -d "query=ranking_search&target_species_id=3232&activity_measure_id=72&operation=<=&activity=0.5&format=json" https://dbaasp.org/api/v1
```

