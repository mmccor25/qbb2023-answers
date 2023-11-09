#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

def main():
	nanopore_fname, bisulfite_fname, out_fname = sys.argv[1:4]

	# Load data from files
	nanopore = load_data(nanopore_fname)
	bisulfite = load_data(bisulfite_fname)

	# create sets
	nanopore_set = set()
	nanopore_coverage = []
	for i in range(len(nanopore)):
		nanopore_set.add(nanopore[i][0])
		nanopore_coverage.append(int(nanopore[i][1]))


	bisulfite_set = set()
	bisulfite_coverage = []
	for i in range(len(bisulfite)):
		bisulfite_set.add(bisulfite[i][0])
		bisulfite_coverage.append(int(bisulfite[i][1]))

	# separated
	total = nanopore_set.union(bisulfite_set)
	total_count = len(total)
	print("There are " + str(total_count) + " total CpG sites.")

	both = nanopore_set.intersection(bisulfite_set)
	both_count = len(both)
	print(str(len(both)) + " CpG sites, or " + str(both_count/total_count*100) + " percent of the total is methylated.")

	nanopore_only = nanopore_set.difference(both)
	nanopore_only_count = len(nanopore_only)
	print("There are " + str(nanopore_only_count) + " CpG sites that are nanopore only.")


	# Make plot
	# Coverage histogram
	fig, ax = plt.subplots(3, 1)
	ax[0].hist(nanopore_coverage, label="Nanopore", bins=20, range=(0, 100), alpha=.5, color="yellow")
	ax[0].hist(bisulfite_coverage, label="Bismark", bins=20, range=(0, 100), alpha=.5, color="magenta")
	ax[0].set_title("Nanopore and Bismark coverage")
	ax[0].legend()

	plt.savefig(out_fname+".png")

def load_data(fname):
	data = []
	for line in open(fname):
		line = line.rstrip().split()
		data.append([line[1], line[4]]) #line[4] is coverage i think
	return data

main()