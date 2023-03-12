import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N = int(input())
num_list = [int(input()) for _ in range(N)]
num_list = sorted(num_list)

# 평균값
n_mean = round(sum(num_list) / N)

# 중앙값
n_median = num_list[N//2]

# 최빈값
dict_mode = {}
for num in num_list:
    if num not in dict_mode:
        dict_mode[num] = 1
    else:
        dict_mode[num] += 1

max_count = 0
for num, count in dict_mode.items():
    if count > max_count:
        max_count = count

times = 0
for num, count in dict_mode.items():
    if count == max_count:
        n_mode = num
        times += 1
        if times == 2:
            break

# 범위
n_range = num_list[-1] - num_list[0]

# 정답 출력
print(n_mean)
print(n_median)
print(n_mode)
print(n_range)