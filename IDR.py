"""
Code to check interstory drift of building
Note: user must be in directory where results are located
"""
def IDR(thisLoc, resultsFolder):

    import numpy as np
    import pandas as pd
    import os
    import matplotlib.pyplot as plt

    fileLoc = thisLoc #get directory of results, set by User
    fileName = 'unit5IDR.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    IDRUnit5 = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
    IDRUnit5 = IDRUnit5.values

    fileName = 'unit4IDR.csv'
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    IDRUnit4 = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing shear forces using first row as column labels and time step as row labels
    IDRUnit4 = IDRUnit4.values

    fileName = 'corridorIDR.csv'
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    IDRCorridor = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing shear forces using first row as column labels and time step as row labels
    IDRCorridor = IDRCorridor.values

    num_time = IDRUnit5.shape[0]

    # IDRUnit5B = IDRUnit5[:,1:4:1]
    # IDRUnit5D = IDRUnit5[:,5:8:1]
    # IDRUnit5A = IDRUnit5[:,9:12:1]
    # IDRUnit5C = IDRUnit5[:,13:16:1]

    # IDRUnit4F = IDRUnit4[:, 1:2:1]
    # IDRUnit4E1 = IDRUnit4[:, 3:4:1]
    # IDRUnit4E2 = IDRUnit4[:, 5:6:1]
    # IDRUnit4G = IDRUnit4[:, 7:8:1]
    # IDRUnit4H = IDRUnit4[:, 9:10:1]

    IDR = resultsFolder + '/' + 'IDR'
    if not os.path.exists(IDR):
        os.mkdir(IDR)

    #maxes and mins
    maxIDRA = []
    maxIDRB = []
    maxIDRC = []
    maxIDRD = []
    minIDRA = []
    minIDRB = []
    minIDRC = []
    minIDRD = []

    maxIDRBRoof = [max(IDRUnit5[:,1]), max(IDRUnit5[:,2])]
    minIDRBRoof = [min(IDRUnit5[:, 1]), min(IDRUnit5[:,2])]
    maxIDRBL2 = [max(IDRUnit5[:,3]), max(IDRUnit5[:,4])]
    minIDRBL2 = [min(IDRUnit5[:, 3]), min(IDRUnit5[:,4])]
    maxIDRDRoof = [max(IDRUnit5[:, 5]), max(IDRUnit5[:,6])]
    minIDRDRoof = [min(IDRUnit5[:, 5]), min(IDRUnit5[:,6])]
    maxIDRDL2 = [max(IDRUnit5[:,7]), max(IDRUnit5[:, 8])]
    minIDRDL2 = [min(IDRUnit5[:,7]), min(IDRUnit5[:, 8])]
    maxIDRARoof = [max(IDRUnit5[:,9]), max(IDRUnit5[:,10])]
    minIDRARoof = [min(IDRUnit5[:,9]), min(IDRUnit5[:,10])]
    maxIDRAL2 = [max(IDRUnit5[:, 11]), max(IDRUnit5[:,12])]
    minIDRAL2 = [min(IDRUnit5[:, 11]), min(IDRUnit5[:, 12])]


    # plotting
    plt.figure()
    x = IDRUnit5[:,0]
    y = IDRUnit5[:, 1]
    y2 = IDRUnit5[:,5]
    y3 = IDRUnit5[:,9]
    y4 = IDRUnit5[:,13]
    plt.plot(x,y,x,y2, x, y3, x, y4)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Unit 5 X Direction Roof')
    plt.legend(('Point B', 'Point D', 'Point A', 'Point C'), loc='upper right')
    name = IDR + '/' + 'IDR_Unit5_RoofX.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    x = IDRUnit5[:,0]
    y = IDRUnit5[:, 3]
    y2 = IDRUnit5[:,7]
    y3 = IDRUnit5[:,11]
    y4 = IDRUnit5[:,15]
    plt.plot(x,y,x,y2, x, y3, x, y4)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Unit 5 X Direction Level 2')
    plt.legend(('Point B', 'Point D', 'Point A', 'Point C'), loc='upper right')
    name = IDR + '/' + 'IDR_Unit5_L2X.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    x = IDRUnit5[:,0]
    y = IDRUnit5[:, 2]
    y2 = IDRUnit5[:,6]
    y3 = IDRUnit5[:,10]
    y4 = IDRUnit5[:,14]
    plt.plot(x,y,x,y2, x, y3, x, y4)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Unit 5 Y Direction Roof')
    plt.legend(('Point B', 'Point D', 'Point A', 'Point C'), loc='upper right')
    name = IDR + '/' + 'IDR_Unit5_roofY.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    x = IDRUnit5[:,0]
    y = IDRUnit5[:, 4]
    y2 = IDRUnit5[:,8]
    y3 = IDRUnit5[:,12]
    y4 = IDRUnit5[:,16]
    plt.plot(x,y,x,y2, x, y3, x, y4)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Unit 5 Y Direction Level 2')
    plt.legend(('Point B', 'Point D', 'Point A', 'Point C'), loc='upper right')
    plt.savefig('IDR/IDR_Unit5_L2Y.png', bbox_inches='tight')

    plt.figure()
    x = IDRUnit4[:,0]
    y = IDRUnit4[:, 1]
    y2 = IDRUnit4[:,3]
    y3 = IDRUnit4[:,5]
    y4 = IDRUnit4[:,7]
    y5 = IDRUnit4[:,9]
    plt.plot(x,y,x,y2, x, y3, x, y4, x, y5)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Unit 4 X Direction Level 2')
    plt.legend(('Point F', 'Point E1', 'Point E2', 'Point G', 'Point H'), loc='upper right')
    name = IDR + '/' + 'IDR_Unit4X.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    x = IDRUnit4[:,0]
    y = IDRUnit4[:, 2]
    y2 = IDRUnit4[:,4]
    y3 = IDRUnit4[:,6]
    y4 = IDRUnit4[:,8]
    y5 = IDRUnit4[:,10]
    plt.plot(x,y,x,y2, x, y3, x, y4, x, y5)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Unit 4 Y Direction Level 2')
    plt.legend(('Point F', 'Point E1', 'Point E2', 'Point G', 'Point H'), loc='upper right')
    name = IDR + '/' + 'IDR_Unit4Y.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    x = IDRCorridor[:,0]
    y = IDRCorridor[:, 5]
    y2 = IDRCorridor[:,6]
    y3 = IDRCorridor[:,8]
    y4 = IDRCorridor[:,7]
    plt.plot(x,y,x,y2, x, y3, x, y4)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Corridor X Direction Roof')
    plt.legend(('Point J', 'Point L', 'Point K', 'Point I'), loc='upper right')
    name = IDR + '/' + 'IDR_Corridor_RoofX.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    x = IDRCorridor[:,0]
    y = IDRCorridor[:, 13]
    y2 = IDRCorridor[:,14]
    y3 = IDRCorridor[:,16]
    y4 = IDRCorridor[:,15]
    plt.plot(x,y,x,y2, x, y3, x, y4)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Corridor Y Direction Roof')
    plt.legend(('Point J', 'Point L', 'Point K', 'Point I'), loc='upper right')
    name = IDR + '/' + 'IDR_CorridorRoofY.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    x = IDRCorridor[:,0]
    y = IDRCorridor[:, 1]
    y2 = IDRCorridor[:,2]
    y3 = IDRCorridor[:,4]
    y4 = IDRCorridor[:,3]
    plt.plot(x,y,x,y2, x, y3, x, y4)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Corridor X Direction Level 2')
    plt.legend(('Point J', 'Point L', 'Point K', 'Point I'), loc='upper right')
    name = IDR + '/' + 'IDR_Corridor_L2X.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    x = IDRCorridor[:,0]
    y = IDRCorridor[:, 9]
    y2 = IDRCorridor[:,10]
    y3 = IDRCorridor[:,12]
    y4 = IDRCorridor[:,11]
    plt.plot(x,y,x,y2, x, y3, x, y4)
    plt.xlabel('Time (s)')
    plt.ylabel('Drift Ratio')
    plt.title('Interstory Drift Corridor Y Direction Level 2')
    plt.legend(('Point J', 'Point L', 'Point K', 'Point I'), loc='upper right')
    name = IDR + '/' + 'IDR_Corridor_L2Y.png'
    plt.savefig(name, bbox_inches='tight')
    plt.close('all')

    return maxIDRBRoof, minIDRBRoof, maxIDRBL2, minIDRBL2, maxIDRDRoof, minIDRDRoof, maxIDRDL2, minIDRDL2, maxIDRARoof, minIDRARoof, maxIDRAL2, minIDRAL2,
