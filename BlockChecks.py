"""
Code to check the blocks
Note: user must be in directory where results are located
"""
def BlockChecks(thisLoc, resultsFolder):
    import os
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    fileLoc = thisLoc #get directory of results, set by User
    fileName = 'blockForceX.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    BlockX = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
    BlockX = BlockX.values

    fileName = 'blockForceY.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    BlockY = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
    BlockY = BlockY.values

    fileName = 'blockForceZ.csv' #name of the csv results to be read in
    filein = os.path.join(fileLoc, fileName) # full file name for pandas to read
    BlockZ = pd.read_csv(filein, skiprows=[0,1,2,3]) #grabbing axial forces using first row as column labels and time step as row labels
    BlockZ = BlockZ.values
    
    BlockCapComp = [2940, 2450, 2450, 2940, 2450, 2940, 2940, 2940, 4900]
    BlockCapX = [75.6,63,63,75.6,63,75.6,75.6,75.6, 243]
    BlockCapY = BlockCapX

    BlockChecks = resultsFolder+'/'+'JointBridgingElements'
    if not os.path.exists(BlockChecks):
        os.mkdir(BlockChecks)

    num_responses =  4 #time step, BlockX, BlockY, BlockZ
    num_time = BlockX.shape[0]
    num_el = BlockX.shape[1]-1
    BlockResults = np.zeros((num_time,num_responses,num_el+1))
    maxForceX = []
    minForceX=[]
    maxForceY=[]
    minForceY=[]
    for i in range(0,num_el):
        BlockResults[:,0,i] = BlockX[:,0]
        BlockResults[:,1,i] = BlockX[:,i+1]/1000 #X Forces for each Block
        BlockResults[:,2,i] = BlockY[:,i+1]/1000 #Y Forces
        BlockResults[:,3,i] = BlockZ[:,i+1]/1000 # Z Forces
        maxForceX.append(max(BlockResults[:,1,i]))
        minForceX.append(min(BlockResults[:,1,i]))
        maxForceY.append(max(BlockResults[:,2,i]))
        minForceY.append(min(BlockResults[:,2,i]))

    #plotting
    dir = ['X', 'Y', 'Z']
    for j in range(1,4):
        fig, axs = plt.subplots(nrows=3,ncols=3,constrained_layout=True)
        figtitle ='Block Force in '+ str(dir[j-1])+' Direction'
        fig.suptitle(str(figtitle))
        for i in range(0,num_el):
            if i < 3:
                if i == 1:
                    x = BlockResults[:,0,i]
                    y = BlockResults[:,j,i]
                else:
                    x = BlockResults[:,0,i]
                    y = BlockResults[:,j,i]
                axs[i,0].plot(x,y)
                axs[i,0].axhline(y=BlockCapX[i], color ='r', label='Block Capacity')
                axs[i,0].axhline(y=BlockCapX[i]*-1, color = 'r')
                title = 'Block '+str(i+1)+ ' Force'
                axs[i,0].set_title(str())
                # plt.tight_layout()
            elif i >= 3 and i < 6:
                if i == 5:
                    x = BlockResults[:,0,i]
                    y = BlockResults[:,j,i]
                else:
                    x = BlockResults[:,0,i]
                    y = BlockResults[:,j,i]
                axs[i-4,1].plot(x,y)
                axs[i-4,1].axhline(y=BlockCapX[i], color ='r', label='Block Capacity')
                axs[i-4,1].axhline(y=BlockCapX[i]*-1, color = 'r')
                title = 'Block '+str(i+1)+ ' Force'
                axs[i-4,1].set_title(str(title))
                # plt.tight_layout()
            else:
                if i == 9:
                    x = BlockResults[:,0,i]
                    y = BlockResults[:,j,i]
                else:
                    x = BlockResults[:,0,i]
                    y = BlockResults[:,j,i]
                axs[i-6,2].plot(x,y)
                axs[i-6,2].axhline(y=BlockCapX[i], color ='r', label='Block Capacity')
                axs[i-6,2].axhline(y=BlockCapX[i]*-1, color = 'r')
                title = 'Block '+str(i+1)+ ' Force'
                axs[i-6,2].set_title(str(title))
                # plt.tight_layout()
        name = BlockChecks +'/'+str(figtitle)
        plt.savefig(name, bbox_inches='tight')
 
    return BlockCapX, BlockCapY, BlockCapComp, maxForceX, minForceX, maxForceY, minForceY
