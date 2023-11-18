# Factorial of a number
def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))
x = 3
print(f"the factorial of a number {x} is {factorial(x)}")