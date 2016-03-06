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
        group = Group()
        return group 
    
    # create empty array to store sum totals for each diet/allergy 
    dietAndAllergies = numpy.zeros([numberOfGuests, 16])
    # create empty array to store preferences
    preferences = numpy.zeros([numberOfGuests,5])
    
    # loop through guest array, append diet/allergy vectors to array
    for i, guest in enumerate(guestArray): 
        dietAndAllergies[i,:] = numpy.hstack((guest.diet,guest.allergy))
        preferences[i,:] = guest.pref
    
    # calculate sum totals for each diet/allergy, and preference
    dietAllergiesSum = numpy.sum(dietAndAllergies,0)
    preferencesSum = numpy.sum(preferences,0)

    # if there are 4 or 5 of a single preference, make a group
    if (preferencesSum==5).any(): 
        prefIndex = numpy.where(preferencesSum==5)[0][0]
        guestIndices = numpy.where(preferences[:,prefIndex]==1)[0]
        guestListTemp = []
        for i in guestIndices: 
            guestListTemp.append(groupArray[i])
        group = Group(guestListTemp)
        groupList.append(group)

    elif (preferencesSum==4).any(): 
        prefIndex = numpy.where(preferencesSum==4)[0][0]
        guestIndices = numpy.where(preferences[:,prefIndex]==1)[0]
        guestListTemp = []
        for i in guestIndices: 
            guestListTemp.append(groupArray[i])
        group = Group(guestListTemp)
        groupList.append(group)

        
    # IF 6, split it up. Base it off of ingredients they can't have.
    
    
    # IF 7, then split 4 off and then deal with the 3. 
        



    
    # elif any diet/allergy has 4, create a group
    
    # if there aren't 4, check if less than 4. If so, make a group. 
    
    # 
    
    
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
    


    
        