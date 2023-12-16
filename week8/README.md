Command to run convert_washU_to_UCSC.py:
$ python convert_washU_to_UCSC.py raw/Design/h19_chr20and21.baitmap output/data/output_washU_text.txt ucsc_output.bed




1.1
<!-- inputs = ["raw/PCHIC_Data/GM_rep1.chinput", "raw/PCHIC_Data/GM_rep2.chinput", "raw/PCHIC_Data/GM_rep3.chinput"]
output_prefix = "output"
design_dir = "raw/Design"
en_feat_list = "raw/Features"
export_format = washU_text -->

$ Rscript runChicago.R raw/PCHIC_Data/GM_rep1.chinput,raw/PCHIC_Data/GM_rep2.chinput,raw/PCHIC_Data/GM_rep3.chinput output --design-dir raw/Design --en-feat-list raw/Features -e washU_text


Q1: 
CTCF: CTCF is present at TAD boundaries, and CTCF-binding regions are expected to interact with each other. Accordingly, we see moderate overlap with interactions.

H3K27ac: This acetylated DNA is typically open, so we expect more (enhancer) interactions with promoters. Surprisingly, the overlap with significant interactions is high. 

H3K27me3: This modification is associated with heterochromatin, so we expect fewer interactions with promoters. Accordingly, this feature has the fewest overlaps with significant interactions.

H3K4me1: This DNA is typically in DNA becoming euchromatin, so we expect moderate interaction. This has the highest overlap with significant interactions, which makes sense because these regions would logically have increased promoter binding to activate the genes within them.

H3K4me3: This is associated with open chromatin, so there should be more interaction. Understandably, we see moderate-to-high overlap with interactions.

H3K9me3: H3K9 is associated with closed chromatin, so we expect fewer interactions. We see moderate overlap, which somewhat aligns with our expectation.




