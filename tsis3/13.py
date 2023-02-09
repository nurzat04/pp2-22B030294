import random

cnt = 0

print("Hello! What is your name?")
name = input()
number = random.randint(1, 20)

print("Well, " + str(name) + ", I am thinking of a number between 1 and 20.")

while cnt < 20:
    print("Take a guess.")
    ans = int(input())
    cnt += 1

    if ans < number:
        print("Your guess is too low.")
    elif ans > number:
        print("Your guess is too high.")
    elif ans == number:
        print("Good job, " + str(name) + "! You guessed my number in " + str(cnt) + " guesses!")
        break