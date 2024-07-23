import random
answer = random.randint(1,99)
name = input("what is your name? ")
guess = int(input("guess a number"))

while guess != answer:
    if guess > answer:
        print("No,too large!!!")
    else:
        print("No, Too small")
    guess = int(input("guess a number"))
    
print("Yaaaay!!!!",name, "you guessed right!")            