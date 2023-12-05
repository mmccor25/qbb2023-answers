#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# pc1 = []
# pc2 = []

# pca_file = pd.read_csv("pca.eigenvec", delim_whitespace=True)
# pc1 = pca_file.iloc[:,2]
# pc2 = pca_file.iloc[:,3]

# # Plot PCA
# pca, ax = plt.subplots()
# ax.scatter(pc1, pc2, alpha=0.5)
# ax.set_title("Genotypes PCA")
# ax.set_xlabel('PC 1')
# ax.set_ylabel('PC 2')
# # plt.show()
# pca.savefig("pca_1.png")

# # EXERCISE 2

# # AFS
# af = []
# file = open("AF.frq", 'r')
# file = file.readlines()
# for line in file[1:]:
# 	line = line.rstrip().split()
# 	af.append(float(line[4]))

# # histogram for AFS
# fig, ax = plt.subplots()
# ax.hist(af, bins=20, range=(0, .6))
# ax.set_title("Allele frequency spectrum")
# ax.set_xlabel("Allele frequency")
# # plt.show()
# fig.savefig("afs.png")



# EXERCISE 3
# set up GS451
gs451 = pd.read_csv("gwas_GS451_IC50.assoc.linear", delim_whitespace=True)

x_gs = gs451.index
y_gs = gs451.loc[:,"P"]
y_gs = -np.log(y_gs)

gs_insignificant_x = []
gs_insignificant_y = []
gs_significant_x = []
gs_significant_y = []
for x,y in zip(x_gs, y_gs):
	if y > 5:
		gs_significant_x.append(x)
		gs_significant_y.append(y)
	else:
		gs_insignificant_x.append(x)
		gs_insignificant_y.append(y)

# set up CB1908
cb1908 = pd.read_csv("gwas_CB1908_IC50.assoc.linear", delim_whitespace=True)

x_cb = cb1908.index
y_cb = cb1908.loc[:,"P"]
y_cb = -np.log(y_cb)

cb_insignificant_x = []
cb_insignificant_y = []
cb_significant_x = []
cb_significant_y = []
for x,y in zip(x_cb, y_cb):
	if y > 5:
		cb_significant_x.append(x)
		cb_significant_y.append(y)
	else:
		cb_insignificant_x.append(x)
		cb_insignificant_y.append(y)



# make manhattan plot
fig, ax = plt.subplots(2,1)

ax[0].set_title("GS451")
ax[0].scatter(x_gs, y_gs)
ax[0].scatter(gs_insignificant_x, gs_insignificant_y, color ="blue")
ax[0].scatter(gs_significant_x, gs_significant_y, color="red")
ax[0].set_ylabel("Significance")
ax[0].set_xlabel("Position")


ax[1].set_title("CB1908")
ax[1].scatter(x_cb, y_cb)
ax[1].scatter(cb_insignificant_x, cb_insignificant_y, color ="blue")
ax[1].scatter(cb_significant_x, cb_significant_y, color="red")
ax[1].set_ylabel("Significance")
ax[1].set_xlabel("Position")

fig.tight_layout()
fig.savefig("manhattan.png")


# 3.3

for i in range(len(cb_significant_y)):
	if cb_significant_y[i] == max(cb_significant_y):
		cb_position = cb_significant_x[i]


for i in range(len(gs_significant_y)):
	if gs_significant_y[i] == max(gs_significant_y):
		gs_position = gs_significant_x[i]

print(cb1908.iloc[cb_position,:])

print(cb1908.iloc[gs_position,:])


