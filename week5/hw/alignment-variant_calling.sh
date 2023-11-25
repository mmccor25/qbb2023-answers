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

for bam in *.bam
do
	samtools index ${bam}
done


# EXERCISE 2
ls *.bam > bam_inputs.txt
freebayes -L bam_inputs.txt -f sacCer3.fa -p 1 --genotype-qualities > variant_calls.vcf


# # 2.2
# for file in *.vcf
# do 
# 	vcffilter -f "QUAL >= 20" $file > ${file%.*}_quality.vcf
# done

# 2.3
# for file in *_quality
# do
# 	vcfallelicprimitives -k -g ${file} > ${file}_biallelic.vcf
# done

# 2.4
# for biallelic in *_biallelic.vcf
# do
# 	snpEff ann $biallelic > ${biallelic%.*}.vcf_final

# head final








