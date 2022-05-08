import sys
sys.stdin = open('input.txt')


# input값 입력받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    max_rlt = -1e100        # 최대 결과값을 담을 max_rlt 변수를 임의의 적은수로 생성
    if len(A_list) < len(B_list):   # A 숫자열이 더 짧은 경우
        for j in range(len(B_list)-len(A_list)+1):
            rlt = 0         # 구간별 결과값을 담을 rlt 변수를 0으로 생성
            for i in range(len(A_list)):
                rlt += (A_list[i]*B_list[j+i])
            if rlt > max_rlt:
                max_rlt = rlt
    else:                           # B 숫자열이 더 짧거나 같은 경우
        for i in range(len(A_list)-len(B_list)+1):
            rlt = 0
            for j in range(len(B_list)):
                rlt += (B_list[j]*A_list[i+j])
            if rlt > max_rlt:
                max_rlt = rlt

    # 결과 출력
    print(f'#{tc} {max_rlt}')