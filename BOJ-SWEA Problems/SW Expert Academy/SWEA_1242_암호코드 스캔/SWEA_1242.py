import sys
sys.stdin = open('input.txt')


# 암호코드
P = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
     '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

# 16진수를 2진수로 변환하기
dict_16_2 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
             '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

# input 값 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_16_mat = [input() for _ in range(N)]
    rlt = 0                                         # 최종 결과를 반환할 rlt 변수를 0으로 생성 (암호코드가 없으면 0 반환)
    rlt_list = []                                   # 유효한 암호코드를 담아줄 rlt_list 라는 빈 리스트 생성

    num_mat = []                                    # 16진수의 암호코드중 필요한 부분만 2진수로 변환하여 담을 num_mat 빈 리스트 생성
    for num_16_list in num_16_mat:                  # for 문을 이용해 암호코드를 조회
        line_16 = ''                                # 각 행별 필요한 부분을 담을 line_16 이라는 빈 스트링 생성
        for num_16 in num_16_list:                  # for 문을 이용해 각 행의 16진수 숫자 원소들을 조회
            if num_16 in dict_16_2:                 # 해당 숫자가 16진수 중 하나인 경우,
                line_16 += dict_16_2[num_16]        # -> line_16 변수에 2진수로 변환한 숫자를 이어 붙이기
        num_mat.append(line_16)                     # num_mat 리스트에 각 행별 추출한 2진수 숫자를 담기

    # for 문을 이용해 행별로 암호코드가 있는지 검사
    for num_list in num_mat:
        idx = 0                                     # 암호코드의 마지막 자리 인덱스 번호를 담을 idx 변수 0으로 생성
        for i in range(len(num_list)-1, -1, -1):    # for 문을 이용해 각 줄의 뒤에서부터 1이 있는지 검사 (암호코드의 마지막 자리)
            if num_list[i] == '1':                  # 1을 찾은 경우,
                idx = i                             # -> idx 변수에 i 값을 저장
                break                               # -> for 문 종료

        if idx > 0:                                     # idx를 찾은 경우,
            code_stack = []                             # 암호코드를 담아줄 code_stack 이라는 빈 스택을 생성
            cnt_1, cnt_2, cnt_3, cnt_4 = 0, 0, 0, 0     # 암호코드의 선이 굵어지는 경우 굵기를 담을 4개의 변수 생성
            for i in range(idx, -1, -1):                # for 문을 이용해 뒤에서부터 암호코드의 굵기를 담기
                if num_list[i] == '1' and cnt_3 == 0:                   # 뒤에서부터 순서대로 1의 개수를 cnt_1에 담고
                    cnt_4 += 1
                elif num_list[i] == '0' and cnt_2 == 0 and cnt_4 > 0:   # 그 다음으로 오는 0의 개수를 cnt_3에 담고
                    cnt_3 += 1
                elif num_list[i] == '1' and cnt_1 == 0 and cnt_3 > 0:   # 그 다음으로 오는 1의 개수를 cnt_2에 담고
                    cnt_2 += 1
                                                                        # 마지막으로 오는 0의 개수를 전체 굵기에 비례할때까지 cnt_4에 담기
                elif (min(cnt_2, cnt_3, cnt_4) != 0) and (cnt_1 + cnt_2 + cnt_3 + cnt_4) / min(cnt_2, cnt_3, cnt_4) != 7:
                    cnt_1 += 1
                    if (min(cnt_2, cnt_3, cnt_4) != 0) and (cnt_1 + cnt_2 + cnt_3 + cnt_4) / min(cnt_2, cnt_3, cnt_4) == 7: # 암호코드가 완성되었다면,
                        d = min(cnt_2, cnt_3, cnt_4)                                                        # -> cnt_1 ~ 3 중 최소값을 변수 d에 담고
                        code_list = [int(cnt_1 / d), int(cnt_2 / d), int(cnt_3 / d), int(cnt_4 / d)]        # -> code_list 라는 리스트에 0,1,0,1 실제개수 넣어주기
                        code = ''                                       # code 라는 빈 스트링을 생성하기
                        for i in range(0, 4, 2):                        # for 문을 이용해 code라는 변수에 실제 숫자코드 (예: '0001011') 만들어서 넣어주기
                            code += str('0') * code_list[i]             # 0의 개수만큼 code 변수에 붙여주기
                            code += str('1') * code_list[i+1]           # 1의 개수만큼 code 변수에 붙여주기
                        code_stack.append(code)                         # code_stack에 실제 숫자코드 쌓기
                        cnt_1, cnt_2, cnt_3, cnt_4 = 0, 0, 0, 0         # cnt_1 ~ 4 변수는 0으로 초기화

            num_code = []                                   # 유효한 암호코드를 십진수로 변경해 저장할 num_code 라는 빈 리스트 생성
            while code_stack:                               # while 문을 이용해 code_stack을 비울때 까지 반복문 진행 
                num_str = code_stack.pop()                  # code_stack의 마지막 숫자코드를 꺼내서 num_str 변수에 저장
                if num_str in P:                            # num_str 이 암호코드 중 하나라면,
                    num_code.append(P[num_str])             # -> 암호코드를 10진수로 변환한 값을 num_code 리스트에 저장

            nc = num_code                                   # 다음 코드의 편의를 위해서 num_code 리스트를 nc 로 명칭 변경
            for n in range(0, len(num_code), 8):                                                            # for 문을 이용해 num_code를 8자리씩 확인
                check_code = ((nc[n]+nc[n+2]+nc[n+4]+nc[n+6]) * 3) + (nc[n+1]+nc[n+3]+nc[n+5]) + nc[n+7]    # 정상적인 코드인지 확인하기 위해 수식 결과를 check_code 변수에 저장
                if check_code % 10 == 0:                                                                    # 정상적인 코드인 경우, (10으로 나누어지는 경우,)
                    curr_rlt = [nc[n], nc[n+1], nc[n+2], nc[n+3], nc[n+4], nc[n+5], nc[n+6], nc[n+7]]       # -> curr_rlt 에 코드 숫자를 리스트 형식으로 저장
                    if curr_rlt not in rlt_list:            # 만약 curr_rlt가 rlt_list에 속해있지 않다면
                        rlt += sum(curr_rlt)                # -> rlt 변수에 curr_rlt의 합을 누적해주기
                        rlt_list.append(curr_rlt)           # -> rlt_list 에 curr_rlt 추가해주기

    # 결과 출력
    print(f'#{tc} {rlt}')