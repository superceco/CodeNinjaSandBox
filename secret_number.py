import random


while True:
    try:
        guess = int(input("Enter number: "))
        secret = 111 #random.randint(1, 999)
        if guess== secret:
            print("Your guess is right and the secrect number is: ", secret)
        else:
            print("Your guess is wrong. Please try again")
    except:
        continue

