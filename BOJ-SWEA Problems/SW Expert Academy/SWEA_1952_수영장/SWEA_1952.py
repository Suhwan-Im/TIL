import sys
sys.stdin = open('input.txt')


# DFS 함수 정의
def DFS(mon, cost):
    global ans
    if mon > 12:            # 월이 12가 넘는경우
        if ans > cost:      # 현재 누적값이 ans 값보다 작을때
            ans = cost      # -> ans 변수에 현재 누적값 갱신
        return
    # 일일권
    DFS(mon+1, cost+(price_list[0]*month_cnt[mon])) # DFS(다음달, 누적값+(일일권가격*이번달 이용횟수))
    # 월간권
    DFS(mon+1, cost+price_list[1])                  # DFS(다음달, 누적값+월간권 가격)
    # 3개월권
    DFS(mon+3, cost+price_list[2])                  # DFS(3달후, 누적값+3개월권 가격)
    # 년간권
    DFS(mon+12, cost+price_list[3])                 # DFS(12달후, 누적값+년간권 가격)

# input 값 입력 받기
T = int(input())
for tc in range(1, T+1):
    price_list = list(map(int, input().split()))
    month_cnt = [0] + list(map(int, input().split())) # 월을 인덱스로 접근하기 위해 앞에 [0] 넣어주기

    ans = 1e100     # 최저값을 담을 ans 변수를 큰수로 생성
    DFS(1, 0)       # DFS 함수 이용 (월, 누적값)

    # 결과 출력
    print(f'#{tc} {ans}')