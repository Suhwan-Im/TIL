import sys
sys.stdin = open('input.txt')

T = 4
for tc in range(1, T+1):
    Ax, Ay, Ap, Aq, Bx, By, Bp, Bq = map(int, input().split())

    rlt = ''        # 결과를 담을 rlt 변수를 빈 스트링으로 생성

    if Ap < Bx or Aq < By or Bp < Ax or Bq < Ay:
        rlt = 'd'
    elif (Ax == Bp and Ay == Bq) or (Ax == Bp and Aq == By) or (Ap == Bx and Aq == By) or (Ap == Bx and Ay == Bq):
        rlt = 'c'
    elif Ax == Bp or Ay == Bq or Ap == Bx or Aq == By:
        rlt = 'b'
    else:
        rlt = 'a'

    # 결과 출력
    print(f'{rlt}')