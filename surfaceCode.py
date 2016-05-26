import pandas as pd

#For each surface I manually selected the surface as there were very few of those.

#This file is wherever you've stored the merged player data
tennisData = pd.read_excel(r"C:\Users\Mason\Desktop\Tennis Internship\player_data_merged.xlsx")
print (tennisData)
surfaces = tennisData["Surface"].unique()
surfaceDF = pd.DataFrame()
fileString = ""


#Iterates through all surfaces in the merged player data and generates a named excel sheet
#       for each containing the matches played on those surfaces.

#for surface in surfaces:
#    surfaceDF = tennisData.loc[tennisData["Surface"] == surface]
#    fileString = surface + "_matches.xlsx"
#    surfaceDF.sort(["Date"]) # Just to be sure they're sorted by date
#    surfaceDF.to_excel(fileString)


#This creates a dataframe containing all matches on Hard surfaces (indoor and outdoor)
#This df is sorted by date

OutdoorHardSurfaceDF = tennisData.loc[tennisData['Surface'] == "Hard"]
IndoorHardSurface = tennisData.loc[tennisData['Surface'] == "I.hard"]

finalHardDF = OutdoorHardSurfaceDF.append(IndoorHardSurface)

finalHardDF.sort_values(["Date"])

print (finalHardDF)

#finalHardDF.to_excel('allHard_matches_unordered.xlsx')