import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    order = str(input().rstrip())
    order = order.replace('RR', '')
    n = int(input().rstrip())
    if n > 0:
        nums = deque(list(map(int, input().rstrip()[1:-1].split(','))))
    else:
        nothing = input().rstrip()
        nums = deque()

    direction = 1       # 방향

    for o in order:
        if o == 'R':
            direction *= -1
        if o == 'D':
            if len(nums) > 0:
                if direction == 1:
                    nums.popleft()
                elif direction == -1:
                    nums.pop()
            else:
                nums = 'error'
                break

    if nums == 'error':
        print(nums)
    elif direction == 1:
        print(str(list(nums)).replace(' ',''))
    elif direction == -1:
        nums.reverse()
        print(str(list(nums)).replace(' ',''))
