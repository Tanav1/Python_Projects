#Avishan Bewtra - aqb6074, Tanav Thanjavuru - tzt5285, Jarrod Keating - jjk6165
#Extract data from booklist.txt and place into multidimensional list booklist
fileA = open("finalbooklist.txt", "r")

booklist = []
booklistFull = []
s = fileA.readline()

while(s != ""):
    s = s.rstrip("\n")

    booklist.append(s.split("#"))
    booklistFull.append(s.split("#"))

    s = fileA.readline()

fileA.close()



# Extract data from librarylog.txt and place into multidimensional list librarylog

librarylog = []


fileB = open("finallibrarylog.txt", "r")

s = fileB.readline()

while(s != ""):
    s = s.rstrip("\n")

    librarylog.append(s.split("#"))

    s = fileB.readline()

fileB.close()

# Based upon each entry to the library log, determine which type of action each entry indicates
#Then perform the action
# When necessary add a person to the people list
actionType = []

people = []
# each entry [name, fees, [book 1 name, day checked out, amount of days checked out], [book2 etc]]

# usage entry [title, days out, days possible]
usageList = []

currentDay = int(librarylog[len(librarylog)-1][0])
for u in booklistFull:
    usageList.append([u[0], 0, int(u[1])*(currentDay-1)])

for i in librarylog:

    if(i[0] == "PAY"):
        #Pay fees - FINISH
        actionType.append(4)
        for m in people:
            if(m[0] == i[2]):
                m[1] -= int(i[3])
    elif(i[len(i)-1] == "RET"):
        #Return book - FINISH
        actionType.append(2)
        # QUESTION:  DOES THE BOOK OR PERSON HAVE TO PREVIOUSLY EXIST, I AM CURRENTLY ASSUMING YES 
        for n in people:
            if(n[0] == i[2]):
                for o in range(2, len(n)):
                        if(n[o][0] == i[1]):
                            daysLate = int(i[0]) - int(n[o][1]) - int(n[o][2])
                            if(daysLate > 0):
                                for p in booklist:
                                    if(i[1] == p[0]):
                                        if(p[2] == "True"):
                                            n[1] = n[1] + (daysLate * 15)
                                        else:
                                            n[1] = n[1] + (daysLate * 5)

                            for z in usageList:
                                if(z[0] == i[1]):
                                    z[1] = z[1] + (int(i[0]) - int(n[o][1]))
                            n.pop(o)
                            break
        for x in booklist:
            if(x[0] == i[1]):
                x[1] = str(int(x[1]) + 1)
        #Remember to add fees at the time of return
        
    elif(len(i) == 3):
        #Add new book
        actionType.append(3)
        for k in range(len(booklist)):
            if(i[1] == booklist[k][0]):
                booklist[k][1] = str(int(booklist[k][1]) + 1)
                booklistFull[k][1] = str(int(booklistFull[k][1]) + 1)
                usageList[k][2] = usageList[k][2] + currentDay - 1 - int(i[0])
            elif(k == (len(booklist) - 1)):
                booklist.append([i[1], "1", i[2]])
                booklistFull.append(booklist[len(booklist)-1])
                usageList.append([i[1], 0, currentDay - 1 - int(i[0])])
    elif(len(i) == 4):
        #Checkout Book
        actionType.append(1)
        if(len(people) > 0):
            for j in range(len(people)):
                if(i[2] == people[j][0]):
                    people[j].append([i[1], i[0], i[3]])
                    break
                elif(j == len(people) - 1):
                    people.append([i[2], 0, [i[1], i[0], i[3]]])
        else:
            people.append([i[2], 0, [i[1], i[0], i[3]]])
        #subtract 1 copy from book list
        for l in range(len(booklist)):
            if(i[1] == booklist[l][0]):
                booklist[l][1] = str(int(booklist[l][1]) - 1)

#Functions that complete the assignment
def canCheckout():
    name = input("Enter a name: ")
    title = input("Enter a book: ")
    days = int(input("How many days would the book be checked out: "))
    for q in people:
        if(name == q[0]):
            if(q[1] > 50):
                print("No. They cannot check it out.", name, "has too many fines.")
                return False
    for r in range(len(booklist)):
        if(booklist[r][0] == title):
            if(int(booklist[r][1]) > 0):
                break
            elif(int(booklist[r][1]) == 0):
                print("No. There are no copies of", title, "available.")
                return False
        if(r == (len(booklist) - 1)):
            print("No. We do not have", title, "on our booklist.")
            return False
    for s in booklist:
        if(s[0] == title):
            if(s[2] == "True"):
                if(days > 7):
                    print("No.", title, "is important and can only be checked out for 7 days.")
                    return False
            else:
                if(days > 28):
                    print("No.", title, "can only be checked out for 28 days.")
                    return False
    print("Yes.", name, "can checkout", title)
    return True


def canReturn():
    name = input("Enter a name: ")
    title = input("Enter a book: ")
    for w in range(len(people)):
        if(people[w][0] == name):
            if(len(people[w]) > 2):
                for f in range(2, len(people[w])):
                    
                    if(people[w][f][0] == title):
                        print("They can!")
                        return True
    print("They cannot.")
    return False

           
def lateFees():
    for t in people:
        print(t[0], ":    $ ", t[1])


# usage = each entry looks like [bookname, days used, total days possible]
for a in people:
    if(len(a) > 2):
        for c in range(2, len(a)):
            for b in booklist:
                if(b[0] == a[c][0]):
                    for d in usageList:
                        if(d[0] == b[0]):
                            d[1] += currentDay - 1 - int(a[c][1])

def usage():
    for e in usageList:
        print(e[0], ":", e[1] / e[2] * 100, "%")
    largest = 0
    second = 1
    for g in range(1, len(usageList)):
        if(usageList[g][1] / usageList[g][2] * 100 >= usageList[largest][1] / usageList[largest][2] * 100):
            second = largest
            largest = g
        if(usageList[second][1] / usageList[second][2] * 100 < usageList[g][1] / usageList[g][2] * 100 < usageList[largest][1] / usageList[largest][2] * 100):
            second = g
    print("The most used books are", usageList[largest][0], "and", usageList[second][0])

while True:
    print("1 Can a person check out a certain book? \n2 Can a person return a certain book? \n3 Show me the list late fees due for each person. \n4 What is the usage of each book? Which are the top used books? \n5 Exit")
    print("Select one of the above:")
    value = input()
    if(value == "5"):
        break
    elif(value == "1"):
        canCheckout()
    elif(value == "2"):
        canReturn()
    elif(value == "3"):
        lateFees()
    elif(value == "4"):
        usage()


