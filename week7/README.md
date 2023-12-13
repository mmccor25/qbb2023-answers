Q1: The majority of cpg sites seem to be methylated.

Q2: The Bismark coverage is overall greater with larger spread, so Bismark appears to be better.

Q3: The methylation reads are more evenly distributed with the Nanopore method.

Q4: Tumorigenesis is associated with an increase in methylation overall.

Q5: There is less methylation in DNMT3A for the tumor cells compared to normal. This makes sense, because DNA-methyltransferase, now in euchromatin, would have increased expression in cancer, meaning that there would be increased methylation of other genes (such as TSGs).

Q6: Imprinting is the inheritence of epigenetic regulation of a gene.

Q7: When I phase the reads, the program is trying to figure out which genes came from the one parent vs. the other (i.e. which genes are inherited from the same parent).

Q8: A set of reads could not be phased if both parents have the same alleles anyway.

$ python script.py ONT.cpg.chr2.bedgraph bisulfite.cpg.chr2.bedgraph out