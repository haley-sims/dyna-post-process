"""
Code to check the curb at the corridor
Note: user must be in directory where results are located
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fileLoc = os.getcwd() #get directory of results, set by User
fileName = 'corridorCurbX.csv' #name of the csv results to be read in
filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
AxialData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
AxialData = AxialData.values

fileLoc = os.getcwd() #get directory of results, set by User
fileName = 'corridorCurbY.csv' #name of the csv results to be read in
filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
ShearYData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
ShearYData = ShearYData.values

fileLoc = os.getcwd() #get directory of results, set by User
fileName = 'corridorCurbZ.csv' #name of the csv results to be read in
filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
ShearZData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
ShearZData = ShearZData.values

fileLoc = os.getcwd() #get directory of results, set by User
fileName = 'corridorCurbMoments.csv' #name of the csv results to be read in
filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
MomentData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
MomentData = MomentData.values

fileName = 'CorridorCurbNvsM.txt'
fileLoc = fileLoc = r'J:\S-F\230000\238558-00\4 Internal Project Data\4-04 Calculations\Struct\97 - LsDyna'
filein = os.path.join(fileLoc, fileName)
PMData = open(filein,'r')
PMData = PMData.read().split('\n')
Tr = float(PMData[6].split('\t')[1])
PMData = PMData[7:]

#initialize variables
PMCurve = []
P=[]
M=[]
flag = 0

for line in PMData:
    if '# Points' in line:
        angle = int(line.split('\t')[3])
        flag = -2
    else:
        flag = flag + 1
    if flag == 0:
        PMCurve.append('Theta ' + str(angle)+'\t '+'Theta '+str(angle)+'\t'+'Theta '+str(angle)+'\t'+'Theta '+str(angle)+'\t'+'Theta '+str(angle)+'\t'+'Theta '+str(angle)+'\t')
    elif flag < 0:
        continue
    else:
        PMCurve.append(line)

while '' in PMCurve:
    PMCurve.remove('')
while ' ' in PMCurve:
    PMCurve.remove(' ')

for line in PMCurve:
    data = line.split('\t')
    P.append(data[2])
    M.append(data[3])

#create lists for the moment curvature at 0 degrees rotation
P0 = P[1:100:1]
P0 = list(map(float, P0))
M0 = M[1:100:1]
M0 = list(map(float,M0))
P0.insert(0,Tr)
M0.insert(0,0)
P0.extend(P0[::-1])
M0rev = [-x for x in M0]
M0.extend(M0rev[::-1])

# create lists for moment curvature at 90 degrees of rotation
P90 = P[102:199:1]
P90 = list(map(float,P90))
M90 = M[102:199:1]
M90 = list(map(float,M90))
P90.insert(0,Tr)
M90.insert(0,0)
P90.extend(P90[::-1])
M90rev = [-x for x in M90]
M90.extend(M90rev[::-1])

num_responses =  4 #time step, Axial force, Myy, Mzz
num_time = AxialData.shape[0]
num_el = AxialData.shape[1]

#initialize array for element responses at each time step
CorridorCurbResults = np.zeros((num_time,num_responses))
CorridorCurbResults[:,0] = AxialData[:,0]
CorridorCurbResults[:,1] = AxialData[:,1]/1000
CorridorCurbResults[:,2] = MomentData[:,1]/1000
CorridorCurbResults[:,3] = MomentData[:,2]/1000

plt.figure(1)
y = CorridorCurbResults[:,1]
x = CorridorCurbResults[:,3]
plt.scatter(x,y)
x = M90
y = P90
plt.plot(x,y)
plt.title("P-M Elastic Column Strong Axis")
plt.xlabel("Moment (k-ft)")
plt.ylabel("Axial Force (k)")

plt.figure(2)
y = CorridorCurbResults[:,1]
x = CorridorCurbResults[:,2]
plt.scatter(x,y)
x = M0
y = P0
plt.plot(x,y)
plt.title("P-M Elastic Column Weak Axis")
plt.xlabel("Moment (k-ft)")
plt.ylabel("Axial Force (k)")
plt.show()
