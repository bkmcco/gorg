from pylab import *
import pandas as pd
import numpy as np
import scipy.stats as st
import os
'''This note intakes SCP data in the form of a .txt and plots it in Python. Default overlays plots from two different .txt files.'''

engine = 'python"   #prevents warning from throwing, no other effect

f1 = pd.read_csv("2024_07_10_3200_400_10_0.9_6.txt",  usecols=[0],names=['colA'],skiprows = 13, skipfooter=16, header=N>
f2 = pd.read_csv("2024_07_10_3100_400_10_0.9_6.txt",  usecols=[0],names=['colA'],skiprows = 13, skipfooter=16, header=N>

#f_ = pd.read_csv("file_name", usecols=[0] , names=['colA'], skiprows=13 , skipfooter=16, header=None)
#more info at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

col1 = f1.colA.values
col2 = f2.colA.values

#col_ = f_.colA.values

plot(col2,color='r',label='3100, 0.9',alpha=0.5)
plot(col1,color='b',label='3200, 0.9',alpha=0.5)

legend(loc='best')
grid('on')
xlabel('|max amplitude| [ADC]')
ylabel('counts')
yscale('log')
title('Coarse Gain: 10')
xlim(0,7000)
show()
