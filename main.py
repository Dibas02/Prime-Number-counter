lower = int(input("Enter the lower value: "))
upper = int(input("Enter the upper value: "))
counter = 0


for c in range(lower, upper+1):
    if c >1:
        for i in range (2, c):
            if c%i == 0:
                break
        else:
            
            print(c)