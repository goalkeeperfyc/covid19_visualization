# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:37:13 2020

@author: Yucheng Fang
"""


import numpy as np
import pandas as pd


raw_data = pd.read_csv("covid_19_clean_complete.csv")

# confirmed, deaths recovered all equal to zero
zeros_subset = raw_data.loc[np.logical_and(np.logical_and(
    raw_data["Confirmed"] == 0, raw_data["Deaths"] == 0), 
    raw_data["Recovered"] == 0), ]

# unique country
unique_country = raw_data["Country/Region"].unique()


# total 