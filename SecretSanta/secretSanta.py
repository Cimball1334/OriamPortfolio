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

def write_to_json(write):
    
    """Dump argument to json file for encoding
    
    The write_to_json file takes in a single argument and dumps the parameter to a specified json file.
    
    TODO: remove hardcoded names and replace with variables names

    Args:
        write (Any): write is the variable that will be dumbed to the json file
        

    Returns:
        None
        
        
    """
    with open('secret_santa.json','w') as file_write:
        json.dump(write, file_write)
        
def read_from_json():
    
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    with open('secret_santa.json') as file_read:
        return json.load(file_read)
        
def print_current(dictionary):
    
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

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
    
    for i in range(len(names)):
        for j in range(buffer):
            if dictionary[names[i]][-1] == names_random[-buffer]:
                assign_names(dictionary,buffer)
       
            
    #list has now been sorted according to rules
    for i in range(len(names)):
        dictionary[names[i]] = dictionary[names[i]]+[names_random[i]]
        

"""""""""""""""""""""""""""
    Variables
"""""""""""""""""""""""""""


grant_names = read_from_json()


"""""""""""""""""""""""""""
    Body
"""""""""""""""""""""""""""

assign_names(grant_names,2)

write_to_json(grant_names)

print_current(grant_names)

