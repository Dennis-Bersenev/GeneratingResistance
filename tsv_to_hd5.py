import numpy as np
import pandas as pd
from IPython.display import clear_output

CHUNK_SIZE = 4 * (2 ** 10)

filename = './data/replicate1/test.tsv'

iter_tsv = pd.read_table(
    filename, iterator=True,
    encoding='utf-8', chunksize=CHUNK_SIZE)

cnt = 0
for ix, chunk in enumerate(iter_tsv):
    chunk.to_hdf("test_data.h5", 'cellmx', format='table', append=True)
    cnt += CHUNK_SIZE
    clear_output(wait=True)
    print(f"Processed {cnt:,.0f} coordinates..")

# with open("GSM5456486_MGH66_Abx3_P1_align2._CDS.tsv.gz") as data:
# adata = ad.read_csv("./../data/GSM5456486_MGH66_Abx3_P1_align2._CDS.tsv.gz", delimiter='\t')
# adata = sc.read_text("./../data/replicate1/")
# sc.read_10x_mtx("./../data/GSM5456486_MGH66_Abx3_P1_align2._CDS.tsv.gz")
# chunksize = 10 ** 8
# for chunk in pd.read_csv(filename, chunksize=chunksize):
#     process(chunk)