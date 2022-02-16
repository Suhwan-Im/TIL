import sys
sys.stdin = open('input.txt')


# num_count 함수 정의
def num_count(lst):
    cnt_0, cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, cnt_6, cnt_7, cnt_8, cnt_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # for문을 이용해 숫자별 개수 누적
    for num_str in lst:
        if num_str == "ZRO":
            cnt_0 += 1
        elif num_str == "ONE":
            cnt_1 += 1
        elif num_str == "TWO":
            cnt_2 += 1
        elif num_str == "THR":
            cnt_3 += 1
        elif num_str == "FOR":
            cnt_4 += 1
        elif num_str == "FIV":
            cnt_5 += 1
        elif num_str == "SIX":
            cnt_6 += 1
        elif num_str == "SVN":
            cnt_7 += 1
        elif num_str == "EGT":
            cnt_8 += 1
        elif num_str == "NIN":
            cnt_9 += 1
        else:
            pass

    # 숫자별 누적 개수를 리스트 형식으로 반환
    cnt_list = [cnt_0, cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, cnt_6, cnt_7, cnt_8, cnt_9]
    return cnt_list


# 테스트 케이스를 통한 코드 실행
T = int(input())
for tc in range(1, T + 1):
    N = input()
    num_list = list(map(str, input().split()))

    # num_count함수를 이용해 계산하기
    c = num_count(num_list)

    # 결과 출력
    print(f'#{tc}')
    print("ZRO" + " ZRO"*(c[0]-1) + " ONE"*c[1] + " TWO"*c[2] + " THR"*c[3] + " FOR"*c[4] + " FIV"*c[5] + " SIX"*c[6] + " SVN"*c[7] + " EGT"*c[8] + " NIN"*c[9])