##############
##main.py
##
##############

import json


def main():
    #take in name of json file from CL
    fileName = sys.argv[0]
    
    guests = list()
    
    with open(fileName) as json_file:
        json_data = json.load(json_file)
    
    for i in range(json_data):
        print json_data[i]['']
    
    
    # preference first
    # apply all dietary needs and allergies to that 
    
    
    
if __name__ == "__main__": main()