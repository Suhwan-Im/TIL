import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_list = list(map(int, input().split()))

    # 정류장 개수 길이 + 1의 0 리스트 생성
    stop_list = [0] * (N + 1)
    # 충전기가 있는 정류장과 맨 마지막 정류장은 1로 수정
    for chrg in charge_list:
        stop_list[chrg] = 1
    stop_list[-1] = 1

    # 충전횟수, 현재위치, 고립상황 변수 만들어서 0으로 설정
    charge = 0
    curr_pos = 0
    impossible = 0

    # while문을 이용해 최소 충전횟수 구하기
    while curr_pos < (N-K):
        # K 정류장 만큼 갔을때 충전기가 있는 경우, 현재위치와 충전횟수 갱신
        if stop_list[curr_pos + K] == 1:
            curr_pos += K
            charge += 1
        # K 정류장 만큼 갔을때 충전기가 없는 경우, 인덱스를 1씩 줄여가며 충전기 찾은 후 변수 갱신
        else:
            for i in range(1, K + 1):
                if stop_list[curr_pos + K - i] == 1:
                    curr_pos += (K - i)
                    charge += 1
                    break
                # K 범위이내에 충전기가 없는 경우 impossible 변수 1로 지정
                elif i == (K-1):
                    curr_pos = N
                    impossible = 1
                    break

    # 결과 출력 -- 중간에 고립된 경우 0을 출력, 그 외에는 충전횟수 출력
    if impossible == 1:
        print(f'#{tc} {int(0)}')
    else:
        print(f'#{tc} {charge}')