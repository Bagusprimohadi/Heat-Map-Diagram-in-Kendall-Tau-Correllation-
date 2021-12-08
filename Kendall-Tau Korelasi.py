# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:13:02 2021

@author: acer
"""

import pandas as pd
from pylab import rcParams
import seaborn as sb
from scipy.stats.stats import kendalltau
import matplotlib.pyplot as plt

# Import the data
data = pd.read_excel('D:\DATA_G_LAINNYA\Data_Python\Project\P9-DataICMR-KendalTau\CH.xlsx')
data.head()

corr = data.corr(method='kendall')

rcParams['figure.figsize'] = 14.7,8.27
sb.heatmap(corr, 
           xticklabels=corr.columns.values, 
           yticklabels=corr.columns.values, 
           cmap="YlGnBu",
          annot=True)
plt.title('Heat Map Diagram of Kendall-Tau Correlation', loc='center', 
          fontsize=25, pad=30, color='black')

