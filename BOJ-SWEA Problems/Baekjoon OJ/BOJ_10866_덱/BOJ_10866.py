import sys
from collections import deque
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(sys.stdin.readline())
deck = deque()

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push_front':
        deck.insert(0, int(order[1]))
    elif order[0] == 'push_back':
        deck.append(int(order[1]))
    elif order[0] == 'pop_front':
        if len(deck) > 0:
            num = deck.popleft()
            print(num)
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if len(deck) > 0:
            num = deck.pop()
            print(num)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(deck))
    elif order[0] == 'empty':
        if len(deck) > 0:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(deck) > 0:
            print(deck[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(deck) > 0:
            print(deck[-1])
        else:
            print(-1)