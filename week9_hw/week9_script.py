#!/usr/bin/env python

# 1.1
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)


# 1.2
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]
counts_df_normed = np.log2(counts_df_normed + 1)


# 1.3
full_design_df = pd.concat([counts_df_normed, metadata], axis=1)


# # 1.4
# model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
# results = model.fit()

# slope = results.params[1]
# pval = results.pvalues[1]

# # 1.5
# # MAKE NEW DATAFRAME WITH MY HOMEMADE ANAYLSIS
# gene_names = full_design_df.columns[:-3]
# slopes = []
# pvalues = []

# for i in range(len(gene_names)):
# 	gene = gene_names[i]
# 	model = smf.ols(formula = 'Q(gene_names[i]) ~ SEX', data=full_design_df)
# 	results = model.fit()

# 	slope = results.params[1]
# 	slopes.append(slope)

# 	pval = results.pvalues[1]
# 	pvalues.append(pval)

# homemade_analysis = pd.DataFrame({'GeneName': gene_names, 'Slope': slopes, 'P-value': pvalues})
# homemade_analysis['P-value'] = homemade_analysis['P-value'].fillna(1.0)

# fdr = multitest.fdrcorrection(homemade_analysis['P-value'], alpha=0.05, method='indep', is_sorted=False)

# homemade_analysis = pd.DataFrame({'GeneName': gene_names, 'Slope': slopes, 'P-value': pvalues, 'FDR': fdr[1]})
# homemade_analysis.to_csv('homemade_analysis.txt')

# find top 10%
homemade_analysis = pd.read_csv("homemade_analysis.txt", index_col = 0)

sig_homemade_results = homemade_analysis.loc[homemade_analysis["FDR"] <.1, :]

sig_genes = sig_homemade_results["GeneName"].tolist()

with open("homemade_significangt_genes.txt", "w") as file:
	for gene in sig_genes:
		file.write(str(gene)+"\n")



# EXERCISE 2:
# 2.1

# dds = DeseqDataSet(
#     counts=counts_df,
#     metadata=metadata,
#     design_factors="SEX"
# )

# dds.deseq2()
# stat_res = DeseqStats(dds)
# stat_res.summary()
# results = stat_res.results_df

# results.to_csv('pydeseq_results.csv')


results = pd.read_csv("pydeseq_results.csv", index_col = 0)

deseq_siggenes = results.loc[results["padj"]<.1, :]



with open("pydeseq_significangt_genes.txt", "w") as file:
	for gene in deseq_siggenes.index:
		file.write(str(gene)+"\n")

my_set = set(sig_genes)
pydeseq_set = set(deseq_siggenes.index.tolist())


intersection = my_set & pydeseq_set
union = my_set | pydeseq_set


print(len(intersection))

jaccard = len(intersection) / len(union) * 100

print(str(jaccard)+"%")



# EXERCISE 3
import matplotlib.pyplot as plt

sig_diff = results.loc[(results['log2FoldChange'].abs() > 1)&(results["padj"]<.1), : ]

y_all = -np.log10(results['padj'])
y_sig = -np.log10(sig_diff['padj'])

fig, ax = plt.subplots()
ax.scatter(x=results['log2FoldChange'], y=y_all, c="blue", label="insignificant differences")
ax.scatter(x=sig_diff['log2FoldChange'], y=y_sig, c="red", label="significant differences")
ax.set_xlabel("log2 fold change")
ax.set_ylabel("-log10(corrected p-value)")
ax.set_title("Differential expression of genes between sexes")
ax.legend()
fig.savefig("volcano.png")


