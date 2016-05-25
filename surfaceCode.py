import pandas as pd

#For each surface I manually selected the surface as there were very few of those.

#This file is wherever you've stored the merged player data
tennisData = pd.read_excel(r"C:\Users\Mason\Desktop\Tennis Internship\player_data_merged.xlsx")
surfaces = tennisData["Surface"].unique()
surfaceDF = pd.DataFrame()
fileString = ""


#Iterates through all surfaces in the merged player data and generates a named excel sheet
#       for each containing the matches played on those surfaces.
for surface in surfaces:
    surfaceDF = tennisData.loc[tennisData["Surface"] == surface]
    fileString = surface + "_matches.xlsx"
    surfaceDF.to_excel(fileString)





#This creates a dataframe containing all matches on Hard surfaces (indoor and outdoor)
#But it doesn't order it by date. This will be done soon for chronological W/L.

OutdoorHardSurfaceDF = tennisData.loc[tennisData['Surface'] == "Hard"]
IndoorHardSurface = tennisData.loc[tennisData['Surface'] == "I.hard"]

finalHardDF = pd.concat([OutdoorHardSurfaceDF, IndoorHardSurface])


finalHardDF.to_excel('allHard_matches_unordered.xlsx')