import numpy 
import json

#string ID
#string Name
#string preference
# 1d array diet 6l
# 1d array allergy 10 length
#array of stringsexclusions
 
class Group:
    groupPref
    groupdiet
    groupAllergies
    groupExclusions
    groupMembersID
    groupMembersName
    
    def __init__(self, groupPref, groupdiet, groupAllergies, groupExclusions, groupMembersID, groupMembersID, groupMembersName):
        self.groupPref = groupPref
        self.groupdiet = 
 
def grouper(guestArray):

    numberOfGuests = guestArray.shape[1]
    dietAndAllergies = numpy.zeros([numberOfGuests, 16])
    for i, guest in ennumerate(guestArray): 
        dietAndAllergies[i,:] = numpy.hstack(guest.diet,guest.allergy)
       
    
    return 
    
    
    
     
if __name__ == '__main__':
    
    
     
