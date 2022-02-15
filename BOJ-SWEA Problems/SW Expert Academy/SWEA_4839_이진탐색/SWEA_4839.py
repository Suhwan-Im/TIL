import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    P, P_A, P_B = map(int, input().split())

    # A학생의 탐색 수 구하기
    cnt_A = 1
    l, r = 1, P
    c = int((l + r) / 2)
    while c != P_A:
        cnt_A += 1
        if P_A > c:
            l = c
        elif P_A < c:
            r = c
        c = int((l + r) / 2)


    # B학생의 탐색 수 구하기
    cnt_B = 1
    l, r = 1, P
    c = int((l + r) / 2)
    while c != P_B:
        cnt_B += 1
        if P_B > c:
            l = c
        elif P_B < c:
            r = c
        c = int((l + r) / 2)


    # A학생과 B학생의 탐색수 비교하여 이긴사람 반환하기 (0: 무승부)
    if cnt_A < cnt_B:
        winner = "A"
    elif cnt_B < cnt_A:
        winner = "B"
    else:
        winner = 0

    # 결과 출력
    print(f'#{tc} {winner}')