import sys
sys.stdin = open('input.txt')


# 이진 코드
P = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

# input 값 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_mat = [list(map(int, input())) for _ in range(N)]

    # for 문을 이용해 행별로 암호코드가 있는지 검사
    for num_list in num_mat:
        idx = 0                                     # 암호코드의 마지막 자리 인덱스 번호를 담을 idx 변수 0으로 생성
        for i in range(len(num_list)-1, -1, -1):    # for 문을 이용해 각 줄의 뒤에서부터 1이 있는지 검사 (암호코드의 마지막 자리)
            if num_list[i] == 1:                    # 1을 찾은 경우,
                idx = i                             # -> idx 변수에 i 값을 저장
                break                               # -> for 문 종료

        if idx > 0:                                 # idx를 찾은 경우,
            code = []                               # 코드를 담을 code 라는 빈 리스트 생성
            for i in range(idx-55, idx, 7):         # for 문을 이용해 8개의 7자리 숫자 코드 구분하기
                sub_code = str(num_list[i]) + str(num_list[i+1]) + str(num_list[i+2]) + str(num_list[i+3]) + str(num_list[i+4]) + str(num_list[i+5]) + str(num_list[i+6])
                code.append(sub_code)               # 각각의 숫자 코드를 code 리스트에 저장하기

            num_code = []                           # 숫자 코드를 십진법으로 변환한 숫자를 담을 num_code 라는 빈 리스트 생성
            for num_str in code:                    # for 문을 이용해 8개의 숫자 코드를 0~9의 이진 숫자와 대조
                if num_str in P:                    # 숫자 코드가 0~9 사이의 이진코드와 일치할 경우,
                    num_code.append(P[num_str])     # -> 십진법으로 변환한 숫자를 num_code 리스트에 담기

            rlt = 0                                 # 결과 값을 담을 rlt 변수 0으로 생성 (코드가 없는 경우 0을 반환)
            nc = num_code                           # 다음 코드의 편의를 위해서 num_code 리스트를 nc 로 명칭 변경
            check_code = ((nc[0]+nc[2]+nc[4]+nc[6]) * 3) + (nc[1]+nc[3]+nc[5]) + nc[7]  # 정상적인 코드인지 확인하기 위해 수식 결과를 check_code 변수에 저장
            if check_code % 10 == 0:                # 정상적인 코드인 경우, (10으로 나누어지는 경우,)
                rlt = sum(num_code)                 # -> rlt 변수에 코드 숫자의 합을 저장

    # 결과 출력
    print(f'#{tc} {rlt}')