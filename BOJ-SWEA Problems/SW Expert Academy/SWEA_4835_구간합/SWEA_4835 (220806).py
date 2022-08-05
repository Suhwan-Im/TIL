import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    n_min = 1e100     # 최소값을 담을 n_min 변수를 임의의 큰 수로 생성
    n_max = -1e100    # 최댓값을 담을 n_max 변수를 임의의 작은 수로 생성

    for i in range(N-M+1):
        num_total = 0   # 구간합을 담을 num_total 변수를 0으로 생성
        for j in range(M):
            num_total += num_list[i+j]

        if num_total < n_min:
            n_min = num_total
        if num_total > n_max:
            n_max = num_total

    rlt = n_max - n_min


    print(f'#{tc} {rlt}')