#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

pc1 = []
pc2 = []

with open('pca.eigenvec', 'r') as file:
	file = file.readlines()
for line in file:
	pc1.append(float(line[2]))
	pc2.append(float(line[3]))

# Plot PCA
pca, ax = plt.subplots()
ax.scatter(pc1, pc2, alpha=0.5)
ax.set_title("Genotypes PCA")
ax.set_xlabel('PC 1')
ax.set_ylabel('PC 2')
# plt.show()
pca.savefig("pca_1.png")

# EXERCISE 2

# 2.1
af = []
file = open("AF.frq", 'r')
file = file.readlines()
for line in file[1:]:
	line = line.rstrip().split()
	af.append(float(line[4]))


fig, ax = plt.subplots()
ax.hist(af, bins=20, range=(0, .6))
ax.set_title("Allele frequency spectrum")
ax.set_xlabel("Allele frequency")
# plt.show()
fig.savefig("afs.png")
