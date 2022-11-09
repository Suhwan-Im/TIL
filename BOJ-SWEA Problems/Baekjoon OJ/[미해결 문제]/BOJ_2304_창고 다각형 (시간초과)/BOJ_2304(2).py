import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]
num_list = sorted(num_list)

col_highest = 0
max_height = 0
for nums in num_list:
    if nums[1] > max_height:
        col_highest = nums[0]
        max_height = nums[1]

area = 0
curr_y = 0
for x, y in num_list:
    if x < col_highest and y < max_height:
        area += (col_highest - x) * y
        curr_y = y

print(num_list)

# 푸는중...