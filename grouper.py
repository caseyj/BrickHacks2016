import numpy 
import json


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
    
    # determine the number of guests 
    numberOfGuests = guestArray.shape[1]
    
    # create empty array to store sum totals for each diet/allergy 
    dietAndAllergies = numpy.zeros([numberOfGuests, 16])
    
    # loop through guest array, append diet/allergy vectors to array
    for i, guest in ennumerate(guestArray): 
        dietAndAllergies[i,:] = numpy.hstack((guest.diet,guest.allergy))
    
    # calculate sum totals for each diet/allergy
    dietAllergiesSum = numpy.sum(dietAndAllergies,1)
    print 'dimensions of sum array: ', dietAllergiesSum.shape
    
    # if any diet/allergy has 
    
    
    
    return 
    
    
    
    