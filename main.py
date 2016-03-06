##############
##main.py
##
##############

import json
import sys
from guest import *

def main():
    #take in name of json file from CL
    fileName = sys.argv[1]
    
    #create an empty list for all of our guests
    guests = list()
    
    #opens the json file and saves to variable json_data
    with open(fileName, 'r') as json_file:
        json_data = json.load(json_file)

    #loops through each object in the json and creates a guest for each one
    #   each guest is stored in guests
    for i in json_data:
        g = Guest(i['ID'], i['name'], i['pref'], i['diet'], i['allergy'], i['exclude'])
        guests.append(g)
    
    #here we will make a call to grouper
    
    #here we will output our grouper results to json&return
    
if __name__ == "__main__": main()