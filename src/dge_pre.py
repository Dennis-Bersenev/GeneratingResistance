import scanpy as sc
import utils


def process_and_save_data(adata, feature_space, neighb, outpath):
    adata = utils.process_adata(adata)
    adata = utils.cluster_adata(adata, feature_space, neighb)
    adata.write_h5ad(outpath)
    

adata1 = sc.read('./data/MrVIoutputs/bacdrop_pp.h5ad')
adata2 = sc.read('./data/MrVIoutputs/bacdrop_pp.h5ad')
adata3 = sc.read('./data/MrVIoutputs/bacdrop_pp.h5ad')
adata4 = sc.read('./data/MrVIoutputs/bacdrop_pp.h5ad')


process_and_save_data(adata1, 'X_mrvi_z', 'gauss', './data/dge_analysis_inputs/adata_z_gauss.h5ad')
process_and_save_data(adata2, 'X_mrvi_u', 'gauss', './data/dge_analysis_inputs/adata_u_gauss.h5ad')

process_and_save_data(adata3, 'X_mrvi_z', 'knn', './data/dge_analysis_inputs/adata_z_knn.h5ad')
process_and_save_data(adata4, 'X_mrvi_u', 'knn', './data/dge_analysis_inputs/adata_u_knn.h5ad')
