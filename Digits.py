x = int(input("Enter a three digit number:"))

one= x//100
two= (x//10) % 10
three= x%10

print("The first digit is: " + str(one))
print("The second digit is: " + str(two))
print("The third digit is: " + str(three))

