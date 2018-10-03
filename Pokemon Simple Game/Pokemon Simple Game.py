data = []
player = x = y = 0
#empty_box = "0"
#player = "1"
#grass = "#"

def read():
    file = open("Pokemon_Map.txt", "r")
    for row in file:
        temp = []
        raw = row.split(" ")
        for i in range(0,8):
            if i == 7:
                temp.append(str(int(raw[i])))
            elif i in range(0,7):
                temp.append(raw[i])
        data.append(temp)
    file.close()

def write():
    temp =""
    file = open("Pokemon_Map.txt", "w")
    for i in range (0,8):
        for j in range (0,8):
            if j == 7:
                temp += str(data[i][j]) + "\n"
            elif j in range(0,7):
                temp += str(data[i][j]) + " "
    file.write(temp)
    file.close()

def view():
    for i in range (0,8):
        for j in range (0,8):
            if data[i][j] == "2":
                print("#",end=" ")
            elif data[i][j] == "0" or "1":
                print(data[i][j],end=" ")
        print("")

read()
while True:
    view()
    menu = int(input("Choose an option:\n[1] Up\n[2] Down\n[3] Left\n[4] Right\n[5] Save and Exit\nChoose no [1..5]: "))
    for i in range(0, 8):
        for j in range(0, 8):
            if data[i][j] == "1":
                x = j
                y = i
                player = data[y][x]
    if menu == 1:
        data[y][x] = data[y - 1][x]
        data[y - 1][x] = player
    elif menu == 2:
        data[y][x] = data[y + 1][x]
        data[y + 1][x] = player
    elif menu == 3:
        data[y][x] = data[y][x - 1]
        data[y][x - 1] = player
    elif menu == 4:
        data[y][x] = data[y][x + 1]
        data[y][x + 1] = player
    elif menu == 5:
        write()
        break
    else:
        print("wrong input")