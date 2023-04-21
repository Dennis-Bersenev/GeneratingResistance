# GeneratingResistance
<pre>
Environment Setup:
  conda create -n GenRes python=3.9 
  conda activate GenRes 
  conda install -c conda-forge scanpy python-igraph leidenalg 
  conda install -c anaconda ipykernel <br/>

Overview of the notebooks:
  bacdrop - loads in the adata object containing all samples and replicates of Klebsiella pneumoniae MGH 66 used by ma et al<sup>1</sup>.
  
  bacdrop_exploration - clustering and visualisation of MrVI<sup>2</sup> output after it has been normalised using standard scanpy tools<sup>3</sup>.
  
  bacdrop_alt_exploration - clustering and visuals corresponding to output of MrVI<sup>2</sup> where data is filtered before going through the model, 
                            and where all normalisations steps have been omitted.  

  combine_data - how the bacdrop<sup>1</sup> data was combined.


References:
[1] Ma, P., Amemiya, H. M., He, L. L., Gandhi, S. J., Nicol, R., Bhattacharyya, R. P., Smillie, C. S., & Hung, D. T. (2023). Bacterial 
      droplet-based single-cell RNA-seq reveals antibiotic-associated heterogeneous cellular states. Cell, 186(4), 
      S0092-8674(23)000028. https://doi.org/10.1016/j.cell.2023.01.002

[2] Boyeau, P., Hong, J., Gayoso, A., Jordan, M. I., Azizi, E., & Yosef, N. (2022). Deep generative modeling for quantifying sample-level 
      heterogeneity in single-cell omics. BioRxiv. https://doi.org/10.1101/2022.10.04.510898

[3] Wolf, F., Angerer, P. & Theis, F. SCANPY: large-scale single-cell gene expression data analysis. Genome Biol 19, 15 (2018).
      https://doi.org/10.1186/s13059-017-1382-0

</pre>
