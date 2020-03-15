t = [2, 3, 4, 4, 4, 4, 5, 6, 7,-2]
t1 = [1, 4, 2, 3, 0, 69]


def connect(list1, list2, k): 
    firstnewlist = list(list1) #Duplicates list1
    templist = list(list1) #Duplicates list1
    secondtemplist = list(list1) #Duplicates list1
    secondlist = list(list2) #Duplicates list2

    temp = 0
    while(temp<len(firstnewlist)-k): #Slices first k numbers from rest of numbers
        templist.pop() #Removes elements from list
        temp+=1
    x = len(templist) #length of list1
    templist.extend(secondlist) #appends first k slice of list one with all of list 2

    temp2 = 0
    secondtemplist.reverse() #reverses list
    while(temp2<k): #gets second half of list 1 after k slice 
            secondtemplist.pop() #removes element from list
            temp2+=1 
    secondtemplist.reverse() #reverses list back to normal
    thirdlist = list(secondtemplist) #thirdlist which will be final list

    templist.extend(thirdlist) #finallist
    print(templist)
   

    
            
            



   
    
    

connect(t, t1, 6)
