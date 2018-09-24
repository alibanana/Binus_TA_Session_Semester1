n = int(input("Isnert Height: "))
disp = []
space = str(n*3)

for _ in range(n):
    disp.append(1)
    print(" " * (n - _),end="")
    for i in range (0,_):
        print(disp[i],end=" ")

    temp = [1]
    for i in range(len(disp)-1):
        temp.append(disp[i] + disp[i+1])
    disp = temp

    print ("1")