print("Enter the number of students: ")
x= int(input())
n = 0
lowestscore = 101
secondlowestscore = 101



while(n<x):
    print("Enter the student's name")
    S1name=str(input())
    print("Enter the student's score: ")
    S1score= int(input())
    n+=1
    if S1score<lowestscore:
            secondlowestscore = lowestscore
            lowestname = S1name
            lowestscore = S1score
    if(S1score>lowestscore and S1score< secondlowestscore):
            secondlowestscore = S1score
            secondlowestname = S1name

            

        

print("The 2nd Lowest student is ", secondlowestname, "with a score of ", secondlowestscore)




    



    
