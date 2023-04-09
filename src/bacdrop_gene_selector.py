import anndata as ad
import scanpy as sc
import pandas as pd


# (TODO: whole idea of the project is basically to use these INSTEAD of UMAP/tSNE etc in the standard Seurat/Scanpy analysis pipelines!)

adata = sc.read('./data/MrVIoutputs/bacdrop.h5ad')

sc.pp.normalize_total(adata, target_sum=5000)
sc.pp.log1p(adata)
sc.pp.filter_cells(adata, min_genes=40)
adata.raw = adata


sc.pp.neighbors(adata, use_rep='X_mrvi_z', knn=False, method='gauss')
sc.tl.leiden(adata)
sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')

df = pd.DataFrame(adata.uns['rank_genes_groups']['names'])

df.to_csv('./out/genes.csv')

