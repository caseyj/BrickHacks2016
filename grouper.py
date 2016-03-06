import numpy 
import json
from guest import *
from Group import *

def grouper(guestArray, totalNumber):
    '''
    Algorithm that will create groups for the correct yummly call
    
    RETURNS: a list of group objects along with all restrictions the entire
    group must adhere to
    '''
    
    # the optimal size of a group, this may differ between 3-5 at 6
    #   we hope two groups of 3 would be created as opposed to a group of 
    #   2 and a group of 4
    OPTIMAL_SIZE = 4
    
    groupList = []
    
    # determine the number of guests 
    numberOfGuests = len(guestArray)
    
    # if 2 or less guests, make it a group
    if numberOfGuests <= 2:
        guestIndices = [0,1]
        guestListTemp = []
        for i in guestIndices: 
            guestListTemp.append(groupArray[i])
        group = Group(guestListTemp)
        groupList.append(group)
    
    # create empty array to store sum totals for each diet/allergy 
    diets = numpy.zeros([numberOfGuests, 6])
    allergies = numpy.zeros([numberOfGuests,10])
    
    # create empty array to store preferences
    preferences = numpy.zeros([numberOfGuests,5])
    
    # loop through guest array, append diet/allergy/preference data to respective arrays
    for i, guest in enumerate(guestArray): 
        diets[i,:] = guest.diet
        allergies[i:] = guest.allergy
        preferences[i,:] = guest.pref
    
    # calculate sum totals for each diet/allergy, and preference
    dietsSum = numpy.sum(diets,0)
    allergiesSum = numpy.sum(allergies,0)
    preferencesSum = numpy.sum(preferences,0)

    # if there are 5 of a single preference, make a group
    if (preferencesSum==5).any(): 
        prefIndex = numpy.where(preferencesSum==5)[0][0]
        guestIndices = numpy.where(preferences[:,prefIndex]==1)[0]
        guestListTemp = []
        for i in guestIndices: 
            guestListTemp.append(groupArray[i])
        group = Group(guestListTemp)
        groupList.append(group)

    # if there are 4 of a single preference, make a group
    elif (preferencesSum==4).any(): 
        prefIndex = numpy.where(preferencesSum==4)[0][0]
        guestIndices = numpy.where(preferences[:,prefIndex]==1)[0]
        guestListTemp = []
        for i in guestIndices: 
            guestListTemp.append(groupArray[i])
        group = Group(guestListTemp)
        groupList.append(group)
        
    # if there are 3 of a single preference, make a group
    elif (preferencesSum==3).any(): 
        prefIndex = numpy.where(preferencesSum==3)[0][0]
        guestIndices = numpy.where(preferences[:,prefIndex]==1)[0]
        guestListTemp = []
        for i in guestIndices: 
            guestListTemp.append(groupArray[i])
        group = Group(guestListTemp)
        groupList.append(group)
        
        
    # if 6 have same preference, split up into 2 groups of 3
    elif(preferencesSum==6).any(): 
        
        # check for 3 people with the same diet
        if (dietsSum==3).any(): 
            # make 2 groups
        
        # check for 3 people with the same allergies 
        elif (allergiesSum==3).any(): 
            # make 2 groups 
            
        # otherwise, arbitrarily split into 2 groups of 3
        elif:
            maxDietsSum = max(dietsSum)
            maxAllergiesSum = max(allergiesSum) 
            
            ######## JOHN DO UR DICTIONARY THING HERE: #############################
            maxExclusions = 'john do ur thing' 
            # split into two groups of 3 based on maxAllergiesSum and maxDietsSum
    
    
    # if 7 have same preference, split into 2 groups (of 4 and 3)       
    elif (preferencesSum==7).any(): 
        # check for 4 people with the same diet
        if (dietsSum==4).any(): 
            # make 2 groups, of 4 and 3 people
        
        # check for 4 people with the same allergies 
        elif (allergiesSum==4).any(): 
            # make 2 groups, of 4 and 3 people 

        # otherwise, split arbitrarily into 2 groups, of 4 and 3 people 
        elif:
            maxDietsSum = max(dietsSum)
            maxAllergiesSum = max(allergiesSum) 
            
            ######## JOHN DO UR DICTIONARY THING HERE: #############################
            maxExclusions = 'john do ur thing' 
            # split into two groups of 3 based on maxAllergiesSum and maxDietsSum


    # if 8 people have same preferences
    elif(preferencesSum>=8).any(): 
        # check for 4 of anything
        if (dietsSum==4).any(): 
            # group these 4 people together 
        elif (allergiesSum==4).any(): 
            # group these 4 people together 
            
        ######## JOHN DO UR DICTIONARY THING HERE: #############################
        #elif exclusions==4
        
        # recursive call 

    
    return 0


if __name__ == '__main__':
    
    
    # beef, chicken, plant based, pork, seafood
    vic_pref = numpy.asarray( [0,0,1,0,0] )
    john_pref = numpy.asarray( [0,0,0,1,0] )
    victoria_pref = numpy.asarray( [0,1,0,0,0] )
    danny_pref = numpy.asarray( [1,0,0,0,0] )
    
    vic_pref = numpy.asarray( [0,0,0,0,1] )
    john_pref = numpy.asarray( [0,0,0,0,1] )
    victoria_pref = numpy.asarray( [0,0,0,0,1] )
    danny_pref = numpy.asarray( [0,0,0,0,1] )
	
    # pescetarian, vegetarian, laco vegetarian, ovo vegetarian, vegan, paleo
    vic_diet = numpy.asarray( [0,0,0,0,1,0] )
    john_diet = numpy.asarray( [0,0,0,0,0,0] )
    victoria_diet = numpy.asarray( [0,0,0,0,0,0] )
    danny_diet = numpy.asarray( [0,0,0,0,0,0] )
    
    # sesame, seafood, treenut, peanut, egg, soy, gluten, wheat, dairy, sulfite 
    vic_allergy = numpy.asarray( [0,0,0,0,0,0,0,0,1,0] )
    john_allergy = numpy.asarray( [0,0,1,1,0,1,0,0,1,0] )
    victoria_allergy = numpy.asarray( [0,0,0,0,0,0,0,0,0,0] )
    danny_allergy = numpy.asarray( [0,0,0,0,0,0,0,1,0,0] )
    
    vic_exclude = numpy.asarray( ['Celery'] )
    john_exclude = numpy.asarray( ['Beef', 'Oatmeal'] )
    victoria_exclude = numpy.asarray( [''] )
    danny_exclude = numpy.asarray( ['Tomato'] )
    
    vic = Guest( '9999', 'Vic', vic_pref, vic_diet, vic_allergy, vic_exclude )
    john = Guest( '8675', 'John', john_pref, john_diet, john_allergy, john_exclude)
    victoria = Guest( '1234', 'Victoria', victoria_pref, victoria_diet, victoria_allergy, victoria_exclude )
    danny = Guest( '8881', 'Danny', danny_pref, danny_diet, danny_allergy, danny_exclude )
    
    groupArray = [vic, john, victoria, danny]
    
    g = grouper( groupArray, len(groupArray) )
    


    
        