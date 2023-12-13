#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
	nanopore_fname, bismark_fname, out_fname = sys.argv[1:4]

	# Load data from files
	nanopore = load_data(nanopore_fname)
	bismark = load_data(bismark_fname)

	# create sets
	nanopore_set = set()
	nanopore_coverage = []
	nanopore_methscores = []
	for i in range(len(nanopore)):
		nanopore_set.add(nanopore[i][0])
		nanopore_coverage.append(int(nanopore[i][2]))
		# nanopore_methscores.append(float(nanopore[i][1]))

	bismark_set = set()
	bismark_coverage = []
	bismark_methscores = []
	for i in range(len(bismark)):
		bismark_set.add(bismark[i][0])
		bismark_coverage.append(int(bismark[i][2]))
		# bismark_methscores.append(float(bismark[i][1]))


	# separated
	total = nanopore_set.union(bismark_set)
	total_count = len(total)
	print("There are " + str(total_count) + " total CpG sites.")

	both = nanopore_set.intersection(bismark_set)
	both_count = len(both)
	print(str(len(both)) + " CpG sites, or " + str(both_count/total_count*100) + " percent of the total were called by both methods.")

	nanopore_only = nanopore_set.difference(both)
	nanopore_only_count = len(nanopore_only)
	print("There are " + str(nanopore_only_count) + " CpG sites that are Nanopore only, which is " + str(nanopore_only_count/total_count*100) + " percent of the total.")

	bismark_only = bismark_set.difference(both)
	bismark_only_count = len(bismark_only)
	print("There are " + str(bismark_only_count) + " CpG sites that are Bismark only, which is " + str(bismark_only_count/total_count*100) + " percent of the total.")

	# Make plot
	# Coverage histogram
	fig, ax = plt.subplots(3, 1)
	ax[0].hist(nanopore_coverage, label="Nanopore", bins=20, range=(0, 100), alpha=.5, color="yellow")
	ax[0].hist(bismark_coverage, label="Bismark", bins=20, range=(0, 100), alpha=.5, color="magenta")
	ax[0].set_title("Nanopore and Bismark coverage")
	ax[0].legend()


	# relationship between methylation scores
	nanopore_pandas = make_pandas(nanopore)
	bismark_pandas = make_pandas(bismark)

	merged = nanopore_pandas.merge(bismark_pandas, on = "site")
	nanopore_methscores = merged.loc[:, 'methscore_x']
	bismark_methscores = merged.loc[:, 'methscore_y']

	hist2d, x, y = np.histogram2d(nanopore_methscores, bismark_methscores)
	ax[1].imshow(np.log10(1+hist2d))
	ax[1].set_title(f"Methylation scores compared. Correlation: {str(np.corrcoef(nanopore_methscores, bismark_methscores)[0,1])[:4]}" )


	# 3d: comparing tumor vs normal
	cancer_nanopore = load_data("tumor.ONT.chr2.bedgraph")
	cancer_nanopore = make_pandas(cancer_nanopore)
	cancer_nanopore.set_index("site")

	cancer_bismark = load_data("tumor.bisulfite.chr2.bedgraph")
	cancer_bismark = make_pandas(cancer_bismark)
	cancer_bismark.set_index("site")

	normal_nanopore = load_data("normal.ONT.chr2.bedgraph")
	normal_nanopore = make_pandas(normal_nanopore)
	normal_nanopore.set_index("site")

	normal_bismark = load_data("normal.bisulfite.chr2.bedgraph")
	normal_bismark = make_pandas(normal_bismark)
	normal_nanopore.set_index("site")

	bismark_compared = cancer_bismark - normal_bismark 
	notnull = bismark_compared["methscore"].notnull()
	bismark_compared = bismark_compared.loc[notnull, :]
	list_bismark_compared = []
	for i in bismark_compared["methscore"]:
		if i !=0:
			list_bismark_compared.append(i)

	nanopore_compared = cancer_nanopore - normal_nanopore 
	notnull = nanopore_compared["methscore"].notnull()
	nanopore_compared = nanopore_compared.loc[notnull, :]
	
	sites_merged = []
	list_nanopore_compared = []

	for i in nanopore_compared["methscore"]:
		if i !=0:
			list_nanopore_compared.append(i)
		#sites_merged.append(nanopore_compared[i])

	for i in normal_nanopore.index:
		 if i in cancer_nanopore.index:
		 	sites_merged.append(i)

	
	r_coeff = np.corrcoef(normal_nanopore.loc[sites_merged, 'methscore'] - cancer_nanopore.loc[sites_merged, 'methscore'], normal_bismark.loc[sites_merged, 'methscore'] - cancer_bismark.loc[sites_merged, 'methscore'])[0, 1]
	

	ax[2].violinplot([list_nanopore_compared, list_bismark_compared])
	ax[2].set_title("Tumor vs. Cancer methylation scores")
	ax[2].set_xticks([1,2], labels=["Nanopore", "Bismark"])

	#both = list_nanopore_compared.intersection(list_bismark_compared)
	#print(both)

	#r_coeff = np.corrcoef(list_nanopore_compared, list_bismark_compared)
	print(r_coeff)
	ax[2].set_title(f"Methylation scores compared. Correlation: {str(r_coeff)[:4]}" )


	# plt.show()
	fig.tight_layout()
	plt.savefig(out_fname+".png")

def load_data(fname):
	data = []
	for line in open(fname):
		line = line.rstrip().split()
		data.append([float(line[1]), float(line[3]), float(line[4])]) #line[4] is coverage i think
	return data

def make_pandas(fname):
	df = pd.DataFrame(fname, columns=['site', 'methscore', 'coverage'])
	return df

main()