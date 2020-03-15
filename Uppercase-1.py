print("Please enter a character")
x=input()
y= ord(x)

if 91>y>64:
    print("The Uppercase is: " + x)

elif 123>y>96:
    t= y-32
    n= chr(t)
    print("The Uppercase is: " + n)
else:
    print("You didn't enter an alphabet")


