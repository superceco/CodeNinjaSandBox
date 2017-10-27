# this my calculator
print("Hello human!")
print("I am your calculator")
print("Let's do some math \n")
while True:
        try:
            number1 = float(input("\nEnter the first number: ")) # using floating point numbers not only integers
            number2 = float(input("Enter the second number: ")) # using floating point numbers not only integers
        except:
            print("That is not a number!")
            continue

        operator = input("Enter an operator \nvalid operators are\n+ for addition,\n- for substraction,\n* for multiplication\n/ for division\n : ")

        #Check if user operator is a valid one
        if operator == "+":
            print(number1, operator, number2, "=", number1 + number2)
        elif operator == "-":
            print(number1, operator, number2, "=", number1 - number2)
        elif operator == "*":
            print(number1, operator, number2, "=", number1 * number2)
        elif operator == "/":
            print(number1, operator, number2, "=", number1 / number2)
        else:
            print("Invalid operator!") # if the operator does not have the +,-,*, / then there must be an error
            continue

