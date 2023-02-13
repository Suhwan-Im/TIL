import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
min_generator = N

for num in range(N, 0, -1):
    total = num
    for n in str(num):
        total += int(n)

    if N == total:
        min_generator = num

# 결과 출력
if min_generator == N:
    print(0)
else:
    print(min_generator)