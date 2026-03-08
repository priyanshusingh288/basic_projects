import random

low = 1
high = 100
response = random.randint(low,high)
guesses = 0
is_running = True

print("===================================")
print("python number gussing game:]")
print(f"enter the number between {low} and {high};")

while is_running:

    guess = input("enter your guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if guess < low or guess>high:
            print("please enter the number between the given range:(")
        elif guess<response:
            print("too low!🥲 please try again")
        elif guess>response:
            print("too high!🤦‍♂️ please try again")
        else:
            print(f"CORRECT 🥴🤤 the answer was:{response}")
            print(f"the number of guesses you took were :{guesses}")
            is_running = False
    else:
        print("invalid guess or input")
        print(f"enter the number between {low} and {high};")
