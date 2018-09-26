#Initial Conditions
x = 1
Top = {}
Mid = {}
Bottom = {}
Max = 15

#Functions
def choose_place(n):
    if n == 1:
        return Top
    elif n == 2:
        return Mid
    elif n == 3:
        return Bottom
def calculate_value(n):
    total_value = sum(choose_place(n).values())
    return total_value
def view (n):
    if n == "fridge":
        print("                                      MY LOVELY FRIDGE")
        print("")
        print("||=======================================================================================||")
        print("                                        ::::TOP::::")
        print(Top)
        print("")
        print("||---------------------------------------------------------------------------------------||")
        print("                                        ::::MID::::")
        print(Mid)
        print("")
        print("||---------------------------------------------------------------------------------------||")
        print("                                        :::BOTTOM:::")
        print(Bottom)
        print("")
        print("||=======================================================================================||")
    if n == "wrong spelling":
        print("")
        print("Whoops... Wrong Spelling")
        print("")
print("")


#USER INTERFACE
while x < x + 1:
    print("")
    print("***********************************")
    print(" --- WELCOME TO YOUR FRIDGE..! ---")
    print("")
    start1 = input ("      Type 'start' to Start\n   Or 'exit' to close program.\n   Don't forget to press Enter!\n \n***********************************\n")
    print("***********************************")
    # MASTER MENU
    if start1 == "start":
        start = int(input("What do you wish to do?:\n[1] Put item\n[2] Take item\n[3] Check entire Fridge\n[4] Change Item Location\nChoose No: "))
        print("***********************************")

        # PUT ITEM
        if start == 1:
            print("")
            item = input("ITEM: \nWhat kind of item is that?: ")
            print("***********************************")
            print("")

            amount = int(input("Select your amount: "))
            print("***********************************")
            print("")

            place = int(input("Where would you like to put it?\n[1] Top\n[2] Middle\n[3] Bottom\nChoose No: "))
            print("***********************************")

            if item in choose_place(place):
                choose_place(place)[item] = choose_place(place)[item] + amount
            else:
                choose_place(place)[item] = amount
            print("")
            print("            ::::::::::")
            print("               DONE!")
            print("            ::::::::::")

            if calculate_value(1) > Max:
                print("")
                print("      --- Fridge is full! ---")
                print("     What's with your egoism..?")
                print("")
                choose_place(place)[item] = choose_place(place)[item] - (amount - Max)

        # TAKE ITEM
        if start == 2:
            if (calculate_value(1) + calculate_value(2) + calculate_value(3)) != 0:
                print("")
                view("fridge")
                place = int(input(
                    "From which segment would you like to take the item?\n[1] Top\n[2] Middle\n[3] Bottom\nChoose No: "))
                print("***********************************")
                print("")
                if calculate_value(place) != 0:
                    item = input("ITEM SELECTION: \nWhat's the name of the item?: ")
                    print("***********************************")
                    print("")

                    amount = int(input("Insert the amount to take out: \nDon't be greedy!"))
                    print("***********************************")

                    if item in choose_place(place):
                        if amount < choose_place(place)[item]:
                            choose_place(place)[item] = choose_place(place)[item] - amount
                        elif amount >= choose_place(place)[item]:
                            print("There's only", choose_place(place)[item], "left")
                            choose_place(place).pop(item)
                        print("")
                        print("          ::::::::::")
                        print("         ITEM REMOVED")
                        print("          ::::::::::")
                        print("")
                        print("    So sad to see you go... :( ")
                    else:
                        print("")
                        print("PRANKED!!", item, "is NOT in the fridge :( ")
                else:
                    print("No item here")
            else:
                print("No Item in Fridge")
        # CHECK FRIDGE

        if start == 3:
            view("fridge")

        # CHANGE ITEM LOCATION
        if start == 4:
            if (calculate_value(1) + calculate_value(2) + calculate_value(3)) != 0:
                print("")
                view("fridge")
                place = int(input(
                    "From which segment would you like to take the item?\n[1] Top\n[2] Middle\n[3] Bottom\nChoose No: "))
                place2 = int(input("Where would you like to put it?\n[1] Top\n[2] Middle\n[3] Bottom\nChoose No: "))
                print("***********************************")
                print("")
                if calculate_value(place) != 0:
                    item = input("ITEM SELECTION: \nWhat's the name of the item?: ")
                    print("***********************************")
                    print("")

                    amount = int(input("Insert the amount to take out: \nDon't be greedy!"))
                    print("***********************************")

                    if item in choose_place(place):
                        if amount < choose_place(place)[item]:
                            choose_place(place)[item] = choose_place(place)[item] - amount
                        elif amount >= choose_place(place)[item]:
                            print("There's only", choose_place(place)[item], "left")
                            choose_place(place).pop(item)
                        print("")
                        print("          ::::::::::")
                        print("         ITEM REMOVED")
                        print("          ::::::::::")
                        print("")
                        print("    So sad to see you go... :( ")
                    else:
                        print("")
                        print("PRANKED!!", item, "is NOT in the fridge :( ")

                else:
                    print("No item here")
            else:
                print("No Item in Fridge")
            if item in choose_place(place2):
                choose_place(place2)[item] = choose_place(place2)[item] + amount
            else:
                choose_place(place2)[item] = amount
            print("")
            print("            ::::::::::")
            print("               DONE!")
            print("            ::::::::::")
            if calculate_value(1) > Max:
                print("")
                print("      --- Fridge is full! ---")
                print("     What's with your egoism..?")
                print("")
                choose_place(place2)[item] = choose_place(place2)[item] - (amount - Max)
    # SAYING GOODBYE
    elif start1 == "exit":
        print("")
        print("Farewell... We'll miss you :)")
        break

    else:
        view("wrong spelling")