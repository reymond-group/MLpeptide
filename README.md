# Machine Learning Designs Non-Hemolytic Antimicrobial Peptides 

### Scope
Antibiotic resistance is one of the major threats to global public health, and antimicrobial peptides (AMPs) are an important resource against it. However, the discovery of novel AMPs is challenging because they are often toxic towards human blood cells. Here, we set to understand if machine learning (ML) can help in design non-hemolytic AMPs and accelerate the discovery of novel AMPs. 

### Methodology
We extracted a highly reliable dataset of AMPs and non-AMPs, as well as hemolytic and non-hemolytic peptides from the DBAASP, a manually curated antimicrobial peptide database. We used the data to train a generative peptide model (prior model), an AMP activity classifier, and a hemolysis classifier. Two copies of the prior model were fine-tuned using active and non-hemolytic peptides against specific strains: P. aeruginosa/A. baumannii and S. aureus, respectively. The fine-tuned models were sampled, and the generated sequences were filtered using the implemented classifiers, basic physicochemical properties, and novelty criteria to obtain short peptides of maximum 15 residues with at least 5 mutations from the sequences in DBAASP. 

### Results
Our best compounds GN2 and GP6 are highly active, non-hemolytic and they show antimicrobial activity also towards multidrug-resistant strains.  

### This repository contains the code for:
- DBAASP AMP actvity data (notebook 01) and hemolyisis data (notebook 01b) extraction
- implementation of the AMP activity classifiers (NB, RF, SVM notebook 02; RNN notebook 03; RNN scr. labels notebook 04) and their evaluations
- implementation of the hemolysis classifiers (NB, RF, SVM notebook 02b; RNN notebook 03b; RNN scr. labels notebook 04b) and their evaluations
- implementation of the AMPs RNN generative prior model (notebook 05);
- fine-tuning of the generative model through transfer learning (P. aeruginosa/A. baumannii notebook 06; S. aureus notebook 07)
- properties calculation of the generated sequences (notebook 08)
- properties analysis of the generated sequences (notebook 09)
- selection for synthesis procedure (notebook 10)

to predict the apha helix % we used [SPIDER3](https://sparks-lab.org/server/spider3/)

### required environment installation:
- `conda env create -f environment.yml`
- `conda activate aipep`