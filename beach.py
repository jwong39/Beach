n = 0
m = 0
people = []
record = []
listL = []
umbrella = int(input())
numLines = int(input())
while n != numLines:
    try:
        person = int(input())
    except:
        break
    if person not in people:
        people.append(person)
    n = n + 1
people.sort()

# people[people.size() - 1] #last element of list

def umbrellaCheck():
    n = 0
    while n != (len(people)):        # scroll through people list
        if people[n] not in record:
            record.append(people[n])
            if (n+1) < len(people):    # if the next spot is not empty
                x = n + 1               #  then x = the next spot
                numCover = people[n]

                while x != (len(people)):                                 # scroll through the remaining people
                    
                    if people[x] <= (people[n]+umbrella):                 # if the person is within distance of umbrella 
                        numCover = numCover + people[x] 
                        record.append(people[x])                          # record person if theyre within reach
                    x = x + 1
                if numCover > people[n]:                    
                    if len(listL) >= 1:                                   # issue: 4 is within the distance of 1
                        g = 0
                        while g != umbrella:                              # increment until you can add umbrella at safe distance
                            listL.append(int(numCover/umbrella)+g)        
                            if (int(numCover/umbrella)+g)-listL[len(listL)-2] < umbrella:
                                del listL[len(listL)-1]                   # delete umbrella if it's within distance of another umbrella
                            g = g + 1
                    elif len(listL) == 0:
                        listL.append(int(numCover/umbrella))

                    
            else:
                listL.append(people[n])
        elif people[n] in record:
            pass
        else:  
            listL.append(people[n])
        n = n + 1

def main():
    umbrellaCheck()
    for v in range(len(listL)):
        print(listL[v])
        v = v + 1
main()