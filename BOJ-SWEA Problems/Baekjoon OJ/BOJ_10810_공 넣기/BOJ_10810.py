import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N, M = map(int, input().split())
baskets = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        baskets[x] = k

# 결과 출력
print(*baskets[:])