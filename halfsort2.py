print("Please enter the number of elements in the list")
x= int(input())



num = 0
lst = []
lst1 = []
lst2 =[]


while(num < x ):
    print("Enter a number: ")
    number = int(input())
    lst.append(number)
    num += 1
lst3= list(lst)
lst2.extend(lst)
lst1 = lst
lst1.reverse()
var = len(lst)/2
var1= len(lst)
num = 0
while(num <= var1):
    if (num < var):
        lst1.pop()
        lst2.pop()
    if (num >= var):
        lst1.sort()
    num+=1
lst2.extend(lst1)

print("You entered: ", lst3)
print("Sorted: ", lst2)
