#1st Method
def fib (x):
    temp = []
    a = 1
    b = 1
    for i in range (0,x + 1):
        if i < 2:
            temp.append (1)
        if i >= 2:
            c = a + b
            temp.append (c)
            a = b
            b = c
    return temp[x - 1]
n = int(input("Input Fibonacci's Number: "))
print("Result: ",fib(n))


#2nd Method:
def fib (x):
    if x <= 2:
        return 1
    elif x >= 3:
        return fib(x - 1) + fib(x - 2)
print("Result: ", fib(int(input ("Input Fibonacci's Number: "))))