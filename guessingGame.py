import random
number= random.randint(1,9)
chances=0
while chances<5:
    guess= int(input ("Guess a number from 1 to 9 (including 1 and 9.)"))
    chances=chances + 1
    if (guess==number):
       print("Congratulations! You have guessed the number!")
    elif (guess<number):
        print("Your guess was too low!")
    else :
        print("Your guess was too high!")

if not chances <5:
    print("You Lose!! The number is", number)