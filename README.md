# InPACT

InPACT is a computational method designed to identify and quantify IPA sites via the examination of contextual sequence patterns and RNA-seq reads alignment. InPACT includes following parts:

* Identify skipped and composite IPA sites.
* Infer novel IPA transcripts.
* Calculate relative usage of novle IPA isoforms based on transcript-level abundance.

## Installation
InPACT consists of both Python and Bash scripts. A conda virtual environment can be created using the provided `environment.yml` file.

1. Clone the repository:
```
git clone https://github.com/YY-TMU/InPACT.git
```

2. Create the environment:
```
conda env create -f environment.yml
conda activate InPACT
```

3. The installation takes about 5 to 8 minutes. If installation was sucessfull, InPACT command is available:
```
InPACT -h
```
    
## Usage
### 1. Identify IPA sites

Based on the human reference genome (GRCh38), we provided an annotation of potential IPA sites predicted from the sequence module that could be used directly.

In the following link, annotation file for GRCh38 of RefSeq could be downloaded.
* [Human (hg38)](https://hgdownload.soe.ucsc.edu/goldenPath/archive/hg38/ncbiRefSeq/109.20211119/hg38.109.20211119.ncbiRefSeq.gtf.gz)

In the following link, test file could be downloaded.
* [Test data](https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos3/sra-pub-zq-22/SRR007/647/SRR7647801.sralite.1)

The following options are available in this part: 
* --input_file/-i: A BAM file that would be used to predict IPA sites and it should be sorted by coordinates.
* --annotation_file/-a: GTF file with annotated transcripts (RefSeq).
* --ipa_sites/-s: Regions from 20nt upstream to potential polyA sites, with columns for gene, chromosome, start, end, and strand.
* --paired/-p: Whether or not the input bam file is paired. [default=True]
* --minimum_spliced_reads_for_skipped: Minimum number of spliced reads required to consider the potential skipped terminal exon. [default=5]
* --minimum_span_reads_for_composite: Minimum number of reads that cross the boundary required to consider the potential composite terminal exon. [default=10]
* --parallel/-P: Number of the threads. [default=1]

**Command**
```
InPACT -i sample.bam -a RefSeq.gtf -s InPACT_polyAsites.hg38.saf -P 5 
```

### 2.Infer novel transcripts

To assemble novel transcripts, a reference genome in FASTA format and a reference gene annotation in GTF format are required.

**Command**
```
InPACT_transcript --predict_terminal predict.result.txt --annotated_gtf RefSeq.gtf --fa_path genome.fa --save_gtf merged.gtf
```

### 3.Calculate usage of IPA sites

[Salmon](https://github.com/COMBINE-lab/salmon) is used to index and quantify the transcriptome, and then the usage is calculated. 

**Command**
```
InPACT_quantify --transcript_tpm quant.sf --annotation_file merged.gtf --ipa_info predict.result.txt --save_file ipa_usage.txt
```

InPACT takes about an hour to run the test file using five cores. The final output format is as follows:

Column | Description
------ | -----------
Terminal exon | Intronic terminal exons for IPA sites
IPA type | Type of IPA sites (Skipped or composite)
Gene | Gene symbols
Upstream coordinate | The 3’ end of the predicted terminal exon’s upstream exon
PolyAsite | IPA sites
IPA usage | PAU estimate
