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
    #
    # templatedir = r'J:\S-F\230000\238558-00\4 Internal Project Data\4-04 Calculations\Struct\97 - LsDyna\0001_Results\TEMPLATES'
    # templates = os.listdir(templatedir)
    # loop through each template and save as new file with date and time stamp
    # for i in templates:
    #     fileName = 'TEMPLATE.xlsx'
    #     filein = os.path.join(filedir, fileName) # full worksheet name to be manipulated
    #     xlworkbook = op.load_workbook(filein)
    #     excelSave = resultsFolder+'/'+folderName+'.xlsx'
    #
    #
    # xlworkbook.save(excelSave)

    return resultsFolder, xlworkbook, excelSave
