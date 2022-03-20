import sys
sys.stdin = open('input.txt')


# DFS 함수 정의
def DFS(n, ssum):
    global ans

    # 가지치기 (키의 합이 이전의 최소합을 넘은 경우)
    if ssum >= B + ans:
        return

    # 종료 조건 (모든 직원(포합&미포함)을 지난 경우)
    if n == N:
        if ssum >= B and ans > ssum - B:    # 만약 키의 합이 책장보다 높고, 높이차가 현존 최소라면
            ans = ssum - B                  # ans 변수에 현재 높이차를 저장해주기
        return

    DFS(n+1, ssum + num_list[n])    # 포함하는 경우
    DFS(n+1, ssum)                  # 포함하지 않는 경우

# input값 입력받기
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    num_list = list(map(int, input().split()))

    ans = 1e100 # ans 변수를 생성하고 큰 수를 넣기

    # DFS 함수 사용하기
    DFS(0, 0)   # DFS(직원 idx 시작값, 시작 높이의 합)

    # 결과 출력
    print(f'#{tc} {ans}')