import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N = int(input())
que = deque()

for _ in range(N):
    order = list(map(str, input().split()))
    if order[0] == "push":
        que.append(int(order[1]))
    elif order[0] == "pop":
        if len(que) > 0:
            print(que.popleft())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(que))
    elif order[0] == "empty":
        if len(que) > 0:
            print(0)
        else:
            print(1)
    elif order[0] == "front":
        if len(que) > 0 :
            print(que[0])
        else:
            print(-1)
    elif order[0] == "back":
        if len(que) > 0 :
            print(que[-1])
        else:
            print(-1)