def indices(some_list, another_list):
    rtn = []
    for i in range(len(some_list)):
        #checks if the value of each list at an index is the same
        if some_list[i] == another_list[i]:
            #adds that index to rtn list
            rtn.append(i)
    return rtn

def compute(lst1, lst2, lst3):
    rtn = []
    #for each value in lst1 <the shorter list>
    for i in range(len(lst1)):
        #if im supposed to sum
        if lst3[i] == True:
            #append the sum of the values at the index
            rtn.append(lst1[i] + lst2[i])
        else:
            #append the difference of the values at the index
            rtn.append(lst1[i]-lst2[i])
    return rtn

def replace_elems(lst1, lst2, n):
    rtn = []
    #if lst1 is shorter than lst2
    if len(lst1) <= len(lst2):
        for i in range(len(lst1)):
            #i+1 because positional math not index math
            if (i + 1) % n == 0:
                #append the lst2 value
                rtn.append(lst2[i])
            else:
                #append the lst1 value
                rtn.append(lst1[i])
    #if lst2 is shorter than lst1
    else:
        for i in range(len(lst2)):
            #positional math i+1
            if (i + 1) % n == 0:
                #append lst1 value
                rtn.append(lst1[i])
            else:
                #append lst2 value
                rtn.append(lst2[i])
    return rtn

def extra_copies(some_list):
    rtn = 0

    #creating a list of only unique values
    unique = []
    #for all values in list a
    for a in some_list:
        #boolean to hold logic resets to False with each itteration
        isin = False
        #b for each value in the unique list
        for b in unique:
            #is value already in the unique list
            if a == b:
                #set boolean to True
                isin = True
        #if my value was NOT anywhere in unique list
        if not isin:
            #append the value to unique list
            unique.append(a)

    #for each unique value
    for a in unique:
        #for each value in parameter list
        for b in some_list:
            if a == b:
                #count the instances of it
                rtn+= 1
    #logic above will count itself at least once so subtract the unecessary values
    rtn -= len(unique)

    return rtn


print(compute([89, 10, 83, 34, 21], [1, 1, 1, 1, 1], [True, False, True, False, True]), [90, 9, 84, 33, 22])