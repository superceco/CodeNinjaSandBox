import random

secret = random.randint(1, 999)
#print(secret)
#guess = int(input("Enter an integer from 1 to 999: "))
while guess != secret:
    try:
        guess = int(input("Enter an integer from 1 to 999: "))

        if guess == secret:
            print("Your guess is right and the secrect number is: ", secret)
            break
        else:
            print("Your guess is wrong. Please try again")
            answer = input('Do you want to continue? Y/N:')
            if answer.lower().startswith("y"):
                print("ok, carry on then")
            elif answer.lower().startswith("n"):
                print("ok, sayonnara")
                exit()
            else:
                print("Y/N")
                answer = input('Do you want to continue? Y/N:')
            continue

    except:
        print("invalid number")
        answer = input('Do you want to continue?: Y/N')
        if answer.lower().startswith("y"):
            print("ok, carry on then")
        elif answer.lower().startswith("n"):
            print("ok, sayonnara")
            exit()
        else:
            print("Y/N")
            exit()
        continue



