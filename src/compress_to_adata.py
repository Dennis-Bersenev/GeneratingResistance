import anndata as ad
import scanpy as sc
import scipy as sp


# TODO: make this its own thing which can take command line arguments etc
uncompressed_filename = './data/replicate1/untreated.tsv'
saved_filename = './data/untreated1.h5ad'

# for tsv
adata = sc.read_csv(uncompressed_filename, delimiter='\t')
adata.X = sp.sparse.csr_matrix(adata.X)

adata.write_h5ad(saved_filename)