
fread = open("DobA.txt","r")

fwrite = open("DobB.txt","w")




test = fread.readline()
test = test.rstrip("\n")
while test != "":
    test = test.split()
    b = (test[(len(test)-1)])
    name = ' '.join(test[0:-1])
    



    mm, dd, year = test[-1].split("/")
    test = fread.readline()
    dob = dd + "/" + mm + "/" + year
    

    fwrite.write(name + ' ' + str(dob) + '\n')


fread.close()
fwrite.close()
