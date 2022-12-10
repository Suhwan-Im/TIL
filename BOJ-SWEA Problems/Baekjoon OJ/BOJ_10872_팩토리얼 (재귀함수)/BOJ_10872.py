N = 10

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(N))