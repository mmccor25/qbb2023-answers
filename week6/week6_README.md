1.1
$ plink --vcf genotypes.vcf --pca --out pca


2.1
$ plink --vcf genotypes.vcf --freq --out AF


3.1
$ plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar pca.eigenvec --allow-no-sex --out gwas_CB1908_IC50
$ plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar pca.eigenvec --allow-no-sex --out gwas_GS451_IC50


3.4
Gene for CB1908 phenotype: DIP2B
This SNP might cause a loss-of-function mutation that leads to the phenotype