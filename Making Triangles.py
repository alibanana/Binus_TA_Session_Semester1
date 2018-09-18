#Excercise 1, Make a Triangle:
print ("Triangle #1")
height = input("insert height: ")
height = int(height)
for i in range (1,height + 1):
        print ("*" * i)


#Make a triangle 2:
print ("Triangle #2")
height = input("insert height: ")
height = int(height)
for i in range (1, height +1):
    print (" " * (height - i), "*" * i)


#Make a triangle 3:
print ("Triangle #3")
height = input("insert height: ")
height = int(height)
for i in range (1, height +1):
    print ("*" * ((height + 1) - i))


#Make a triangle 4:
print ("Triangle #4")
height = input("insert height: ")
height = int(height)
for i in range (1, height +1):
    print (" " * (i - 1),"*" * ((height + 1) - i))


#Make a triangle 5:
print ("Triangle #5")
height = input("insert height: ")
height = int(height)
for i in range (1, height +1):
    print (" " * (height - i),"* " * i)


#Make a triangle 6:
print ("Triangle #6")
height = input("insert height: ")
height = int(height)
for i in range (1, height +1):
    print (" " * (i - 1),"* " * ((height + 1) - i))


#Make a Diamond:
print ("Diamond")
height = input("insert height: ")
height = int(height)
for i in range(1, height + 1):
    if i < height/2:
        print(" " * (height - i), "* " * i)
    elif i > height/2:
        print (" " * (i - 1),"* " * ((height + 1) - i))


#Make Pyramid using While:
print ("Pyramid using While")
height = input("insert height: ")
height = int(height)
x = 1
y = 1
while x in range (1, height*2) :
    if x < (height*2):
        print (" " * (height - y),"*" * x)
        x = x + 2
        y = y + 1