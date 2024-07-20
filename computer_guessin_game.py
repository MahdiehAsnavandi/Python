import random
guess = random.randint(1, 99)
print(guess)
answer = input("is this the number? ")

while answer != "c":
    if answer == "l":
        print("NO!, pick a smaller number")
        guess = random.randint(1, guess)
        print(guess)
        answer = input("is this the number? ")
    elif answer == "s":
        print("NO, pick a larger number")
        guess = random.randint(guess, 99)
        print(guess)
        answer = input("is this the number? ")
    

print("yeeees! that is CORRECT!!!")