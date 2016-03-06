##############
##main.py
##
##############

import json
import sys

def main():
    #take in name of json file from CL
    fileName = sys.argv[1]
    print fileName
    guests = list()
    
    with open(fileName, 'r') as json_file:
        json_data = json.load(json_file)
    
    guests = list
    for i in json_data:
        print i['pref']
    
    
    # preference first
    # apply all dietary needs and allergies to that 
    
    
    
if __name__ == "__main__": main()