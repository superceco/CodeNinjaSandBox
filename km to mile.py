while True:
    try:
        kilometer = float(input("Enter the kilometers: "))
        miles= 1/1.6
        print( kilometer ,"km" ,"are ", kilometer*miles, "miles")
        break
    except:
        print("Enter correct value")
        continue
