"""
Code to check brace connections
Note: user must be in directory where results are located
"""

import numpy as np
import pandas as pd
import os
import xlrd
import matplotlib.pyplot as plt

fileLoc = os.getcwd() #get directory of results, set by User
fileName = 'unit5IDR.csv' #name of the csv results to be read in
filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
IDRUnit5 = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
IDRUnit5 = IDRUnit5.values

fileName = 'unit4IDR.csv'
filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
IDRUnit4 = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing shear forces using first row as column labels and time step as row labels
IDRUnit4 = IDRUnit4.values
#
fileName = 'corridorIDR.csv'
filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
IDRCorridor = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing shear forces using first row as column labels and time step as row labels
IDRCorridor = IDRCorridor.values

num_time = IDRUnit5.shape[0]
