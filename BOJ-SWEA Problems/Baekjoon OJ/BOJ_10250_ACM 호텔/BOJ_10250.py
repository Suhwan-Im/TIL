import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
T = int(input())

# for문을 이용해 각 케이스별 정답 구하기
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H   # 층수 구하기
    if floor == 0:      # 꼭대기 층인 경우
        floor = H
        room = N // H
    else:               # 그 외의 경우
        room = N // H + 1

    if room < 10:       # 호실이 10 미만인 경우 숫자 0을 앞에 넣기
        room = "0" + str(room)

    # 결과 출력
    print(int(str(floor) + str(room)))