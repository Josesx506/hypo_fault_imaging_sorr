# Hypocenter-based 3D Imaging of Active Faults

The code in this repository allows to image active faults in 3D based on relatively relocated hypocenter datasets after the method presented by Truttmann et al. (2023).

## Scientific publication
If you use the code in this repository please cite the following references:
- Truttmann, S., Diehl, T., Herwegh, M. (2023). Hypocenter-based 3D Imaging of Active Faults: Method and Applications in the Southwestern Swiss Alps. JGR, DOI xxx.
- Truttmann, S., Diehl, T., Herwegh, M. (2023). Hypocenter-based 3D Imaging of Active Faults: Method and Applications in the Southwestern Swiss Alps [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.7487904
- Truttmann, S. (2023). hypo_fault_imaging [Software]. Github-Zenodo. DOI xxx

## Requirements
The following dependencies need to be installed by the user (we recommend using conda):
- numba
- obspy
- scikit-learn (version 0.23.2)
- FB8 (https://github.com/tianluyuan/sphere)
- mplstereonet (https://github.com/joferkington/mplstereonet)
- spherecluster (https://github.com/jasonlaska/spherecluster)
    - Important: replace the files "spherical_kmeans.py" and "von_mises_fisher_mixture.py" with the updated versions thereof, provided in the folder Misc in this repository

The currently supported version of Python is 3.8
