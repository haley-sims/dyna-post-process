"""
Code to check theUnit 4/Unit 5 interface
Note: user must be in directory where results are located
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fileLoc = os.getcwd() #get directory of results, set by User
fileName = 'unit4Unit5X.csv' #name of the csv results to be read in
filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
Xdata = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
Xdata = Xdata.values

fileLoc = os.getcwd() #get directory of results, set by User
fileName = 'unit4Unit5Y.csv' #name of the csv results to be read in
filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
Ydata = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
Ydata = Ydata.values

#initialize array for element responses at each time step
num_time = Xdata.shape[0]
num_responses = 3 #time, X force, Y force
interfaceLength = 20.4*3.2808 #Length in ft

Unit4Unit5Results = np.zeros((num_time,num_responses))
Unit4Unit5Results[:,0] = Xdata[:,0]
Unit4Unit5Results[:,1] = Xdata[:,3]/(1000*interfaceLength)
Unit4Unit5Results[:,2] = Ydata[:,3]/(1000*interfaceLength)

if not os.path.exists('Unit4Unit5Interface'):
    os.mkdir('Unit4Unit5Interface')
shearCap = 17.1
tensionCap = 19.3

plt.figure(1)
x = Unit4Unit5Results[:,0]
y = Unit4Unit5Results[:,1]
plt.title("Shear Force at Unit 4/Unit 5 Interface X Direction")
plt.xlabel("Time Step (s)")
plt.ylabel("Shear Force (klf)")
plt.plot(x,y)
plt.axhline(y=shearCap, color = 'r')
plt.axhline(y=-shearCap, color = 'r')
plt.savefig('Unit4Unit5Interface/Unit4Unit5_Shear.png', bbox_inches = 'tight')

plt.figure(2)
x = Unit4Unit5Results[:,0]
y = Unit4Unit5Results[:,2]
plt.plot(x,y)
plt.title("Tension/Compression Force at Unit 4/Unit 5 Interface Y Direction")
plt.axhline(y=tensionCap, color ='r')
plt.xlabel("Time Step (s)")
plt.ylabel("Shear Force (klf)")
plt.savefig('Unit4Unit5Interface/Unit4Unit5_Tension.png')
