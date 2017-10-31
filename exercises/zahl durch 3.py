b = int(input("Enter the highest number: "))
sum = 0
for i in range(1,b):
    if i%3 == 0:
        print(i)
        sum = sum + 1
    else:
        continue
print("total number of numbers is:", sum)