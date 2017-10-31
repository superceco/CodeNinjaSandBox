print("Hello Human my name is MileKill and I will convert "
      "killometers into miles for you")

while True:
    try:
        kilometer = float(input("Enter the kilometers: "))
        miles = 1 / 1.6093440
        print(kilometer, "km", "are ", kilometer * miles, "miles")
        break
    except:
        print("Enter correct value")
        continue

