#2nd Method:
def fib (x):
    if x <= 2:
        return 1
    elif x >= 3:
        return fib(x - 1) + fib(x - 2)
print("Result: ", fib(int(input ("Input Fibonacci's Number: "))))