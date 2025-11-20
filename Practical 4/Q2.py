import random

while True:
    answer = random.randint(1,2)
    
    guess = int(input("Enter your guess as 1 for a head, 2 for a tail, or 0 to exit: "))
    
    if guess == 0:
        print ("Thank you for playing the game!")
        break
    elif guess == 1 or guess == 2:
        if answer == guess:
            print("Your guess is correct!\n")
        else:
            print("Your guess is incorrect!\n")
    else:
        print("Please enter either 0, 1 or 2 \n")