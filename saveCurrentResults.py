"""
Code to make current run an excel sheet with summary of all results as well as ground motion already imported
"""

def saveCurrentResults(groundMotion, runName):

    import os
    import openpyxl as op
    import datetime

    filedir = r'J:\S-F\230000\238558-00\4 Internal Project Data\4-04 Calculations\Struct\97 - LsDyna\0001_Results'

    #get date and time information to create unique folder with all results
    now = datetime.datetime.now()
    dateRef = str(now.month)+str(now.day)+str(now.year)
    timeRef = str(now.hour)+str(now.minute)+str(now.second)
    folderName= runName+'_'+groundMotion+'_'+dateRef+'-'+timeRef
    resultsFolder = os.path.join(filedir, folderName)
    #create folder for results
    if not os.path.exists(resultsFolder):
        os.mkdir(resultsFolder)

    templatedir = r'J:\S-F\230000\238558-00\4 Internal Project Data\4-04 Calculations\Struct\97 - LsDyna\0001_Results\TEMPLATES'

    jobFolder = filedir

    return resultsFolder, folderName, templatedir, jobFolder
