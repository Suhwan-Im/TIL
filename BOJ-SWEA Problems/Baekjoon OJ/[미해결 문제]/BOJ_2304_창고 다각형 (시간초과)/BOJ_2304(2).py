import sys
sys.stdin = open('input.txt')


N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]

max_height = 0
col_highest = 0
min_col = 1000
max_col = 0
for nums in num_list:
    if nums[1] > max_height:
        max_height = nums[1]
        col_highest = nums[0]
    if nums[0] < min_col:
        min_col = nums[0]
    if nums[0] > max_col:
        max_col = nums[0]

print(col_highest, min_col, max_col)

# 푸는중...