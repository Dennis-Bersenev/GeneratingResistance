import anndata as ad
import scanpy as sc
import pandas as pd
import scipy as sp
import glob
import numpy as np
import pickle as pkl


"""
Discovers different cell types, and identifies the representative genes of each type.

Parameters
adata: stores the Cell x Gene matrix and all associated meta information
feature_space: which matrix of observations to use in generating the neighborhood graph (select from adata.obsm)
neighbor_method: method to generate neighborhood graph (only supports 'gauss' and knn)   

Return
Dataframe containing each cluster's genes ranked from most->least indicative of the cell state associated with the cluster 
"""
def mrvi_identify_cell_states(adata: ad.AnnData, feature_space: str, neighbor_method: str):
    
    # Assumes Bacdrop replicate 1 cell read depth of 5,000
    sc.pp.normalize_total(adata, target_sum=5000)
    sc.pp.log1p(adata)
    sc.pp.filter_cells(adata, min_genes=40)
    adata.raw = adata

    if (neighbor_method == 'gauss'):
        sc.pp.neighbors(adata, use_rep=feature_space, knn=False, method='gauss')
    else:
        sc.pp.neighbors(adata, use_rep=feature_space, knn=True)

    sc.tl.leiden(adata)
    sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
    df = pd.DataFrame(adata.uns['rank_genes_groups']['names'])

    return df


"""
Save genes mrvi finds to a text file.

Parameters
ranked_groups: a Dataframe output by @mrvi_identify_cell_states
outfile: file path of where to save results to
n_genes: the number of top genes to save from all the clusters (default is all)   

Return
"""
def write_cell_state_genes(ranked_groups: pd.DataFrame, outfile: str, n_genes=0):

    if n_genes == 0:
        ranked_groups.to_csv('./out/genes.csv')
    else:
        df = ranked_groups.head[n_genes]
        df.to_csv('./out/genes.csv')




"""
Saves files in any text format to anndata objects in h5ad file format.

Parameters
input_file: path to the file to save
output_file: desired location to save the results
delimiter: seperator used between entries in the text file (eg. ',' for csv)

Return
"""
def text_to_adata(input_file: str, output_file: str, delimiter='\t'):
    adata = sc.read_csv(input_file, delimiter=delimiter)
    adata.X = sp.sparse.csr_matrix(adata.X, dtype=np.float32)
    adata = adata.transpose()
    adata.write_h5ad(output_file)


"""
Saves all files with given format in a directory to adata objects in h5ad format to specified directory. 
"""
def directory_to_adata(data_dir: str, output_dir: str):
    for filepath in glob.iglob(data_dir + "*.tsv"):
        outfile = output_dir + (filepath.split('/')[-1]).split('.')[0] + ".h5ad"
        text_to_adata(filepath, outfile)


"""
Convert and save the given object as a bytestream for quick future reloads. 
"""
def write_pickle(object, save_path: str):
    with open(save_path, 'wb') as outstream:
        pkl.dump(object, outstream)

"""
Load in a pickled object. 
"""
def load_pickle(object_name, save_path: str):
    with open(save_path, 'rb') as instream:
        object_name = pkl.load(instream)
