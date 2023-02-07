import random

print(" i am thinking of a number between 1 and 20")
secret_number = random.randint(1, 20)
tries = 0
while True:
    if tries == 3:
        print("You lose")
        end2 = input("would you like to try again").lower()
        if end2 == "y" or "yes":
            tries = 0
            secret_number = random.randint(1, 20)
            continue
        elif end2 == "n" or "no":
            break
        else:
            print("I dont understand")
    else:
        guess = int(input("take a guess: "))
        if guess < secret_number:
            print("your guess is too low")
            tries += 1
        elif guess > secret_number:
            print("your number is too high")
            tries += 1
        elif guess == secret_number:
            print("You win!")
            end = input("would yo like to play again?").lower()
            if end == "y" or "yes":
                tries = 0
                secret_number = random.randint(1, 20)
                continue
            elif end == "n" or "no":
                break
            else:
                print("I dont understand")

print("thanks for playing")


