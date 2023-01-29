import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
num_list = list(map(int, input().split()))

num = num_list[0]
prev_num = num_list[0]
for i in range(1, 8):
    if num == 1 and num_list[i] > prev_num:
        prev_num = num_list[i]
        if i == 7:
            print("ascending")
    elif num == 8 and num_list[i] < prev_num:
        prev_num = num_list[i]
        if i == 7:
            print("descending")
    else:
        print("mixed")
        break