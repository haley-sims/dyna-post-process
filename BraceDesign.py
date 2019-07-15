"""
Code to check steel braces at each time step
Note: user must be in directory where results are located
"""
def BraceDesign(thisLoc, resultsFolder):

    import numpy as np
    import pandas as pd
    import math
    import os
    import xlrd
    import matplotlib.pyplot as plt

    fileLoc = thisLoc#get directory of results, set by User
    fileName = 'braceAxial.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    AxialData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
    AxialData = AxialData.values

    fileName = 'braceForceY.csv'
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    ShearYData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing shear forces using first row as column labels and time step as row labels
    ShearYData = ShearYData.values

    fileName = 'braceForceZ.csv'
    filein = filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    ShearZData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing shear forces using first row as column labels and time step as row labels
    ShearZData = ShearZData.values

    fileName = 'braceMyy.csv'
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    MomentYData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing moments using first row as column labels and time step as row labels
    MomentYData = MomentYData.values

    fileName = 'braceMzz.csv'
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    MomentZData = pd.read_csv(filein,skiprows=[0,1,2,3]) #grabbing moments using first row as column labels and time step as row labels
    MomentZData = MomentZData.values

    fileName = 'braceTorsion.csv'
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    TorsionData = pd.read_csv(filein,skiprows=[0,1,2,3]) #grabbing moments using first row as column labels and time step as row labels
    TorsionData = TorsionData.values

    #load beam dictionary with design info
    fileLoc = r'J:\S-F\230000\238558-00\4 Internal Project Data\4-04 Calculations\Struct\97 - LsDyna' #get directory of results, set by User
    fileName = 'BeamDesignInfo.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    BeamDesignInfo = pd.read_csv(filein, header=0, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12]) #all Beam design info
    BeamDesignInfo = BeamDesignInfo.values

    phi_axial = 0.9
    Fy = 50
    Fu = 65

    #Use data to calculate tension/compression
    num_responses =  20 #time step, Axial Force, Axial Capacity, Axial DCR, Moment Y, Moment Capoacity Y, Moment Z Moment Capacity Z, Moment Y DCR, 
                        #Moment X DCR, Torsion, Torsional Capacity, Torsion DCR, Shear Y
    num_time = AxialData.shape[0]
    num_el = BeamDesignInfo.shape[0]
    con_responses = 8 #time step, in plane shear, out of plane shear, tension/compression, Myy, Mzz, combined shear, Total value

    #initialize array for element responses at each time step
    BeamResults = np.zeros((num_time,num_responses,num_el))
    BeamConnection = np.zeros((num_time, con_responses, num_el))
    names = ['Time Step', 'Axial Force', 'Axial Capacity', 'Axial DCR', 'Moment Y', 'Moment Y Capacity', 
             'My DCR', 'Moment Z', 'Mz Capacity', 'Mz DCR', 'Torsion', 'Torsion Capacity', 'Torsion DCR', 
             'Shear Y', 'Shear Y Capacity','Vy DCR', 'Shear Z', 'Shear Z Capacity', 'Vz DCR', 'Total Interaction DCR']

    for i in range(1,num_el+1):
        # BeamResults[0,:,i] = names
        BeamConnection[:,0,i-1] = AxialData[:,0] #set timestep in BeamConnection
        BeamResults[:,0, i-1] = AxialData[:,0] #set timestep in BeamResults
        BeamResults[:,1, i-1] = AxialData[:,i]/1000 #Axial Force for responses
        BeamResults[:, 4, i-1] = MomentYData[:,i]/1000 #My data for responses
        BeamResults[:, 7, i-1] = MomentZData[:, i]/1000 #Mz data for responses
        BeamResults[:, 10, i-1] = TorsionData[:,i]/1000
        BeamResults[:, 13, i-1] = ShearYData[:, i]/1000
        BeamResults[:, 16, i-1] = ShearZData[:, i]/1000

    for i in range(0,num_el):
        for j in range(1,num_time):
            #Axial calculations
            if BeamResults[j,1,i] < 0:

                Fe = BeamDesignInfo[i,8]
                Fcr = 0.658**(Fy/Fe)*Fy
                Ag = BeamDesignInfo[i,4]
                Pn = Fcr*Ag
                phi_Pn = phi_axial*Pn
                DCR = BeamResults[j,1,i]/phi_Pn

            else:
                    Ag = BeamDesignInfo[i,4]
                    Pn = Fy*Ag
                    phi_Pn = phi_axial*Pn
                    Pu = Fu*Ag
                    phi_Pu= phi_axial*Pu
                    phi_Pn = min(phi_Pn,phi_Pu)
                    DCR = BeamResults[j,1,i]/phi_Pn
            BeamResults[j,2,i] = phi_Pn
            BeamResults[j,3,i] = abs(DCR)

        #Moment Calculations - should be built out to include check for compactness
            Z = BeamDesignInfo[i,9]
            Mn = Fy*Z
            phi_Mn = phi_axial*Mn
            BeamResults[j,5,i] = phi_Mn/12
            BeamResults[j,8,i] = phi_Mn/12
            DCR1 = BeamResults[j, 4, i]/phi_Mn
            DCR2 = BeamResults[j,7,i]/phi_Mn
            BeamResults[j, 6, i] = abs(DCR1)
            BeamResults[j,9,i] = abs(DCR2)

        #Torsion
            Fcr = 0.6*Fy
            if BeamDesignInfo[i,0] == 'HSS10x10x1/2':
                C = 84.2
            else:
                C = 123
                phi_Tn = Fcr*C*phi_axial
                BeamResults[j,11,i] = abs(BeamResults[j, 10,i])/phi_Tn

        #Shear calculations
            kv = 5.0
            Cv = 1.0
            if BeamDesignInfo[i,0] == 'HSS10x10x1/2':
                Aw = 2*0.5*(10-1.5)
            else:
                Aw = 2*0.5*(12-1.5)
            Vn = 0.6*Fy*Aw*Cv
            phi_Vn = phi_axial*Vn
            BeamResults[j,14,i] = phi_Vn
            BeamResults[j,17,i] = phi_Vn
            BeamResults[j, 15, i] = abs(BeamResults[j,13,i]/BeamResults[j,14,i])
            BeamResults[j,18,i] = abs(BeamResults[j, 16,i]/BeamResults[j,17,i])

        #Total interaction
            if BeamResults[j, 12, i] <= 0.2:
                if BeamResults[j, 3, i] < 0.2:
                    BeamResults[j, 19, i] = BeamResults[j, 3, i]*0.5 + BeamResults[j, 6,i] + BeamResults[j, 9,i] + (BeamResults[j, 15,i]+BeamResults[j, 18,i])**2
                else:
                    BeamResults[j, 19, i] = BeamResults[j, 3, i]*8/9 + BeamResults[j, 6,i] + BeamResults[j, 9,i] + (BeamResults[j, 15,i]+BeamResults[j, 18,i])**2
            else:
                if BeamResults[j,3,i] < 0.2:
                    BeamResults[j, 19, i] = BeamResults[j, 3, i]*0.5 + BeamResults[j, 6,i] + BeamResults[j, 9,i] + (BeamResults[j, 15,i]+BeamResults[j, 18,i]+BeamResults[j,12,i])**2
                else:
                    BeamResults[j, 19, i] = BeamResults[j, 3, i]*8/9 + BeamResults[j, 6,i] + BeamResults[j, 9,i] + (BeamResults[j, 15,i]+BeamResults[j, 18,i]+BeamResults[j,12,i])**2
                    
        #Anchorage data
            flag = BeamDesignInfo[i,12]
            if flag == 2:
                theta = BeamDesignInfo[i,13]
                BeamConnection[j,1,i] = BeamResults[j,1,i]*math.sin(theta)+BeamResults[j,13,i]*math.cos(theta)+BeamResults[j,16, i]*math.sin(theta) # in plane shear
                BeamConnection[j,2,i] = BeamResults[j,16,i]*math.cos(theta) #out of plane shear
                BeamConnection[j,3,i] = BeamResults[j,1,i]*math.cos(theta)+BeamResults[j,13,i]*math.sin(theta) #tensions/comcpression
                BeamConnection[j,4,i]= BeamResults[j,4,i]
                BeamConnection[j,5,i] = BeamResults[j,7,i]
            elif flag == 1:
                BeamConnection[j,1,i] = BeamResults[j,1,i] # in plane shear for vertical elements (axial force of the element)
                BeamConnection[j,2,i] = BeamResults[j,16,i] #out of plane shear
                BeamConnection[j,3,i] = BeamResults[j,13,i] #tension/compression (in plane shear of the element)
                BeamConnection[j,4,i] = BeamResults[j,4,i]
                BeamConnection[j,5,i] = BeamResults[j,7,i]
            else:
                BeamConnection[j,1,i] =BeamResults[j,13,i] #in plane shear
                BeamConnection[j,2,i] = BeamResults[j,16,i] #out of plane shear
                BeamConnection[j,3,i] = BeamResults[j,1,i] #tension/compression
                BeamConnection[j,4,i] = BeamResults[j,4,i] #MYy
                BeamConnection[j,5,i] = BeamResults[j,7,i] #Mzz
                
            BeamConnection[j,6,i] = (BeamConnection[j,2,i]**2+BeamConnection[j,1,i]**2)**.5/0.6
            BeamConnection[j,7,i] = BeamConnection[j,6,i]+BeamConnection[j,3,i]
        # title = 'BeamResults '+ str(BeamDesignInfo[i,0])+'.csv'
        # np.savetxt(title,BeamResults[:,:,i], delimiter=',')

    #anchorage calculations
    tensionCap = 4*60*0.44
    maxTension= np.zeros((num_el,1))
    maxShearIP = np.zeros((num_el,1))
    maxShearOP = np.zeros((num_el,1))
    maxShearComb = np.zeros((num_el, 1))
    maxMy = np.zeros((num_el,1))
    maxMz = np.zeros((num_el,1))
    maxTot = np.zeros((num_el, 1))
    maxDCR = np.zeros((num_el, 1))
    
    for i in range(0, num_el):
        maxTension[i] = max(BeamConnection[:,3,i])
        maxShearIP[i] = max(BeamConnection[:,1,i])
        maxShearOP[i] = max(BeamConnection[:,2,i])
        maxShearComb[i] = max(BeamConnection[:,6,i])
        maxMy[i] = max(BeamConnection[:,4,i])
        maxMz[i] = max(BeamConnection[:,5,i])
        maxTot[i] = max(BeamConnection[:,7,i])
        maxDCR[i] = max(BeamResults[:,19,i])
    
    BraceResults = resultsFolder+'/'+'BraceDesign'
    if not os.path.exists(BraceResults):
        os.mkdir(BraceResults)
        
    #plotting
    plt.figure()
    for i in range(0,num_el):
        x = BeamResults[:,0,i]
        y = BeamResults[:,19,i]
        plt.plot(x,y, label = BeamDesignInfo[i,0])
    plt.title("Brace DCR Interaction")
    plt.xlabel("Time step (S)")
    plt.ylabel('DCR')
    plt.legend(loc='upper right')
    name = BraceResults +'/'+'Brace_DCR_Interaction.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    for i in range(0,num_el):
        x = BeamResults[:,0,i]
        y = BeamConnection[:,1,i]
        plt.plot(x,y, label=BeamDesignInfo[i,0])
    plt.title('Embed in Plane Shear')
    plt.xlabel('Time Step (s)')
    plt.ylabel('Shear Force (k)')
    plt.legend(loc='upper right')
    name = BraceResults +'/'+'InPlane_Shear.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    for i in range(0, num_el):
        x = BeamResults[:,0, i]
        y = BeamConnection[:,2,i]
        plt.plot(x,y, label=BeamDesignInfo[i,0])
    plt.title('Embed Out of Plane Shear')
    plt.xlabel('Time Step (s)')
    plt.ylabel('Shear Force (k)')
    plt.legend(loc='upper right')
    name = BraceResults +'/'+'OOP_Shear.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    for i in range(0, num_el):
        x = BeamResults[:,0, i]
        y = BeamConnection[:,3,i]
        plt.plot(x,y, label=BeamDesignInfo[i,0])
    plt.axhline(y=tensionCap, color = 'r')
    plt.title('Embed Tension/Compression')
    plt.xlabel('Time Step (s)')
    plt.ylabel('Force (k)')
    plt.legend(loc='upper right')
    name = BraceResults +'/'+'Tension_Compression.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    for i in range(0, num_el):
        x = BeamResults[:,0, i]
        y = BeamConnection[:,4,i]
        plt.plot(x,y, label=BeamDesignInfo[i,0])
    plt.title('Embed Moment')
    plt.xlabel('Time Step (s)')
    plt.ylabel('Shear Force (k)')
    plt.legend(loc='upper right')
    name = BraceResults +'/'+'Myy.png'
    plt.savefig(name, bbox_inches='tight')

    plt.figure()
    for i in range(0, num_el):
        x = BeamResults[:,0, i]
        y = BeamConnection[:,5,i]
        plt.plot(x,y, label=BeamDesignInfo[i,0])
    plt.title('Embed Moment')
    plt.xlabel('Time Step (s)')
    plt.ylabel('Shear Force (k)')
    plt.legend(loc='upper right')
    name = BraceResults +'/'+'Mzz.png'
    plt.savefig(name, bbox_inches='tight')
    
    plt.close('all')
    print('Brace and Connection Design Complete')
    return maxDCR, maxTot, num_el
