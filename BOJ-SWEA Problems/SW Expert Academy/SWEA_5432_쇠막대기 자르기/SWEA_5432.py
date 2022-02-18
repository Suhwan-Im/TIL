import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    code_list = list(map(str, input()))
    code_list += ['0']          # 리스트 맨 마지막에 '0' 추가

    # 변수 설정
    curr_stick = 0      # 현재 막대기 층수
    tot_piece = 0       # 레이저 직전에 잘려진 막대기 수
    i = 0               # idx 숫자

    # while문을 이용해 쇠막대기 개수 누적해 나가기
    while i <= (len(code_list) - 1):
        if code_list[i] == '0':         # 리스트 마지막에 도달하면 while문 종료
            break
        elif code_list[i] == '(' and code_list[i + 1] == ')':   # 레이저를 만난 경우 (막대기 층수를 총수에 누적)
            tot_piece += curr_stick
            i += 2
        elif code_list[i] == '(':       # 막대기 시작 부분 (막대기 층수 1 증가)
            curr_stick += 1
            i += 1
        elif code_list[i] == ')':       # 막대기 끝 부분 (막대기 층수 1 감소 / 총 막대기수 1 증가)
            curr_stick -= 1
            tot_piece += 1
            i += 1

    # 결과 출력
    print(f'#{tc} {tot_piece}')