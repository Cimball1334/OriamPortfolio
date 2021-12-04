"""
Author: Craig Kimball
Date: 11/7/2021

"""



"""""""""""""""""""""""""""
    Imports
"""""""""""""""""""""""""""

import json
import random

# grant_names = {'Granny': ['Jackie','Ali','Cameron','Trina','Megan','Kevin'],
#                 'Grandpa': ['Katy','Lesley','Richard','Kevin','Scott','Ali'],
#                 'Jackie': ['Kiki','Scott','Lesley','Cameron','Trina','Cameron'],
#                 'Kevin': ['Grandpa','Kiki','Scott','Megan','Cameron','Richard'],
#                 'Ali': ['Trina','Kevin','Jackie','Scott','Katy','Lesley'],
#                 'Kiki': ['Lesley','Granny','Trina','Katy','Richard','Stuart'],
#                 'Scott': ['Kevin','Jackie','Granny','Lesli','Ali','Kiki'],
#                 'Trina': ['Ali','Katy','Ali','Kiki','Chloe','Grandpa'],
#                 'Lesley': ['Cameron','Trina','Grandpa','Chloe','Kevin','Granny'],
#                 'Richard': ['Scott','Cameron','Kevin','Jackie','Granny','Trina'],
#                 'Katy': ['Granny','Richard','Kiki','Ali','Grandpa','Megan'],
#                 'Cameron': ['Richard','Grandpa','Katy','Richard','Lesley','Jackie'],
#                 'Chloe': ['','','','Granny','Kiki','Scott'],
#                 'Meagan': ['','','','Grandpa','Jackie','Katy'],
#                 'Stuart': ['','','','','','Chloe']
#             }

# """Summary line.
#
#     Extended description of function.
#
#     Args:
#         arg1 (int): Description of arg1
#         arg2 (str): Description of arg2
#
#     Returns:
#         bool: Description of return value
#
#     """

"""""""""""""""""""""""""""
    Functions
"""""""""""""""""""""""""""

def write_to_json(write,file):
    
    """Dump argument to json file for encoding
    
    The write_to_json file takes in a 2 arguments and dumps the parameter write to a specified json file.
    

    Args:
        write (Any): write is the variable that will be dumbed to the json file
        file (string): path to file
        

    Returns:
        None
        
        
    """
    with open(file,'w') as file_write:
        json.dump(write, file_write)
        
def read_from_json(file):
    
    """Read data from a json for decoding

    The read_from_json file takes in a single parameter of a file location and decodes the data

    Args:
        file (string):  path to json file 

    Returns:
        object: returns decoded json data

    """
    with open(file) as file_read:
        return json.load(file_read)
        
def print_current(dictionary):
    
    """Print the current Seccret Santa Assignments to the console

    print_current prints out the key, and final value for each elemetn of dictionary

    Args:
        dictionary (Dict): a dictionary containing array as the values

    Returns:
        None: prints to console

    """
    for key in dictionary:
        print('{:<8} -->  {}'.format(key, dictionary[key][-1]))
        
def assign_names(dictionary, buffer):
    #rules: cannot be most recent, must not be spouse
    
    names = list(dictionary.keys())
    names_random = names[:]
    
    random.shuffle(names_random)
    print(names_random)
    
    #implement rules

    
       
            
    #list has now been sorted according to rules
    for i in range(len(names)):
        dictionary[names[i]] = dictionary[names[i]]+[names_random[i]]
        

"""""""""""""""""""""""""""
    Variables
"""""""""""""""""""""""""""

file_name = 'secret_santa.json'

grant_names = read_from_json(file_name)


"""""""""""""""""""""""""""
    Body
"""""""""""""""""""""""""""

assign_names(grant_names,2)

write_to_json(grant_names,file_name)

print_current(grant_names)

