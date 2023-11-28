#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

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

# AFS
af = []
file = open("AF.frq", 'r')
file = file.readlines()
for line in file[1:]:
	line = line.rstrip().split()
	af.append(float(line[4]))

# histogram for AFS
fig, ax = plt.subplots()
ax.hist(af, bins=20, range=(0, .6))
ax.set_title("Allele frequency spectrum")
ax.set_xlabel("Allele frequency")
# plt.show()
fig.savefig("afs.png")



# EXERCISE 3
gs451 = pd.read_csv("gwas_GS451_IC50.assoc.linear", delim_whitespace=True)
cb1908 = pd.read_csv("gwas_CB1908_IC50.assoc.linear", delim_whitespace=True)

x_gs = gs451.loc[:,2]
y_gs = gs451.loc[:,8]
y_gs = -np.log(y_gs)

x_cb = cb1908.loc[:,2]
y_cb = gs451.loc[:,8]
y_cb = -np.log(y_cb)

fig, ax = plt.subplots(2,1)
ax[0,0].set_title("GS451")
ax[0,0].scatter(x_gs, y_gs)
ax[1,0].set_title("CB1908")
ax[1,0].scatter(x_cb, y_cb)
fig.savefig("manhattan.png")






