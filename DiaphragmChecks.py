"""
Code to check the curb at the corridor
Note: user must be in directory where results are located
"""
def DiaphragmChecks(thisLoc, resultsFolder):

    import os
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    #import all data and read into arrays for each diaphragm, each location, each direction
    
    fileLoc = thisLoc
    fileName = 'unit5RoofDiaphX.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    Unit5RoofX = pd.read_csv(filein, skiprows=[0,1,2]) #grabbing axial forces using first row as column labels and time step as row labels
    Unit5RoofX = Unit5RoofX.values

    fileName = 'unit5L2DiaphX.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    Unit5L2X = pd.read_csv(filein, skiprows=[0,1,2]) #grabbing axial forces using first row as column labels and time step as row labels
    Unit5L2X = Unit5L2X.values

    fileName = 'unit5RoofDiaphY.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    Unit5RoofY = pd.read_csv(filein, skiprows=[0,1,2]) #grabbing axial forces using first row as column labels and time step as row labels
    Unit5RoofY = Unit5RoofY.values

    fileName = 'unit5L2DiaphY.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    Unit5L2Y = pd.read_csv(filein, skiprows=[0,1,2]) #grabbing axial forces using first row as column labels and time step as row labels
    Unit5L2Y = Unit5L2Y.values

    fileName = 'unit4DiaphX.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    Unit4DiaphX = pd.read_csv(filein, skiprows=[0,1,2]) #grabbing axial forces using first row as column labels and time step as row labels
    Unit4DiaphX = Unit4DiaphX.values

    fileName = 'unit4DiaphY.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    Unit4DiaphY = pd.read_csv(filein, skiprows=[0,1,2]) #grabbing axial forces using first row as column labels and time step as row labels
    Unit4DiaphY = Unit4DiaphY.values

    fileName = 'corrRoofDiaphX.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    CorridorRoofX = pd.read_csv(filein, skiprows=[0,1,2]) #grabbing axial forces using first row as column labels and time step as row labels
    CorridorRoofX = CorridorRoofX.values

    fileName = 'corrL2DiaphX.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    CorridorL2X = pd.read_csv(filein, skiprows=[0,1,2]) #grabbing axial forces using first row as column labels and time step as row labels
    CorridorL2X = CorridorL2X.values

    fileName = 'corridorDiaphY.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    CorridorDiaphY = pd.read_csv(filein, skiprows=[0,1,2]) #grabbing axial forces using first row as column labels and time step as row labels
    CorridorDiaphY = CorridorDiaphY.values

    num_time = CorridorDiaphY.shape[0]

    num_el = 12 #Unit 5 Roof X, Unit 5 Roof Y, Unit 5 L2 X, Unit 5 L2 Y, Unit 4 Roof X, Unit 4 Roof Y, Corridor Roof 1 X, Corridor Roof 1 Y,
    #Corridor Roof 2 X, Corridor Roof 2 Y, Corridor L2 X, Corridor L2 Y
    num_responses = 8 #time, max number of section cuts from all areas
    sectionLengths = [25.04*3.2808, 26.98*3.2808, 40.106*3.2808, 19.86*3.2808, 20.47*3.2808,
                    11.32*3.2808, 22.352*3.2808, 27.7*3.2808, 2.667*3.2808, 14*3.2808,47.5*3.2808] #Unit 5 Roof X normal, Unit 5 X at added length,
                                                                                            # Unit 5 roof Y, Unit 5 Roof at small geometry Y, Unit 4 Roof X normal,
                                                                                            # Unit 4 Roof X at north end,Unit 4 Roof west side, Unit 4 roof east side, 
                                                                                            #corridor X, Corridor Y
    DiaphragmResults = np.zeros((num_time,num_responses, num_el))
    for i in range(0,num_el):
        DiaphragmResults[:,0,i] = Unit5RoofX[:,0] # make first column time step

    #organize data for Unit 5 Roof Diaphragm X Direction
    for j in range(1,num_responses):
        if j == 1 or j ==7:
            DiaphragmResults[:,j,0] = Unit5RoofX[:,j]/1000/sectionLengths[0]
        else:
            DiaphragmResults[:,j,0] = Unit5RoofX[:,j]/1000/sectionLengths[1]

    #organize data for Unit 5 Roof Diaphragm Y Direction
    for j in range(1,num_responses):
        if j == 1:
            DiaphragmResults[:,j,1] = Unit5RoofY[:,j]/1000/sectionLengths[3]
        else:
            DiaphragmResults[:,j,1] = Unit5RoofY[:,j]/1000/sectionLengths[2]

    #organize data for Unit 5 L2 Diaphragm X Direction
    for j in range(1,num_responses-1):
        if j == 1 or j == 6:
            DiaphragmResults[:,j,2] = Unit5L2X[:,j]/1000/sectionLengths[0]
        else:
            DiaphragmResults[:,j,2] = Unit5L2X[:,j]/1000/sectionLengths[1]

    #organize data for Unit 5 L2 Diaphragm Y Direction
    for j in range(1,num_responses-1):
        if j == 1:
            DiaphragmResults[:,j,3] = Unit5L2Y[:,j]/1000/sectionLengths[3]
        else:
            DiaphragmResults[:,j,3] = Unit5L2Y[:,j]/1000/sectionLengths[2]

    #organize data for Unit 4 Roof Diaphragm X Direction
    for j in range(1,num_responses-2):
        if j == 5:
            DiaphragmResults[:,j,4] = Unit4DiaphX[:,j]/1000/sectionLengths[5]
        else:
            DiaphragmResults[:,j,4] = Unit4DiaphX[:,j]/1000/sectionLengths[4]

    #organize data for Unit 4 Diaphragm Y Direction
    for j in range(1,num_responses):
        if j == 1 or j == 2 or j == 3:
            DiaphragmResults[:,j,5] = Unit4DiaphY[:,j]/1000/sectionLengths[6]
        else:
            DiaphragmResults[:,j,5] = Unit4DiaphY[:,j]/1000/sectionLengths[7]
            
    #organize data for Corridor Upper Roof Diaphragm X Directions
    for j in range(1,num_responses-2):
            DiaphragmResults[:,j,6] = CorridorRoofX[:,j+1]/1000/sectionLengths[8]
    
    #organize data for Corridor Upper Roof Diaphragm Y Direction
    for j in range(1,num_responses-5):
            DiaphragmResults[:,j,7] = CorridorDiaphY[:,j]/1000/sectionLengths[10]

    #organize data for Corridor Lower Roof Diaphragm X Direction
    for j in range(1,num_responses-5):
        if j ==1:
            DiaphragmResults[:,j,8] = CorridorRoofX[:,j]/1000/sectionLengths[8]
        else:
            DiaphragmResults[:,j,8] = CorridorRoofX[:,7]/1000/sectionLengths[8]

    #organize data for Corridor Lower Roof Diaphragm Y Direction
    for j in range(1,num_responses-5):
            DiaphragmResults[:,j,9] = CorridorDiaphY[:,j+4]/1000/sectionLengths[9]
            
    #organize data for Corridor Level 2 Diaphragm X Direction
    for j in range(1,num_responses-2):
            DiaphragmResults[:,j,10] = CorridorL2X[:,j]/1000/sectionLengths[8]

    #organize data for Corridor Level 2 Diaphragm Y Direction
    for j in range(1,num_responses-5):
            DiaphragmResults[:,j,11] = CorridorDiaphY[:,j+2]/1000/sectionLengths[10]

    names = ['Unit 5 Roof Diaphragm X', 'Unit 5 Roof Diaphragm Y', 'Unit 5 L2 Diaphragm X', 'Unit 5 L2 Diaphragm Y',
            'Unit 4 Roof Diaphragm X', 'Unit 4 Roof Diaphragm Y', 'Corridor Upper Roof Diaphragm X', 'Corridor Upper Roof Diaphragm Y', 
            'Corridor Lower Roof Diaphragm X', 'Corridor Lower Roof Diaphragm Y','Corridor Level 2 Diaphragm X', 'Corridor Level 2 Diaphragm Y']

    Unit5RXCap = [12, 7, 7, 7, 7, 12,12]
    Unit5RYCap = [11.7, 11.7, 11.7, 11.7, 11.7, 11.7, 11.7]
    Unit5L2XCap = [11.4,11.4,11.4,11.4,11.4,15.8]
    Unit5L2YCap = [12.1,12.1,7.7,9.5,10.1,10.1]
    Unit4L2XCap = [9.3,10.3,10.3,10.3,6.1]
    Unit4L2YCap = [6.1,6.1,6.1,10.9,10.9,10.9,10.5]
    CorrLowRoofXCap = [24.8, 24.8]
    CorrHighRoofXCap = [24.8, 24.8, 24.8, 24.8, 24.8]
    CorrL2XCap = [24.8, 24.8, 24.8, 24.8, 24.8]
    CorrLowRoofYCap = [13.1, 13.1]
    CorrHighRoofYCap = [13.1, 13.1]
    CorrL2YCap = [13.1, 13.1]

    Capacities = np.array((Unit5RXCap, Unit5RYCap, Unit5L2XCap, Unit5L2YCap, Unit4L2XCap, Unit4L2YCap, CorrHighRoofXCap, CorrHighRoofYCap, CorrLowRoofXCap, CorrLowRoofYCap, CorrL2XCap, CorrL2YCap))
    
    DiaphragmChecks = resultsFolder+'/'+'DiaphragmChecks'
    if not os.path.exists(DiaphragmChecks):
        os.mkdir(DiaphragmChecks)

    #plotting`
    figsize = (10, 8)
    for j in range(0,len(names)):
        print(names[j])
        if DiaphragmResults[0,4,j] == 0:
            cols = 2
            rows = 1
            fig1, axs = plt.subplots(rows,cols, figsize=figsize, constrained_layout=True)
            count = 1
            for i in range(0, cols):
                axs[i].set_title('Section '+str(count))
                axs[i].set_ylabel('Force (klf)')
                axs[i].set_xlabel('Time (s)')
                y = DiaphragmResults[:,count,j]
                x = DiaphragmResults[:,0,j]
                axs[i].axhline(y = Capacities[j][count-1], color ='r', label='Diaphragm Capacity')
                axs[i].axhline(y = Capacities[j][count-1]*-1, color ='r', label='Diaphragm Capacity')
                axs[i].plot(x,y)
                count += 1
        elif DiaphragmResults[0,6,j] == 0:
            cols = 3
            rows = 2
            fig1, axs = plt.subplots(rows, cols, figsize=figsize, constrained_layout=True)
            fig1.delaxes(axs[1,2])
            count = 1
            for i in range(0,rows):
                for k in range(0,cols):
                    axs[i,k].set_title('Section '+str(count))
                    axs[i,k].set_ylabel('Force (klf)')
                    axs[i,k].set_xlabel('Time (s)')
                    y = DiaphragmResults[:,count,j]
                    x = DiaphragmResults[:,0,j]
                    axs[i,k].plot(x,y)
                    if count < 6:
                        axs[i,k].axhline(y = Capacities[j][count-1], color ='r', label='Diaphragm Capacity')
                        axs[i,k].axhline(y = Capacities[j][count-1]*-1, color ='r', label='Diaphragm Capacity')
                    count += 1
        elif DiaphragmResults[0,7,j] == 0:
            cols = 3
            rows = 2
            fig1, axs = plt.subplots(rows, cols, figsize=figsize, constrained_layout=True)
            count = 1
            for i in range(0,rows):
                for k in range(0,cols):
                    axs[i,k].set_title('Section '+str(count))
                    axs[i,k].set_ylabel('Force (klf)')
                    axs[i,k].set_xlabel('Time (s)')
                    y = DiaphragmResults[:,count,j]
                    x = DiaphragmResults[:,0,j]
                    axs[i,k].axhline(y = Capacities[j][count-1], color ='r', label='Diaphragm Capacity')
                    axs[i,k].axhline(y = Capacities[j][count-1]*-1, color ='r', label='Diaphragm Capacity')
                    axs[i,k].plot(x,y)
                    count += 1
        else:
            cols = 4
            rows = 2
            fig1, axs = plt.subplots(rows, cols, figsize=figsize, constrained_layout=True)
            count = 1
            for i in range(0,rows):
                for k in range(0,cols):
                    if count < 8:
                        axs[i,k].set_title('Section '+str(count))
                        axs[i,k].set_ylabel('Force (klf)')
                        axs[i,k].set_xlabel('Time (s)')
                        y = DiaphragmResults[:,count,j]
                        x = DiaphragmResults[:,0,j]
                        axs[i,k].axhline(y = Capacities[j][count-1], color ='r', label='Diaphragm Capacity')
                        axs[i,k].axhline(y = Capacities[j][count-1]*-1, color ='r', label='Diaphragm Capacity')
                        axs[i,k].plot(x,y)
                        count += 1
                    else:
                        fig1.delaxes(axs[1,3])
                        continue
        fig1.suptitle(names[j])
        name = DiaphragmChecks +'/'+ str(names[j]+'.png')
        fig1.savefig(name, bbox_inches='tight')
        
    plt.close('all')
    
    #initiate all min/max lists
    Unit5RoofXMax = []
    Unit5RoofXMin = []
    Unit5RoofYMax = []
    Unit5RoofYMin = []
    Unit5RoofXMin = []
    Unit5L2XMax = []
    Unit5L2XMin = []
    Unit5L2YMax = []
    Unit5L2YMin = []
    Unit4L2XMax =[]
    Unit4L2XMin =[]
    Unit4L2YMax = []
    Unit4L2YMin = []
    CorridorRoofXMax = []
    CorridorRoofXMin = []
    CorridorRoofYMax =[]
    CorridorRoofYMin = []
    CorridorL2XMax = []
    CorridorL2XMin = []
    CorridorL2YMax = []
    CorridorL2YMin = []
    CorridorLowRoofXMax = []
    CorridorLowRoofXMin = []
    CorridorLowRoofYMax = []
    CorridorLowRoofYMin = []
    
    #compute mins and maxes
    for i in range(1, num_responses):
        Unit5RoofXMax.append(max(DiaphragmResults[:,i,0]))
        Unit5RoofXMin.append(min(DiaphragmResults[:,i,0]))
        Unit5RoofYMax.append(max(DiaphragmResults[:,i,1]))
        Unit5RoofYMin.append(min(DiaphragmResults[:,i,1]))
        Unit5L2XMax.append(max(DiaphragmResults[:,i,2]))
        Unit5L2XMin.append(min(DiaphragmResults[:,i,2]))
        Unit5L2YMax.append(max(DiaphragmResults[:,i,3]))
        Unit5L2YMin.append(min(DiaphragmResults[:,i,3]))
        Unit4L2XMax.append(max(DiaphragmResults[:,i,4]))
        Unit4L2XMin.append(min(DiaphragmResults[:,i,4]))
        Unit4L2YMax.append(max(DiaphragmResults[:,i,5]))
        Unit4L2YMin.append(min(DiaphragmResults[:,i,5]))
        CorridorLowRoofXMax.append(max(DiaphragmResults[:,i,6]))
        CorridorLowRoofXMin.append(min(DiaphragmResults[:,i,6]))
        CorridorLowRoofYMax.append(max(DiaphragmResults[:,i,9]))
        CorridorLowRoofYMin.append(min(DiaphragmResults[:,i,9]))
        CorridorRoofXMax.append(max(DiaphragmResults[:,i,7]))
        CorridorRoofXMin.append(min(DiaphragmResults[:,i,7]))
        CorridorRoofYMax.append(max(DiaphragmResults[:,i,10]))
        CorridorRoofYMin.append(min(DiaphragmResults[:,i,10]))
        CorridorL2XMax.append(max(DiaphragmResults[:,i,8]))
        CorridorL2XMin.append(min(DiaphragmResults[:,i,8]))
        CorridorL2YMax.append(max(DiaphragmResults[:,i,11]))
        CorridorL2YMin.append(min(DiaphragmResults[:,i,11]))
    print("Diaphragms Complete")
    return Capacities, Unit5RoofXMax, Unit5RoofXMin, Unit5RoofYMax, Unit5RoofYMin, Unit5L2XMax, Unit5L2XMin, Unit5L2YMax, Unit5L2YMin, Unit4L2XMax, Unit4L2XMin, Unit4L2YMax, Unit4L2YMin, CorridorLowRoofXMax, CorridorLowRoofXMin, CorridorLowRoofYMax, CorridorLowRoofYMin,CorridorRoofXMax, CorridorRoofXMin, CorridorRoofYMax, CorridorRoofYMin, CorridorL2XMax, CorridorL2XMin, CorridorL2YMax, CorridorL2YMin
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        