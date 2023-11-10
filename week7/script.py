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
	plt.show()

	plt.savefig(out_fname+".png")

	print()


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