def findRecommendations(matches):
    #stores the data
    base = list(matches)
    #wipes matches
    matches.clear()
    #formats the data by groups of 3
    for i in range(0,len(base)-1,3):
        if base[i+2] >= 80:
            matches.append([base[i],base[i+1],base[i+2]])
    #sort for highest by initial index
    #most is a position index not a value
    if len(matches) > 0:
        most = 0
        for i in range(len(matches)):
            if matches[i][2] > matches[most][2]:
                most = i
        #adding the heart
        matches[most].append("\u2665")
    
def compressInfo(datingTrack):
    base = list(datingTrack)
    datingTrack.clear()
    #adding first element to avoid index errors
    datingTrack.append((base[0][0],1))
    #for each index of base from 1 forward to the length
    for i in range(1,len(base)):
        #for each index of the datingTrack list from 0 forward to length
        isin = False
        for j in range(len(datingTrack)):
            #check if date is already in there
            if base[i][0] == datingTrack[j][0]:
                #if it is in there - increment
                datingTrack[j] = (datingTrack[j][0],datingTrack[j][1]+1)
                isin = True
        #do i need to add it?
        if not isin:
            #add the new date with 1 
            datingTrack.append((base[i][0],1))

def combineInfo(profileInfo, datingTrack):
    base = list(profileInfo)
    profileInfo.clear()

    #for each date
    for i in range(len(base)):
        isin = False
        for j in range(len(datingTrack)):
            #find the name for the date
            if datingTrack[j][0] == base[i][1]:
                #if the numbers match
                profileInfo.append([base[i][0],datingTrack[j][0],datingTrack[j][1]])
                isin = True

        if not isin:
            profileInfo.append([base[i][0],base[i][1]])

def setofNames(profiles, location):
    #create an empty set
    rtn = set()
    #loop through each set of values in dictionary
    for val in profiles.values():
        #do the locations match
        if val[2] == location:
            #add name to set
            rtn.add(val[0])

    return rtn

