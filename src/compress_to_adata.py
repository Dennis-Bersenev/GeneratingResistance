import anndata as ad
import scanpy as sc
import scipy as sp
import glob


# test names:
# uncompressed_filename = './data/replicate1/untreated.tsv'
# saved_filename = './data/untreated1.h5ad'

# tsvs by default
def text_to_adata(input_file: str, output_file: str, delimiter='\t'):
    adata = sc.read_csv(input_file, delimiter=delimiter)
    adata.X = sp.sparse.csr_matrix(adata.X)
    adata.write_h5ad(output_file)


data_dir = "./data/replicate1/"
output_dir = "./data/"

for filepath in glob.iglob(data_dir + "*.tsv"):
    outfile = output_dir + (filepath.split('/')[-1]).split('.')[0] + ".h5ad"
    text_to_adata(filepath, outfile)
    