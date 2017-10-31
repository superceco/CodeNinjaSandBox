'''secret = 111
correct = False
tries = 5

while correct==False:
    guess =int(input("Enter number: "))
    tries = tries -1

    if guess == secret:
        print("right")
        correct = True
    else:
        print("wrong")
    if tries == 0:
        print("no more tries")
        break
'''

secret = 111
for i in range(0,5):
    guess = int(input("Enter number: "))
    if guess == secret:
        print("right")


        break
    else:
        print("wrong")
