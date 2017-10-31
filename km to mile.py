print("Hello Human my name is MileKill and I will convert "
      "killometers into miles for you")

while True:
    try:
        kilometer = float(input("Please Human enter the kilometers as number: "))
        miles = 1 / 1.609344
        print(kilometer, "km", "are ", kilometer * miles, "miles")
        break
    except:
        print("Enter correct value")
        continue
