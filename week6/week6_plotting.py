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

print(len(pc2))

# Plot PCA
pca, ax = plt.subplots()
ax.scatter(pc1, pc2, alpha=0.5)
ax.set_title("Genotypes PCA")
ax.set_xlabel('PC 1')
ax.set_ylabel('PC 2')
plt.show()