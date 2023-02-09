import sys
sys.stdin = open('input.txt')

from collections import deque

# input 값 입력 받기
N = int(input())
cards = deque(i for i in range(1, N+1))

while len(cards) > 2:
    cards.popleft()
    cards.append(cards.popleft())

# 결과 출력
print(cards[-1])