#!/usr/bin/env python

import scanpy as sc
import matplotlib.pyplot as plt

# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

# EXERCISE 1
# 1.1
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)

# 1.2
sc.tl.leiden(adata)

# 1.3
sc.tl.umap(adata, maxiter=900)
sc.tl.tsne(adata)

fig, ax = plt.subplots(ncols=2)
sc.pl.umap(adata, ax=ax[0], color='leiden', title="UMAP", show=False)
sc.pl.tsne(adata, ax=ax[1], color='leiden', title="t-SNE", show=False)
fig.tight_layout()
fig.savefig("umap_and_tsne.png")


# EXERCISE 2
# 2.1
wilcoxon_adata = sc.tl.rank_genes_groups(adata, method='wilcoxon', groupby='leiden', use_raw=True, copy=True)
logreg_adata = sc.tl.rank_genes_groups(adata, method='logreg', groupby='leiden', use_raw=True, copy=True)

# 2.2
sc.pl.rank_genes_groups(wilcoxon_adata, n_genes=25, title="Top 25 genes: Wilcoxon", sharey=False, show=False, use_raw=True, save="_wilcoxon.png")
sc.pl.rank_genes_groups(logreg_adata, n_genes=25, title="Top 25 genes: logistic regression", save="_logreg.png", sharey=False, show=False, use_raw=True)


# EXERCISE 3
# 3.1
leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne
adata.write('filtered_clustered_data.h5')

# 3.2
# CCL5
fig, ax = plt.subplots(ncols=3)
sc.pl.umap(adata, ax=ax[0], color='LYZ', title="LYZ", show=False) # myeloid cells
sc.pl.umap(adata, ax=ax[1], color='GNLY', title="GNLY", show=False) # natural killer cells
sc.pl.umap(adata, ax=ax[2], color='CD79A', title="CD79A", show=False) # B-cells
fig.tight_layout()
fig.savefig("3.2.png")

# 3.3
adata.rename_categories(key='leiden', categories=["0", "myeloid", "B-cells", "3", "4", "NK cells", "6", "7"])
fig, ax = plt.subplots()
sc.pl.umap(adata, ax=ax, color='leiden', title="UMAP", show=False)
fig.tight_layout()
fig.savefig("3.3_umap_with_gene_names.png")



