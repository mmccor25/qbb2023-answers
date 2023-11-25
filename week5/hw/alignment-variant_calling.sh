#!/bin/bash

cd /Users/cmdb/qbb2023-answers/week5/hw

# # 1.2
# for sample in *.fastq
# do 
# 	echo $sample
# 		bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \
# 		sacCer3.fa \
# 		${sample} > ${sample%.*}.sam
# done

# # 1.3
# for sam in *.sam
# do
# 	samtools sort -o ${sam%.*}.bam -O bam ${sam}
# done

# for bam in *.bam
# do
# 	samtools index ${bam}
# done


# EXERCISE 2
# 2.1
# ls *.bam > bam_inputs.txt
# freebayes -L bam_inputs.txt -f sacCer3.fa -p 1 --genotype-qualities > variant_calls.vcf


# 2.2
# vcffilter -f "QUAL > 20" variant_calls.vcf > quality_variant_calls.vcf

# 2.3
# vcfallelicprimitives -k -g quality_variant_calls.vcf > biallelic.vcf

# 2.4
snpEff -download R64-1-1.105 biallelic.vcf > final.vcf

head -n 100 final.vcf > head_final.vcf








