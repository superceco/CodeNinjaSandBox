b = int(input("please insert a number b/n 1 and 100: "))
for number in range(1,b):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3 ==0 and number%5!=0:
        print("fizz")
    elif number%5==0 and number%3!=0:
        print("buzz")
    else:
        print(number)
