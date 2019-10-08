# STREAM.DimensionReduction

Perform dimension reduction.

* nb_pct: `float`, optional (default: 0.1)
    The percentage neighbor cells (only valid when 'mlle','se', or 'umap' is specified).
* n_components: `int`, optional (default: 3)
    Number of components to keep.
* n_jobs: `int`, optional (default: all available cpus)
    The number of parallel jobs to run.
* feature: `str`, optional (default: 'var_genes')
    Choose from {{'var_genes','top_pcs','all'}}
    Feature used for dimension reduction.
    'var_genes': most variable genes
    'top_pcs': top principal components
    'all': all genes
* method: `str`, optional (default: 'mlle')
    Choose from {{'mlle','umap','pca'}}
    Method used for dimension reduction.
    'mlle': Modified locally linear embedding algorithm
    'se': Spectral embedding algorithm
    'umap': Uniform Manifold Approximation and Projection
    'pca': Principal component analysis
* eigen_solver: `str`, optional (default: None)
    For 'mlle', choose from {{'arpack', 'dense'}}
    For 'se', choose from {{'arpack', 'lobpcg', or 'amg'}}
    The eigenvalue decomposition strategy to use
