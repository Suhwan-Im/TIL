import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 2, 3, 5, 7, 11의 제곱횟수를 담을 squares 리스트 생성
    squares = [0, 0, 0, 0, 0]

    # while문을 이용해 소인수분해 하기
    while N > 1:
        if N % 11 == 0:
            squares[4] += 1
            N //= 11
        elif N % 7 == 0:
            squares[3] += 1
            N //= 7
        elif N % 5 == 0:
            squares[2] += 1
            N //= 5
        elif N % 3 == 0:
            squares[1] += 1
            N //= 3
        elif N % 2 == 0:
            squares[0] += 1
            N //= 2

    # 결과 출력
    print(f'#{tc}', *squares[:])