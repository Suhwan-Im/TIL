import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
A, B, C = map(int, input().split())

# 손익분기점 계산하기
if B >= C:
    print(-1)
else:
    n = A // (C - B)
    print(n+1)