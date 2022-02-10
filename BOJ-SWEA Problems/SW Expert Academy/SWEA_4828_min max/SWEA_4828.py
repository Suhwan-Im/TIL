import sys
sys.stdin = open('input.txt')


# 최대값 함수 구현
def num_max(lst):
    no_max = -1e100
    for num in lst:
        if num > no_max:
            no_max = num
    return no_max

# 최소값 함수 구현
def num_min(lst):
    no_min = 1e100
    for num in lst:
        if num < no_min:
            no_min = num
    return no_min


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    diff = num_max(num_list) - num_min(num_list)

    # 결과 출력
    print(f'#{tc} {diff}')