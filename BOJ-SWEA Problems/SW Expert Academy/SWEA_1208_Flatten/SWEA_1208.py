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

# dump 함수 구현
def dump(N, lst):
    # while문을 이용해 N번 반복하여 리스트내 최대값에서 1을 빼고 최소값에 1을 더함
    while N > 0:
        lst[lst.index(num_max(lst))] -= 1
        lst[lst.index(num_min(lst))] += 1
        N -= 1

    # 리스트의 최대값과 최소값의 차이를 반환
    diff = num_max(lst) - num_min(lst)
    return diff


# 테스트 케이스 입력 후 함수 활용하여 계산
T = 10
for tc in range(1, T + 1):
    # 입력
    N = int(input())
    list_box = list(map(int, input().split()))

    # 함수를 이용한 계산
    diff = dump(N, list_box)

    # 출력
    print(f'#{tc} {diff}')