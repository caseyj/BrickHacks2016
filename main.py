##############
##main.py
##
##############

import json
import sys
from guest import *
from grouper import *
from Group import *

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
	########################################
    # beef, chicken, plant based, pork, seafood
	 # beef, chicken, plant based, pork, seafood
    vic_pref = [0,0,1,0,0]
    john_pref = [0,0,0,1,0]
    victoria_pref = [0,1,0,0,0]
    danny_pref = [1,0,0,0,0]
    
    vic_pref =[0,0,0,0,1]
    john_pref = [0,0,0,0,1]
    victoria_pref = [0,0,0,0,1]
    danny_pref = [0,0,0,0,1]
	
    # pescetarian, vegetarian, laco vegetarian, ovo vegetarian, vegan, paleo
    vic_diet = [0,0,0,0,1,0]
    john_diet = [0,0,0,0,0,0]
    victoria_diet = [0,0,0,0,0,0]
    danny_diet = [0,0,0,0,0,0]
    
    # sesame, seafood, treenut, peanut, egg, soy, gluten, wheat, dairy, sulfite 
    vic_allergy = [0,0,0,0,0,0,0,0,1,0]
    john_allergy = [0,0,1,1,0,1,0,0,1,0]
    victoria_allergy = [0,0,0,0,0,0,0,0,0,0]
    danny_allergy = [0,0,0,0,0,0,0,1,0,0]
    
    vic_exclude = ['Celery']
    john_exclude = ['Beef', 'Oatmeal']
    victoria_exclude = ['']
    danny_exclude = ['Tomato']
    
    vic = Guest( '9999', 'Vic', vic_pref, vic_diet, vic_allergy, vic_exclude )
    john = Guest( '8675', 'John', john_pref, john_diet, john_allergy, john_exclude)
    victoria = Guest( '1234', 'Victoria', victoria_pref, victoria_diet, victoria_allergy, victoria_exclude )
    danny = Guest( '8881', 'Danny', danny_pref, danny_diet, danny_allergy, danny_exclude )
    d5 = Guest( '8881', 'D5', danny_pref, danny_diet, danny_allergy, john_exclude )
    d4 = Guest( '8881', 'D4', danny_pref, danny_diet, danny_allergy, john_exclude )
    d3 = Guest( '8881', 'D3', danny_pref, danny_diet, danny_allergy, john_exclude )
    
    guestArray = [vic, john, victoria, danny, d5, d4, d3]
    
    g = grouper( guestArray, len(guestArray) )
    print g
    dList = list()
    for i in g:
    	dList.append(i.toDictGroup())
    #here we will output our grouper results to json&return
    with open('groupy.json', 'wb') as outfile:
        #groups = groups[0].pref
        json.dump(dList, outfile)
    
if __name__ == "__main__": main()