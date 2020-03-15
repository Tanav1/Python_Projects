print("Please enter n: ")
inpt = int(input())

num = 0
total = 0


while num < inpt:
    num += 1
    total += num

print("Please enter the numbers: ")

temp = 0
missingnum = 0
while temp < (inpt-1):
    print("Please enter a number: " )
    number = int(input())
    missingnum += number
    temp += 1

missingnum = total - missingnum
print("The missing number is: ", missingnum)
