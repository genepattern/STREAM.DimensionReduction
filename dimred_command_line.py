#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings

warnings.filterwarnings('ignore')

__tool_name__='STREAM'
print('''
   _____ _______ _____  ______          __  __ 
  / ____|__   __|  __ \|  ____|   /\   |  \/  |
 | (___    | |  | |__) | |__     /  \  | \  / |
  \___ \   | |  |  _  /|  __|   / /\ \ | |\/| |
  ____) |  | |  | | \ \| |____ / ____ \| |  | |
 |_____/   |_|  |_|  \_\______/_/    \_\_|  |_|
... Dimension Reduction                                               
''',flush=True)

import stream as st
import argparse
import multiprocessing
import os
from slugify import slugify
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import sys
import ast

mpl.use('Agg')
mpl.rc('pdf', fonttype=42)

os.environ['KMP_DUPLICATE_LIB_OK']='True'


print('- STREAM Single-cell Trajectory Reconstruction And Mapping -',flush=True)
print('Version %s\n' % st.__version__,flush=True)
    

def main():
    sns.set_style('white')
    sns.set_context('poster')
    parser = argparse.ArgumentParser(description='%s Parameters' % __tool_name__ ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", "--data-file", dest="input_filename",default = None, help="input file name, pkl format from Stream preprocessing module", metavar="FILE")
    parser.add_argument("-of","--of",dest="output_filename_prefix", default="StreamiFSOutput",  help="output file name prefix")

    parser.add_argument("-nb_pct","--percent_neighbor_cells",dest="nb_pct", type=float, default=None, help="")
    parser.add_argument("-n_comp_k",dest="n_comp_k", type = int, default=None,  help="")
    parser.add_argument("-feat",dest="feature", default=None,   help="feature")

    parser.add_argument("-method",dest="method",  default=None,  help="")
    parser.add_argument("-nc_plot",dest="nc_plot", type=int, default=None,  help="")
    parser.add_argument("-comp1",dest="comp1", default=None,   help="feature")
    parser.add_argument("-comp2",dest="comp2", type=int, default=None,  help="")
    parser.add_argument("-fig_width",dest="fig_width", type=int, default=8, help="")        
    parser.add_argument("-fig_height",dest="fig_height", type=int, default=8, help="")
    parser.add_argument("-n_jobs",dest="n_jobs", type=int, default=2,  help="")
    
    parser.add_argument("-fig_legend_ncol",dest="fig_legend_ncol", type=int, default=None, help="")                                   


    args = parser.parse_args()
    print(args)
    
    print('Starting dimension reduction procedure...')

    workdir = "./"

    adata = st.read(file_name=args.input_filename, file_format='pkl', experiment='rna-seq', workdir=workdir)
    print("Feature " , args.feature, type(args.feature))
    st.dimension_reduction(adata,method=args.method, feature='var_genes', nb_pct=args.nb_pct,n_components=args.n_comp_k, n_jobs=args.n_jobs ,eigen_solver=None)

    fig_size=(args.fig_width, args.fig_height)
    st.plot_dimension_reduction(adata, n_components=args.nc_plot, comp1=args.comp1, comp2=args.comp2, save_fig=True, 
                            fig_name=(args.output_filename_prefix + '_stddev_dotplot.png'),
                            fig_path="./",fig_size=fig_size,fig_legend_ncol=args.fig_legend_ncol)


    st.write(adata,file_name=(args.output_filename_prefix + '_stream_result.pkl'),file_path='./',file_format='pkl') 
    print('Output: '+ str(adata.obs.shape[0]) + ' cells, ' + str(adata.var.shape[0]) + ' genes')

    print('Finished computation.')

if __name__ == "__main__":
    main()
