import sys
sys.stdin = open('input.txt')


# input값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    s, e = 1, N # 시작값과 끝값을 의미하는 s와 e 변수를 1과 N으로 생성
    ans = -1    # ans 변수에 -1 저장 (세제곱 정답을 못 찾을 경우 -1 반환)

    # while 문을 이용해 정답 찾기
    while s <= e:
        m = (s+e) // 2
        if m**3 == N:       # m 의 세제곱이 N 일때,
            ans = m         # -> ans 변수에 m 값 담기
            break           # -> 반복문 종료
        elif m**3 < N:      # m 의 세제곱이 N 보다 작을때,
            s = m + 1       # -> 시작값인 s 변수를 m+1 로 지정
        else:               # m 의 세제곱이 N 보다 클때,
            e = m - 1       # -> 끝값인 e 변수를 m-1 로 지정

    # 결과 출력
    print(f'#{tc} {ans}')