#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HYPOCENTER-BASED 3D IMAGING OF ACTIVE FAULTS
Example script of how to conduct the sensitivity analysis for the input parameters r_nn (search radius) and dt_nn (search time window).

Please cite: Truttmann et al. (2023). Hypocenter-based 3D Imaging of Active Faults: Method and Applications in the Southwestern Swiss Alps.

@author: Sandro Truttmann
@contact: sandro.truttmann@geo.unibe.ch
@license: GPL-3.0
@date: December 2022
@version: 1.0
"""

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import numpy as np
from mycolorpy import colorlist as mcp
import os
import sys
sys.path.insert(0, './src')
import fault_network, model_validation, stress_analysis

# Specify the different r_nn and dt_nn parameters to be assessed
# (example: St. Leonard)
r_nn_list = [50, 100, 200, 400, 600, 800]
dt_nn_list = [24, 48, 168, 8766, 26298, 999999]


# ##########################    Input parameters     ###########################
input_params = {
    ###     Hypocenter input file
    'hypo_file' : './data_examples/StLeonard/hypoDD_StLeonard.txt',        # File location
    'hypo_sep' : '\t',                                                 # Separator
    ###     Output directory
    'out_dir' : os.getcwd(),
    ###     "Fault network reconstruction" module settings
    'n_mc' : 1000,                      # number of Monte Carlo simulations
    'r_nn' : 100,                       # search radius [m] of nearest neighbor search
    'dt_nn' : 26298,                    # search time window [h]
    'mag_type' : 'ML',                  # magnitude type: 'ML' or 'Mw'
    ###     "Model Validation" module settings
    'validation_bool' : True,
    'foc_file' : './data_examples/StLeonard/FocalMechanisms_StLeonard.txt',
    'foc_sep' : ';',
    'foc_mag_check' : True,             # check focal magnitude (recommended)
    'foc_loc_check' : True,             # check focal location (recommended)
    ###     "Automatic Classification" module settings
    'autoclass_bool' : True,
    'n_clusters' : 2,                   # number of expected classes
    'algorithm' : 'vmf_soft',           # clustering algorithm
    'rotation' : True,                  # rotate poles before analysis (recommended for vertical faults)
    ###     "Fault Stress Analysis" module settings
    'stress_bool' : True,
    'S1_trend' : 301,                   # σ1 trend
    'S1_plunge' : 23,                   # σ1 plunge
    'S3_trend' : 43,                    # σ3 trend
    'S3_plunge' : 26,                   # σ3 plunge
    'stress_R' : 0.35,                  # Stress shape ratio
    'PP' : 0,                           # Pore pressure
    'fric_coeff' : 0.75                 # Friction coefficient
}

# Combine the needed modules of the file "runfile.py" in a function
def runfile_function(r_nn, dt_nn):
        
    ###############################################################################
    # Fault network reconstruction
    (data_input, data_output,
    per_X, per_Y, per_Z) = fault_network.faultnetwork3D(input_params)
    
    ###############################################################################
    # Model Validation
    data_input, data_output = model_validation.focal_validation(input_params,
                                                                data_input,
                                                                data_output)

    
    return data_input, data_output, input_params

# Loop over the different combinations of r_nn and dt_nn and plot the cumulative distributions thereof
fig, axs = plt.subplots(nrows=1, ncols=1,
                        figsize=(10, 10))
color_count = 0
cmap = mcp.gen_color(cmap='viridis', n=len(r_nn_list)*len(dt_nn_list))
for r_nn in r_nn_list:
    for dt_nn in dt_nn_list:
        now = datetime.now()
        now_time = now.strftime("%H:%M:%S")
        print("Start Time: ", now_time)
        input_params['r_nn'] = r_nn
        input_params['dt_nn'] = dt_nn
        print('r_nn: ', r_nn)
        print('dt_nn', dt_nn)
        data_input, data_output, input_params = runfile_function(r_nn, dt_nn)
        
        # Plot data
        data_focals = data_output.dropna(subset=['epsilon'])
        x = (data_focals['epsilon']).sort_values(ascending=True)
        y = pd.Series(range(0, len(x)))
        axs.plot(x, y + 1,
                 label=f'{r_nn}/{dt_nn}',
                 color=cmap[color_count])
        color_count = color_count + 1
            
axs.set_xlabel('Angular difference')
axs.set_ylabel('Cumulative frequency')
axs.legend()

plt.savefig(input_params['out_dir'] + '/InputParams_Sensitivity.pdf')