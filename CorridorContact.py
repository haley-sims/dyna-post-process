"""
Code to check the infill at the corridor/Unit4 interface
Note: user must be in directory where results are located
"""
def CorridorContact(thisLoc, resultsFolder):
    import os
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    fileLoc = thisLoc
    fileName = 'corridorContact.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    ContactData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
    ContactData = ContactData.values

    contactLength = 27.7*3.2808 #contact length in ft
    
    CorridorContact = resultsFolder+'/'+'JointBridgingElements'
    if not os.path.exists(CorridorContact):
        os.mkdir(CorridorContact)
    
    maxT = max(ContactData[:,1]/1000/contactLength)
    maxC = min(ContactData[:,1]/1000/contactLength)
    maxShear = max(ContactData[:,2]/1000/contactLength)
    minShear = min(ContactData[:,2]/1000/contactLength)
    
    #plot the Tension direction
    tensionCap = 34.3
    compressionCap = -490
    plt.figure()
    x = ContactData[:,0]
    y = ContactData[:,1]/1000/contactLength
    plt.plot(x,y)
    plt.title('Tension/Compression across Unit 4/Corridor Interface')
    plt.axhline(y=tensionCap, color = 'r')
    plt.axhline(y=compressionCap, color ='r')
    plt.xlabel('Time (s)')
    plt.ylabel('Force (klf)')
    name = CorridorContact + '/Unit4Corridor_Contact_TandC.png'
    plt.savefig(name, bbox_inches='tight')

    shearcap = 16.9
    plt.figure()
    x = ContactData[:,0]
    y = ContactData[:,2]/1000/contactLength
    plt.plot(x,y)
    plt.axhline(y=shearcap, color='r')
    plt.axhline(y=-shearcap, color = 'r')
    plt.title('Shear Across Unit 4/Corridor Interface')
    plt.xlabel('Time (s)')
    plt.ylabel('Force (klf)')
    name = CorridorContact+'/Unit4Corridor_Contact_Shear.png'
    plt.savefig(name, bbox_inches='tight')
    
    plt.close('all')
    print('Unit 4/Corridor Interface Complete')
    return shearcap, tensionCap, maxT, maxC, maxShear, minShear
