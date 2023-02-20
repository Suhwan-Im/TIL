import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
N_list = list(map(int, input().split()))
N_list = sorted(N_list)
M = int(input())
M_list = list(map(int, input().split()))

for m in M_list:
    start, end = 0, N-1
    while True:
        mid = (start + end) // 2
        if start > end:
            print(0)
            break
        elif m == N_list[mid]:
            print(1)
            break
        elif m > N_list[mid]:
            start = mid + 1
        elif m < N_list[mid]:
            end = mid - 1