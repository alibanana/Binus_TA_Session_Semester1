def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Insert Number: "))
print("Result: ",factorial(number))