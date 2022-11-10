import sys
sys.stdin = open('input.txt')

N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]
num_list = sorted(num_list)             # 기둥 리스트 정순으로 정렬

col_highest = 0     # 가장 높은 첫번째 기둥의 x좌표
max_height = 0      # 가장 높은 기둥의 높이
for nums in num_list:
    if nums[1] > max_height:
        col_highest = nums[0]
        max_height = nums[1]

area = 0            # 정답을 담을 area 변수를 0으로 생성

# 큰기둥 기준으로 왼쪽 구역
curr_y = 0
for x, y in num_list:
    if x < col_highest and y > curr_y:
        area += (col_highest - x) * (y - curr_y)
        curr_y = y
    elif x == col_highest:
        break

# 큰기둥 기준으로 오른쪽 구역
num_list = sorted(num_list, reverse=True)   # 기둥 리스트 역순으로 정렬
curr_y = 0
for x, y in num_list:
    if x > col_highest and curr_y < y < max_height:
        area += (x + 1 - col_highest) * (y - curr_y)
        curr_y = y
    # 큰기둥 더해주기 (큰기둥이 복수개인 경우의 넓이 포함)
    elif y == max_height:
        area += (x + 1 - col_highest) * (max_height - curr_y)
        break

print(area)