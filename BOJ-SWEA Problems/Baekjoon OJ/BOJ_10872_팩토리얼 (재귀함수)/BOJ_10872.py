N = 10

# 재귀함수를 이용한 팩토리얼 함수
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(N))