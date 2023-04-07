import anndata as ad
import scanpy as sc
import scipy as sp
import glob
import numpy as np


# test names:
# uncompressed_filename = './data/replicate1/untreated.tsv'
# saved_filename = './data/untreated1.h5ad'

# tsvs by default
def text_to_adata(input_file: str, output_file: str, delimiter='\t'):
    adata = sc.read_csv(input_file, delimiter=delimiter)
    adata.X = sp.sparse.csr_matrix(adata.X, dtype=np.float32)
    adata = adata.transpose()
    adata.write_h5ad(output_file)


# data_dir = "/home/dennis/Downloads/replicate1/"
# output_dir = "./data/"

data_dir = "/home/dennis/Downloads/replicate2/"
output_dir = "./data/replicate2/"

for filepath in glob.iglob(data_dir + "*.tsv"):
    outfile = output_dir + (filepath.split('/')[-1]).split('.')[0] + ".h5ad"
    text_to_adata(filepath, outfile)
    