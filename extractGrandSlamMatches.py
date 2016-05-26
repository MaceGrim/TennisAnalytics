import pandas as pd


### Takes an excel spreadsheet of tennis matches and creates a new spreadsheet containing the subset of those matches which were played in
###     Grand Slam tournaments
### Inputs:
###     string excelFileLocation - the location of the file containing the tennis matches
###     string desiredName - the name for the new file I_want_this_name.xlsx

def extractGrandSlamMatches(excelFileLocation, desiredName):
    grandSlams = ["U.S. Open - New York", "Wimbledon - London", "French Open - Paris", "Australian Open - Melbourne"]
    inputDataFrame = pd.read_excel(excelFileLocation)
    grandSlamMatchesFromInput = pd.DataFrame()
    grandSlamMatchesFromInput = inputDataFrame.loc[inputDataFrame['Tournament'].isin(grandSlams)]
    
    newFileName = desiredName + ".xlsx"
    grandSlamMatchesFromInput.to_excel(newFileName)

### Same as above, but for non-grand slam tourneys

def extractNonGrandSlamMatches(excelFileLocation, desiredName):
    grandSlams = ["U.S. Open - New York", "Wimbledon - London", "French Open - Paris", "Australian Open - Melbourne"]
    inputDataFrame = pd.read_excel(excelFileLocation)
    grandSlamMatchesFromInput = pd.DataFrame()
    grandSlamMatchesFromInput = inputDataFrame.loc[~inputDataFrame['Tournament'].isin(grandSlams)]
    
    newFileName = desiredName + ".xlsx"
    grandSlamMatchesFromInput.to_excel(newFileName)


#extractGrandSlamMatches(r"C:\Users\Mason\Desktop\Tennis Internship\player_data_merged.xlsx", "complete__grand_slam_matches")
#extractNonGrandSlamMatches(r"C:\Users\Mason\Desktop\Tennis Internship\player_data_merged.xlsx", "complete_non_grand_slam_matches")