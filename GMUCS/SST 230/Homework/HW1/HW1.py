"""
Craig Kimball (G01295498)
Systems 230 HW 1

1. This assignment is my own work.
2. I/We have not taken help from any other individuals or resources on this assignment that was not permitted. 
"""

"""
Problem 1 - Replace n outliers from an array
"""
def remove_outliers(outliers, list):
    #Length Error Handling
    if len(list) < 2*outliers:
        print(f'List is too short, must have at least {2*outliers} elements.')
        return list
    
    #store lowest and highest outliers
    outliers = sorted(list)[0:outliers]+sorted(list)[-outliers:]
    #list comprehension, None if an outlier or x if a value
    return ["None" if x in outliers else x for x in list]


#Input from User

nu_list = []
nu_entries = int(input('Enter the number of list entries?'))
for i in range(nu_entries):
   nu_list.append(int(input()))

nu_outliers = int(input('How many outliers would you like to remove? '))

#Function Call returns a copy of the list, 
#here I am printing it and not saving it

print(remove_outliers(2,nu_list))



"""
Problem 2 - Unique String Inputs
"""

print('Enter each string, end with a new line to stop adding')
#Getting User Input
string_list = [x for x in iter (input, '')]

#creating the unique list
unique_list = []

#Appends all unique values (not already added) in lowercase using .lower()
[unique_list.append(x.lower()) for x in string_list if x.lower() not in unique_list]

#prints the elements of the list seperated by a new line
print(*unique_list,sep='\n')
