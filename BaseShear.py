"""
Code to check steel braces at each time step
Note: user must be in directory where results are located
"""

def BaseShear(resultsFolder, thisLoc):
    import os
    import numpy as np
    import pandas as pd
    import xlrd
    import matplotlib.pyplot as plt
    import math
    
    fileLoc = thisLoc #get directory of results, set by User
    fileName = 'baseShearX.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    BaseShearX = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
    BaseShearX = BaseShearX.values

    fileName = 'baseShearY.csv'
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    BaseShearY = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing shear forces using first row as column labels and time step as row labels
    BaseShearY = BaseShearY.values

    Weight = 3.3766*10**6/1000/4.4482216
    SlidingCap = 0.4*9.81*Weight
    num_time = BaseShearX.shape[0]
    maxX = max(BaseShearX[:,1])/1000
    minX = min(BaseShearX[:,1])/1000
    maxY = max(BaseShearY[:,1])/1000
    minY = min(BaseShearY[:,1])/1000
    
    baseShearResults = resultsFolder+'/'+'BaseShear'
    if not os.path.exists(baseShearResults):
        os.mkdir(baseShearResults)

    #plotting at each time step
    plt.figure(1)
    x = BaseShearX[:,0]
    y = BaseShearX[:,1]/1000
    plt.plot(x,y, label = 'Base Shear')
    plt.axhline(y=SlidingCap, color = 'r', label='Sliding Capacity')
    plt.axhline(y=SlidingCap*-1, color = 'r')
    plt.title("Base Shear X Direction")
    plt.xlabel("Time (s)")
    plt.ylabel("Shear (k)")
    plt.legend(loc='upper right')
    name = baseShearResults+'/'+'BaseShearX.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure(2)
    x = BaseShearY[:,0]
    y = BaseShearY[:,1]/1000
    plt.plot(x,y, label='Base Shear')
    plt.axhline(y=SlidingCap, color = 'r', label='Sliding Capacity')
    plt.axhline(y=SlidingCap*-1, color = 'r')
    plt.title("Base Shear Y Direction")
    plt.xlabel("Time (s)")
    plt.ylabel("Shear (k)")
    plt.legend(loc='upper right')
    name = baseShearResults+'/'+'BaseShearY.png'
    plt.savefig(name, bbox_inches='tight')
    
    plt.close('all')
    
    print('Base Shear Complete')
    return maxX, minX, maxY, minY, Weight, SlidingCap

