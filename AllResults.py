"""
Code to run all fast tcf scripts
Note: user must be in directory where results are located
"""
def AllResults():
    import os
    import tkinter
    from tkinter import filedialog

    #suppress tkinter pop up window
    root = tkinter.Tk()
    root.overrideredirect(1)
    root.withdraw()

    #name file location for THIS .inp scripts to generate all results
    filedir = r'J:\S-F\230000\238558-00\4 Internal Project Data\4-04 Calculations\Struct\97 - LsDyna\scripts\THIS'
    # get all scripts to run to generate results from list of files in the THIS script folder
    files = os.listdir(filedir)

    # #ask user for the specific This file
    # thisFiles = filedialog.askopenfilename(parent=root, title= 'Choose a file')
    # thisFileNames = root.tk.splitlist(thisFiles)

    #assign executable command to run THIS in batch mode
    executable = r'"C:\Program Files\Ove Arup\v16.0_x64\this16_x64.exe"'

    #for each file in the script list, run the .inp and generate csv files
    for i in files:
        fullPath = os.path.join(filedir,i)
        cmd = '"' + str(executable)+ " -tcf=" + '"'+str(fullPath)+ '"'  +" -batch "+str(thisFileNames) + '"'
        os.system(cmd)
        print(str(i+' is complete'))

    #get the location of the THIS file and all the results csv's
    thisLoc = os.path.split(thisFile)[0]
    #get the name of the ground motion
    groundMotion = os.path.split(thisFile)[1]
    #get the name of the run number
    run = os.path.split(thisFile)[0]
    runName = os.path.split(run)[1]

    return runName, groundMotion, thisLoc
