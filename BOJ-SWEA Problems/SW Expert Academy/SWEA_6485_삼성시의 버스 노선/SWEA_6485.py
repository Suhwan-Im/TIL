import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus_list = [list(map(int, input().split())) for _ in range(N)]

    P = int(input())
    P_list = [int(input()) for _ in range(P)]

    # 5000개의 정류장을 가진 bus_stops라는 빈 리스트 생성
    bus_stops = [0] * 5000

    for i in range(N):
        for j in range(bus_list[i][0] - 1, bus_list[i][1]):
            bus_stops[j] += 1

    # 출력을 위한 rlt_list라는 빈 리스트 생성
    rlt_list = [0] * P
    for i in range(P):
        rlt_list[i] = bus_stops[P_list[i] - 1]

    # 결과 출력
    print(f'#{tc}', *rlt_list[:])