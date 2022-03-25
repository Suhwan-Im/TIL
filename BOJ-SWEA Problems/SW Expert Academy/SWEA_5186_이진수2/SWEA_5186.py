import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = float(input())
    N = int(N * 1e12)

    num_2 = ''                      # 2진수 결과값을 누적할 num_2라는 빈 변수 생성
    # for 문을 이용해 2진수로 변환하기
    for i in range(-1, -14, -1):
        calc = int((2**i) * 1e12)   # 2의 -n승을 calc 변수에 저장
        if N == 0:                  # N 값이 0인 경우
            break                   # -> 반복문 종료
        elif calc <= N:             # calc 값이 N 값보다 작거나 같을 때
            N -= calc               # -> N 값에서 calc 값 빼주기
            num_2 += str('1')       # -> num_2 변수에 2진수 '1' 누적
        else:                       # 그 외의 경우
            num_2 += str('0')       # -> num_2 변수에 2진수 '0' 누적

    if len(num_2) > 12:             # 만약 2진수값이 12자리를 초과했다면,
        num_2 = 'overflow'          # num_2 변수의 값을 'overflow'로 바꿔주기

    # 결과 출력
    print(f'#{tc} {num_2}')