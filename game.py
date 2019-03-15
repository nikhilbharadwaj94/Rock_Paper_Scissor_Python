import random

print("the creator of this game is Nikhil Bharadwaj")
print("Version 2.0")

#initialize the variables
lose = "the computer wins"
win = "You Win"

lives=5
score = 0
draw = 0
computer_lives = 7
password_list = []
#Now for the main logic
while True:
    print("To begin with fill in the below information")
    userName = input("Please enter your user name:   ")
    password = input("Please enter your password:   ")
    searchFile = open("acounts.txt", "r")
    for line in searchFile:
	password_list.append(line.strip())
        if userName and password in password_list:
            print("Welcome ", userName)
            print("Basic Rules of the game")
            print("You start the game with ", lives , " lives")
            print("if you win you get an extra life")
            print("if you lose one of ur life is reduced")
            print("if you draw then number of lives remains same")
            print("Same rules apply to the computer as well")
            print("to see a list of rules type \"rules\"")
            print("At any point type \"exit\" to leave the game")
            print("------------------------------------------------------")
            print("------------------------------------------------------")
            print("CAN YOU BEAT THE COMPUTER??????")
            print("Good Luck <3")
            while True:
                rps = input("rock, paper, scissor?   ")
               # rps = rps.lower()
                computer = ("rock", "paper", "scissor")
                c_choice = random.choice(computer)
                #When user chooses rock
                if rps == "rock" and c_choice =="rock":
                    print("the computer chooses ", c_choice)
                    print(draw)
                if rps == "rock" and c_choice =="paper":
                    print("the computer chooses ", c_choice)
                    print(lose)
                    lives -=1
                if rps == "rock" and c_choice =="scissor":
                    print("the computer chooses ", c_choice)
                    print(win)
                    lives +=1
                    score+=1
                    computer_lives -=1
                #When user chooses scissor
                if rps == "scissor" and c_choice =="scissor":
                    print("the computer chooses ", c_choice)
                    print(draw)
                if rps == "scissor" and c_choice =="paper":
                    print("the computer chooses ", c_choice)
                    print(win)
                    lives +=1
                    score+=1
                    computer_lives -=1
                if rps == "scissor" and c_choice =="rock":
                    print("the computer chooses ", c_choice)
                    print(lose)
                    lives -=1
                #When user chooses paper
                if rps == "paper" and c_choice =="paper":
                    print("the computer chooses ", c_choice)
                    print(draw)
                if rps == "paper" and c_choice =="scissor":
                    print("the computer chooses ", c_choice)
                    print(lose)
                    lives -=1
                if rps == "paper" and c_choice =="rock":
                    print("the computer chooses ", c_choice)
                    print(win)
                    lives +=1
                    score+=1
                    computer_lives -=1
                
                #system or some required info statements
                if rps == "rules":
                    print("#########################################################")
                    print("GAME RULES")
                    print("#########################################################")
                    print("rock beats scissor")
                    print("scissor beats paper")
                    print("paper beats rock")
                    print("#########################################################")
                
                #Main Game logic
                if lives == 0:
                    print("You have reached 0 lives!!! Thanks for playing :)")
                    print("You got ", score, " Points")
                    stop = input("Press enter to exit   ")
                    exit()
                if computer_lives == 0:
                    print("The computer has reached 0 lives!!! Thanks for playing :)")
                    print("You got ", score, " Points")
                    stop = input("Press enter to exit   ")
                    exit()
                #exit
                if rps == "exit":
                    break
        else :
            print("your username or password is incorrect")
            print("#########################################################")
            
