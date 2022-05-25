#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:39:44 2022

@author: kgraham
"""

# Python packages to import (via Anaconda environment)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# MatchUpData
mud = pd.read_csv('/Users/kgraham/matchupdata.csv')      # batterID, pitcherID, outcome

# initialize "empty" dataframe for output
out = pd.DataFrame(np.nan, index=range(0,100), columns=['batterID','outcome_next'] )

# loop through all batterID numbers 1..100
# model is fit to each individual batter
# 300 random pitchers scenarios are drawn for each individual batter
for i in range(1,101):
    # selects mud with batterID
    batterdf = mud[ mud.batterID==i ]

    # defines model used for fit and prediction       
    bt = linear_model.BayesianRidge()      

    # fits model, series defined as numpy arrays with reshaping 
    bt.fit(np.array(batterdf.pitcherID).reshape(-1,1), np.array(batterdf.outcome).reshape(-1,1))
    
    # define random pitcher matchups 300x using numpy random integer function    
    random_pitchers = np.random.randint(low=101, high=200, size=300).reshape(-1,1)
    
    # predict single batter outcome against random_pitchers using model fit
    predict = bt.predict(random_pitchers)
    
    # take mean of predicted outcomes for a single batter
    mean = predict.mean() 
    
    # writing batterID to out dataframe
    out.batterID[i-1:i] = i
    
    # input mean outcome to out
    out.outcome_next[i-1:i] = mean

# write populated dataframe to file
out.to_csv('/Users/kgraham/next_season_projections.csv')



# ------------------------------------------- #
# figure for data exploration
def hist():     # histogram of previous season outcomes
    mean = mud.outcome.mean()
    plt.hist(mud.outcome, bins=30, density=True, color='navy')
    plt.axvline(mean, color='lightgray', linestyle='dashed', linewidth=1)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Outcomes', fontsize=14)
    plt.ylabel('Probability Density', fontsize=14)
    plt.title('Histogram of all past outcomes', fontsize=14)