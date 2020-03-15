def thirtyTwos(n):
    if (n<0):
        return 0
    else:
        temp = str(n)
        if (temp[0] == 3 and temp[2]):
                print(1 + thirtyTwos(temp[1:]))

			
thirtyTwos(432)
