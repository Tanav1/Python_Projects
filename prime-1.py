x= int(input("Enter value: ")) 
q = 2
y = x*2
prime = True


while q<x:
    if x % q == 0:
        prime = False
    q+=1



for var in range(x,y):
    if var > 1:
        for len in range(2, var):
            if (var % len) == 0:
                break
            else:
                p1=var
                break



for var in range(x): 
    if var > 1:
        for len in range(2, var):
            if (var % len) == 0:
                break
            else:
                p2=var


print("The prime closest to ",x," is: " )

if(x-p2>p1-x):
    print(p2)
elif (prime == True):
    print(x)
else:
    print(p2)

