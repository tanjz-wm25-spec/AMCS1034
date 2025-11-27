import random

answers = []
guesses = []
outputs = []

while True:
    answer = random.randint(1,2)   # 单次答案（1 或 2）

    guess = input("Enter your guess as 1 for a head, 2 for a tail, or 0 to exit: ")

    if guess.isdigit():
        guess = int(guess)

        if guess < 0 or guess > 2:
            print("Please enter 0, 1, or 2.")
            continue

        if guess == 0:
            print("Thank you for playing the game!")
            break

        # 记录答案与猜测
        answers.append(answer)
        guesses.append(guess)

        if answer == guess:
            print("Correct!\n")
            outputs.append(True)
        else:
            print("Wrong!\n")
            outputs.append(False)

    else:
        print("Please enter 0, 1, or 2.\n")

# 总结
correct = [o for o in outputs if o]
incorrect = [o for o in outputs if not o]

print("RESULTS")
print("-------")
print(f"You have made {len(correct)} correct guesses and {len(incorrect)} incorrect guesses.")

for i in range(len(answers)):
    print(f"Round #{i+1}")
    print("Answer: {}".format("Head" if answers[i] == 1 else "Tail"))
    print("Guess : {}".format("Head" if guesses[i] == 1 else "Tail"))
    print("Result: {}".format("Correct" if outputs[i] else "Wrong"))
    print()