#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 12:15:55 2022

@author: kgraham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read in projections and previous season outcomes
out = pd.read_csv('/Users/kgraham/github_build/next_season_projections.csv')
mud = pd.read_csv('/Users/kgraham/github_build/to_submit/given/matchupdata.csv')

# initialize dataframe
df = pd.DataFrame( index=range(1,101), columns=['batterID', 'previous', 'projection'] )

# take mean of previous season outcomes & load projections into one dataframe
for i in range(0,101):
    prev_mean = mud.outcome[mud.batterID == i+1].mean()
    df.batterID[i:i+1] = i+1
    df.previous[i:i+1] = prev_mean
    df.projection[i:i+1] = out.outcome_next[out.batterID == i+1]
    
# call linplot function to draw plot of previous versus projected outcomes
def linplot():
    # establish x and y data
    x = df.previous
    y = df.projection
    
    # build figure
    plt.figure( figsize=(8,6) )
    
    # 1 to 1 line, quickly done
    plt.plot( [-45, 58], [-45, 58], linestyle='--', color='gray', alpha=0.5, label='y = x')
    
    # scatterplot of datapoints, x vs. y
    plt.scatter(x, y, color='navy', edgecolors='lightblue', label='comparison')
    
    # include other data, absolute differnce mean
    mean_diff = np.round( np.abs( x-y ).mean() , decimals=3)
    plt.text( 20,-35, 'Absolute Difference: {}'.format(mean_diff), fontsize=12,
        bbox={'facecolor': 'gray', 'alpha': 0.15, 'pad': 8} )
    
    # labels
    plt.title('Previous versus Projected Outcomes', size=16)
    plt.xlabel('Previous', size=14)
    plt.ylabel('Projected', size=14)
    # formatting
    plt.tick_params(axis='x', which='major', labelsize=14)
    plt.tick_params(axis='y', which='major', labelsize=14)
    plt.legend()
    
