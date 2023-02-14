import sys
sys.stdin = open('input.txt')

while True:
    num_list = list(map(int, input().split()))
    nums = sorted(num_list)
    A, B, C = nums[0], nums[1], nums[2]
    if (A == 0) and (B == 0) and (C == 0):
        break
    elif (A**2 + B**2) == (C**2):
        print('right')
    else:
        print('wrong')