"""
Code to check column design at unit 4 unit 5 interface
"""
def ElasticColumnDesign(thisLoc, resultsFolder):

    import os
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    fileLoc = thisLoc #get directory of results, set by User
    fileName = 'elasticColAxial.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    AxialData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
    AxialData = AxialData.values

    fileName = 'elasticColMy.csv'
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    MomentYData = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing moments using first row as column labels and time step as row labels
    MomentYData = MomentYData.values

    fileName = 'elasticColMz.csv'
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    MomentZData = pd.read_csv(filein,skiprows=[0,1,2,3]) #grabbing moments using first row as column labels and time step as row labels
    MomentZData = MomentZData.values
    
    fileName  = 'elasticColVy.csv'
    filein = os.path.join(fileLoc, fileName)
    ShearYData = pd.read_csv(filein, skiprows=[0,1,2,3])
    ShearYData = ShearYData.values
    
    fileName = 'elasticColVz.csv'
    filein = os.path.join(fileLoc, fileName)
    ShearZData = pd.read_csv(filein, skiprows=[0,1,2,3])
    ShearZData = ShearZData.values

    fileLoc = r'J:\S-F\230000\238558-00\4 Internal Project Data\4-04 Calculations\Struct\97 - LsDyna\Concrete Design'
    fileName = 'ElasticColNvsM.txt'
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
    maxShearY = []
    minShearY = []
    maxShearZ = []
    minShearZ = []
    
    #sort text PM Data so that it makes sense
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

    num_responses =  6 #time step, Axial force, Myy, Mzz, Vy, Vz
    num_time = AxialData.shape[0]
    num_el = AxialData.shape[1]-1

    #initialize array for element responses at each time step
    ElasticColResults = np.zeros((num_time,num_responses,num_el))
    
    #sort results into array
    for i in range(0,num_el):
        ElasticColResults[:,0,i] = AxialData[:,0]
        ElasticColResults[:,1,i] = AxialData[:,i+1]/1000
        ElasticColResults[:,2,i] = MomentYData[:,i+1]/1000
        ElasticColResults[:,3,i] = MomentZData[:,i+1]/1000
        ElasticColResults[:,4,i] = ShearYData[:,i+1]/1000
        ElasticColResults[:,5,i] = ShearZData[:,i+1]/1000
        minShearY.append(min(ElasticColResults[:,4,i]))
        maxShearY.append(max(ElasticColResults[:,4,i]))
        minShearZ.append(min(ElasticColResults[:,5,i]))
        maxShearZ.append(max(ElasticColResults[:,5,i]))
        
    ElasticColumn = resultsFolder+'/'+'ElasticColumn'
    if not os.path.exists(ElasticColumn):
        os.mkdir(ElasticColumn)
        
    plt.figure()
    for i in range(0,num_el):
        y = ElasticColResults[:,1,i]
        x = ElasticColResults[:,2,i]
        plt.scatter(x,y, label = 'Elastic Column Section '+str(i+1))
    x = M90
    y = P90
    plt.plot(x,y)
    plt.title("P-M Elastic Column Strong Axis")
    plt.xlabel("Moment (k-ft)")
    plt.ylabel("Axial Force (k)")
    plt.legend(loc='upper right')
    name = ElasticColumn+'/PM_Strong_Axis.png'
    plt.savefig(name, bbox_inches = 'tight')

    plt.figure()
    for i in range(0,num_el):
        y = ElasticColResults[:,1,i]
        x = ElasticColResults[:,3,i]
        plt.scatter(x,y, label='Elastic Column Section '+str(i+1))
    x = M0
    y = P0
    plt.plot(x,y)
    plt.title("P-M Elastic Column Weak Axis")
    plt.xlabel("Moment (k-ft)")
    plt.ylabel("Axial Force (k)")
    plt.legend(loc='upper right')
    name = ElasticColumn + '/PM_Weak_Axis.png'
    plt.savefig(name, bbox_inches = 'tight')
    plt.close('all')
    
    return maxShearY, minShearY, maxShearZ, minShearZ
