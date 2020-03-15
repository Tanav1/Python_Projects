def largest(x, y, z):
    if x >= y and x>=z:
        big = x
        return big
    elif y>=x and y>=z:
         big = y
         return big
    elif z>=x and z>=y:
        big = z
        return big


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))


biggestnum = largest(x, y, z)
print ("The largest number is " + str(biggestnum))
