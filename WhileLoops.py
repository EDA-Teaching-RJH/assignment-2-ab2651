### Part Two -- your code goes here. 
import random
number = random.randint(1, 100)
attempt = 0
while attempt != number:
    userGuess = input("Guess my number between 1 and 100: ")
    attempt = int(userGuess)

    if attempt < 1 or attempt > 100:
        print("The number is between 1 and 100. Try again")

    elif attempt > number:
        print("The guess is higher than the number. Try again.")
    
    elif attempt < number:
        print("The guess is lower than the number. Try again.")
else:
    print("Well done you guessed the number", number,"correctly.")

    
    
    



