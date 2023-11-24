#!/bin/bash

cd /Users/cmdb/qbb2023-answers/week5/hw

# 1.2
# for sample in *.fastq
# do 
# 	echo $sample
# 		bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \
# 		sacCer3.fa \
# 		${sample} > ${sample}.sam
# done

# 1.3
# for sam in *.sam
# do
# 	samtools sort -o `${sam} - ".sam"`.bam -O bam ${sam}
# done

for bam in *.bam
do
	samtools index ${bam}
	freebayes -f sacCer3.fa -p 1 --genotype-qualities ${bam} > ${bam}.vcf
done

