secret = 111
correct = False

while correct==False:
    guess =int(input("Enter number: "))

    if guess == secret:
        print("right")
        correct = True
    else:
        print("wrong")