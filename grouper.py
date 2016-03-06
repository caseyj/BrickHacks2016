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
    
    # create empty list to append each group to
    groupList = [ ]
    
    # determine the number of guests 
    numberOfGuests = len(guestArray)
    
    
    ################################################################# 
    # if there are 2 or less guests, make 1 group
    if numberOfGuests <= 2:
        guestIndices = range(0,numberOfGuests)
        groupList, guestArray = create_group(guestArray, guestIndices, useAll='False')

    
    else: # create empty array to store sum totals for each diet/allergy 
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
    
    
        ################################################################# 
        # if 5 have same preference, group them
        if (preferencesSum==5).any(): 
            prefIndex = numpy.where(preferencesSum==5)[0][0]
            guestIndices = numpy.where(preferences[:,prefIndex]==1)[0]
            guestListTemp = [ ]
            for i in guestIndices: 
                guestListTemp.append(guestArray[i])
            group = Group(guestListTemp)
            groupList.append(group)
            
        ################################################################# 
        # if there are 4 of a single preference, make a group
        elif (preferencesSum==4).any(): 
            prefIndex = numpy.where(preferencesSum==4)[0][0]
            guestIndices = numpy.where(preferences[:,prefIndex]==1)[0]
            guestListTemp = [ ]
            for i in guestIndices: 
                guestListTemp.append(guestArray[i])
            group = Group(guestListTemp)
            groupList.append(group)
            
        # if there are 3 of a single preference, make a group
        elif (preferencesSum==3).any(): 
            prefIndex = numpy.where(preferencesSum==3)[0][0]
            guestIndices = numpy.where(preferences[:,prefIndex]==1)[0]
            guestListTemp = [ ]
            for i in guestIndices: 
                guestListTemp.append(guestArray[i])
            group = Group(guestListTemp)
            groupList.append(group)
        
        #################################################################    
        # 6 have same preference, split up into 2 groups of 3
        elif(preferencesSum==6).any(): 
            
            # check for 3 people with the same diet
            if (dietsSum==3).any(): 
                # make 1 group out of the 3 people with same diet
                dietIndex = numpy.where(dietsSum==3)[0][0]
                guestIndices = numpy.where(diets[:,dietIndex]==1)[0]
                guestListTemp = [ ]
                for i in guestIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)
                
                # determine the remaining guest indices for second group
                remainingIndices = range(0,numberOfGuests)
                for i in guestIndices: 
                    remainingIndices.remove(i)
                
                # put the other 3 people into a second group
                guestListTemp = []
                for i in remainingIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)
        
            
            # check for 3 people with the same allergies 
            elif (allergiesSum==3).any(): 
                
                # make 1 group out of the 3 people with same allergies
                allergyIndex = numpy.where(allergiesSum==3)[0][0]
                guestIndices = numpy.where(allergies[:,allergy]==1)[0]
                guestListTemp = [ ]
                for i in guestIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)
            
                # determine the remaining guest indices for second group
                remainingIndices = range(0,numberOfGuests)
                for i in guestIndices: 
                    remainingIndices.remove(i)
                
                # put the other 3 people into a second group
                guestListTemp = []
                for i in remainingIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)        
            
                
            # otherwise, arbitrarily split into 2 groups of 3
            else:
                maxDietsSum = max(dietsSum)
                maxAllergiesSum = max(allergiesSum) 
                
                ######## JOHN DO UR DICTIONARY THING HERE: #############################
                dic = dict()
                for i in groupList:
                    for j in i.exclusions:
                        if j in dic:
                            dic[j] = dic[j] + 1
                        else:
                            dic[j] = 1
                            # TODO: write code...
                maxExclusions = 'john do ur thing' 
                # split into two groups of 3 based on maxAllergiesSum and maxDietsSum
        
        #################################################################
        # 7 have same preference: split into 2 groups (f 4 and 3)
        elif (preferencesSum==7).any(): 
            
            # check for 4 people with the same diet
            if (dietsSum==4).any(): 
                # make 2 groups, of 4 and 3 people
                dietIndex = numpy.where(dietsSum==4)[0][0]
                guestIndices = numpy.where(diets[:,dietIndex]==1)[0]
                guestListTemp = [ ]
                for i in guestIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)
                
                # determine the remaining guest indices for second group
                remainingIndices = range(0,numberOfGuests)
                for i in guestIndices: 
                    remainingIndices.remove(i)
                
                # put the other 3 people into a second group
                guestListTemp = []
                for i in remainingIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)
            
            
            # check for 4 people with the same allergies 
            elif (allergiesSum==4).any(): 
                # make 2 groups, of 4 and 3 people 
                allergyIndex = numpy.where(allergiesSum==4)[0][0]
                guestIndices = numpy.where(allergies[:,allergy]==1)[0]
                guestListTemp = [ ]
                for i in guestIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)
            
                # determine the remaining guest indices for second group
                remainingIndices = range(0,numberOfGuests)
                for i in guestIndices: 
                    remainingIndices.remove(i)
                
                # put the other 3 people into a second group
                guestListTemp = []
                for i in remainingIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)  
                
    
            # otherwise, split arbitrarily into 2 groups, of 4 and 3 people 
            elif:
                maxDietsSum = max(dietsSum)
                maxAllergiesSum = max(allergiesSum) 
                
                ######## JOHN DO UR DICTIONARY THING HERE: #############################
                maxExclusions = 'john do ur thing' 
                # split into two groups of 3 based on maxAllergiesSum and maxDietsSum
    
        
        #################################################################
        # if 8 people have same preferences
        elif(preferencesSum>=8).any(): 
            
            # check for 4 of anything, starting with diet
            if (dietsSum==4).any(): 
                # make 2 groups, of 4 and 3 people
                dietIndex = numpy.where(dietsSum==4)[0][0]
                guestIndices = numpy.where(diets[:,dietIndex]==1)[0]
                guestListTemp = [ ]
                for i in guestIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)
                
                # determine the remaining guest indices for second group
                remainingIndices = range(0,numberOfGuests)
                for i in guestIndices: 
                    remainingIndices.remove(i)
                
                # put the other 3 people into a second group
                guestListTemp = []
                for i in remainingIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)
            
            # check for 4 with the same allergy 
            elif (allergiesSum==4).any(): 
                # make 2 groups, of 4 and 3 people 
                allergyIndex = numpy.where(allergiesSum==4)[0][0]
                guestIndices = numpy.where(allergies[:,allergy]==1)[0]
                
                
                #%#$^#%^^%^
                guestListTemp = [ ]
                for i in guestIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)
            
                # determine the remaining guest indices for second group
                remainingIndices = range(0,numberOfGuests)
                for i in guestIndices: 
                    remainingIndices.remove(i)
                
                # put the other 3 people into a second group
                guestListTemp = []
                for i in remainingIndices: 
                    guestListTemp.append(guestArray[i])
                group = Group(guestListTemp)
                groupList.append(group)          
            
            
            
            ######## JOHN DO UR DICTIONARY THING HERE: #############################
            #elif exclusions==4
            
            
            # so far we've only looked at preferences at first for grouping decisions 
            # next step in logic: look at diet, allergy, excluded ingredients. 
            
            
            # recursive call 
            g = grouper()
    
    return groupList



def create_group(guestArray, guestIndices, groupList=[], useAll='True'):
    """
    Function takes in indices of guests to be grouped together. 
    The group that is created gets appended onto groupList. 
    If "useAll" parameter is True, then the remaining guests in the guestArray
    get grouped together into a second group (which then gets appended onto groupList). 
    Otherwise, the remaining guests are left in guestArray for future grouping.
    """

    for i in guestIndices: 
        guestListTemp.append(guestArray[i])
        if useAll: 
            guestArray.remove(i)
        group = Group(guestListTemp)
        groupList.append(group)
    
    if useAll: 
        group = Group(guestArray)
        groupList.append(group)
    
    return groupList, guestArray
    


if __name__ == '__main__':
    
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
    
    guestArray = [vic, john, victoria, danny]
    
    g = grouper( guestArray, len(guestArray) )
    


    
        