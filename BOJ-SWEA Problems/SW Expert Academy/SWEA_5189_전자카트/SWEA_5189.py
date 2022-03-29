import sys
sys.stdin = open('input.txt')


# 순열을 구하는 perm 함수 정의
def perm(n, k):
    if n == k:
        tmp = [1] + p + [1]     # 순열 앞 뒤에 사무실 번호 1번 넣어주기
        p_list.append(tmp)
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    # 관리구역 리스트와 순열 구하기
    area_list = [n for n in range(2, N+1)]    # 관리구역을 순서대로 나열하기
    p = area_list     # 순열 함수내에서 변수명을 간략하게 하기위해 area_list를 p에 저장
    p_list = []         # 순열을 담을 리스트 생성
    perm(0, len(p))     # 순열 함수를 이용해 순열 구하기

    # for 문을 이용해 각 경로의 배터리 소비량 구하기
    bat_min = 1e100                                     # 최소 배터리 소비량을 저장할 bat_min 변수를 큰수로 생성
    for pat in p_list:                                  # for 문을 이용해 각 패턴을 가져오기
        bat_sum = 0                                     # 해당 패턴의 배터리 소비량을 저장할 bat_sum 변수를 0으로 생성
        for i in range(len(pat) - 1):                   # for 문을 이용해 해당 패턴의 배터리 소비량 누적하기
            bat_sum += num_mat[pat[i]-1][pat[i+1]-1]    # 해당 패턴의 인덱스와 배터리 소비 표의 인덱스를 대조해 사용량을 bat_sum 변수에 누적하기
        if bat_sum < bat_min:                           # 만약 해당 패턴의 배터리 소모량이 현존 최소값인 경우,
            bat_min = bat_sum                           # -> bat_min 값을 현재 배터리 소모량 (bat_sum)으로 갱신

    # 결과 출력
    print(f'#{tc} {bat_min}')