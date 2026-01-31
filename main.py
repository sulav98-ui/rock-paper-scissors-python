import random
'''
1 for Rock 
-1 for Scissor 
0 for Paper 
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice (R=Rock, S=Scissor, P=Paper): ")

youDict = {"R": -1, "S": 1, "P": 0}
reverseDict = {-1: "Rock", 1: "Scissor", 0: "Paper"}

you=youDict[youstr]


print(f"You chose {reverseDict[you]}\ncomputer chose{reverseDict[computer]}")

if (computer == you):
    print ("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("Congrats! you won")
        
    elif(computer == -1 and you == 0):
        print("Oops! you loose")

    elif(computer == 1 and you == -1):
        print("Oh no! you loose")
    elif (computer== 1 and you == 0):
        print("Hurray! you won")
    elif (computer==0 and you == -1):
        print("Ohyeahhh! you won")
    elif (computer == 0 and you ==1):
        print("Opps! you loose")
    else:
        print("something is wrong")
                                                