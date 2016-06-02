# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 23:49:47 2016

@author: Mason
"""

"""
Parser for flashscore data tables given by the DataMiner chrome addon. Returns only singles matches.
input: match data in the form of: 08.11.2015Djokovic N. (Srb)Murray A. (Gbr)2Â :Â 0
output: a list as follows: [date, player1, player2, match_result (eg, 3:2)]
"""

# TODO: Have it return dates in a way that matches our other data sets

def parseMatch(string):
    date_index_current_year = 12
    date_index_previous_year = 10

    if ":" in string[8:10]:
        date_index = date_index_current_year
    else:
        date_index = date_index_previous_year
    
    dateString = string[:date_index]
    string = string[date_index:]
    
    #Delete weird A's
    string = string[:len(string) - 6] + string[len(string)- 5:]
    string = string[:len(string) - 3] + string[len(string) - 2:]
    
    stringParts = string.split()
    if len(stringParts[1]) < 3 and stringParts[len(stringParts) - 1] in "0123456789":
        player1 = stringParts[1] + " " + stringParts[0]
        if len(stringParts) == 7:
            player2 = stringParts[3] + " " + stringParts[2][5:]
            setResult = stringParts[4][5] + ":" + stringParts[6]
        else:
            player2 = stringParts[4] + " " + stringParts[2][5:] + " " + stringParts[3]
            setResult = stringParts[5][5] + ":" + stringParts[7]
        return [dateString, player1, player2, setResult]
    else:
        return None
    
    
"""
Parser for flashscore URL's given by DataMiner chrome addon
input: match specific link in the form of: IcKE2Ah8
output: URL that will take you to that page


NOTE: The default set in a match is notated by a 1 on the end of the string, change this to go to different matches (2 = set 2 and so on)
"""
def parseURL(string):
    httpString = "http://www.flashscore.com/match/"
    endString = "/#point-by-point;1"
    url = string[4:]
    return httpString + url + endString
    
import pandas as pd


"""
Makes a new spreadsheet that is the cleaned up, parsed version of the input spreadsheet

NOTE: For inputs, please precede the string with a lowercase "r" so that it takes the literal and doesn't escape the "\"
eg. r"file_location"
"""
def clean_flashscore(excel_file_location, new_file_name):
    data = pd.read_excel(excel_file_location)
    matches = data["Match Data"]
    urls = data["URL"]
    
    cleaned_matches = pd.DataFrame(columns = ['Date', 'Player 1', 'Player 2', 'Result'])
    cleaned_urls = pd.Series(name = "URLS")
    cleaned_urls.rename("URLS")    
    
    for match in matches:
        cleaned_match = parseMatch(match)
        if cleaned_match != None:
            cleaned_matches.loc[len(cleaned_matches)] = cleaned_match
            
    for url in urls:
        cleaned_url = parseURL(url)
        cleaned_urls.loc[len(cleaned_urls)] = cleaned_url
        
    cleaned_matches["URLS"] = cleaned_urls
    
    cleaned_matches.to_excel(new_file_name + ".xlsx")
        
        
clean_flashscore(r"C:\Users\Mason\Desktop\Tennis Internship\flashscore_links\Djokovic.xlsx", "Djokovic_Cleaned")


    
    
    
