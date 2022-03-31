import sys
sys.stdin = open('input.txt')


# DFS 함수 정의
def DFS(s, n):
    global min_n
    if n >= min_n:      # n 값이 현재 최소 교환횟수보다 크면
        return          # -> DFS 함수 반환 (백트래킹)
    elif s >= N:        # n 값이 min_n값보다 작은 상태에서, 시작 인덱스가 정류장 종점이거나 이미 넘었으면
        min_n = n       # -> 현재의 n값을 min_n 변수에 갱신
        return          # -> DFS 함수 반환
    for i in range(bat_list[s-1], 0, -1):   # for 문을 이용해 충전지의 숫자 범위의 경우의수를 DFS 함수에 갱신
        DFS(s+i, n+1)                       # DFS(시작 인덱스 + 이동거리, 충전횟수 + 1)

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    N = num_list[0]                     # 정류장 개수
    bat_list = num_list[1:] + [0]       # 정류장별 배터리 용량 리스트

    min_n = 1e100   # 배터리 최소 교환횟수를 담을 min_n 변수를 큰수로 생성
    DFS(1, -1)      # DFS 함수 이용해서 배터리 최소 교환횟수 구하기
                    # DFS(시작 인덱스, 충전횟수)  <-- 충전횟수를 -1로 시작하는 것은 출발지에서 배터리 장착은 포함시키지 않기 때문

    # 결과 출력
    print(f'#{tc} {min_n}')