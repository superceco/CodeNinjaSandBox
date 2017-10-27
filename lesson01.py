a = int(input("Bitte Zahl a: "))
b = int(input("Bitte Zahl b: "))
operation = input("+ oder - : ")
if operation == "+":
    print(eval(a + b))
elif operation =="-":
    print(a - b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)
else:
    print(" so geht es nicht")