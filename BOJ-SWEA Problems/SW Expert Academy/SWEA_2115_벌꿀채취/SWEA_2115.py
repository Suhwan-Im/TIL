import sys
sys.stdin = open('input.txt')


# DFS 함수 정의
def DFS(n, cnt, ssum, lst):
    global sol
    if cnt > C:             # 꿀의 양이 허용범위를 넘은 경우,
        return              # -> DFS 함수 반환
    elif n == M:            # 꿀을 수확한 벌통의 개수가 M 값과 같아졌을때
        if sol < ssum:      # -> 만약 현재 합계가 기존 최대값보다 큰 경우,
            sol = ssum      # -> -> sol 값을 현재 합계로 갱신
        return              # -> DFS 함수 반환
    # DFS 재귀
    DFS(n+1, cnt+lst[n], ssum+lst[n]**2, lst)   # 포함 시키는 경우
    DFS(n+1, cnt, ssum, lst)                    # 포함 시키지 않는 경우

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    ans = 0     # 최댓값을 담을 ans 변수를 0으로 생성

    # 이중 for 문을 이용해 첫번째 일꾼의 꿀통 구하기
    for i1 in range(N):
        for j1 in range(N-M+1):
            sol = 0                                 # 수익을 담을 sol 변수를 0 으로 생성
            DFS(0, 0, 0, num_mat[i1][j1:j1+M])      # DFS(n, cnt, ssum, lst)
            t1 = sol                                # t1에 첫번째 일꾼의 수익 담기
            # 이중 for 문을 이용해 두번째 일꾼의 꿀통 구하기
            for i2 in range(i1, N):
                sj = 0                      # sj 값을 0으로 리셋
                if i1 == i2:                # 만약 첫번째 일꾼과 두번째 일꾼이 같은 줄에서 꿀을 채취할때,
                    sj = j1 + M             # -> sj 값을 첫번째 일꾼의 범위 직후로 지정
                for j2 in range(sj, N-M+1):
                    sol = 0                             # 수익을 담을 sol 변수를 0 으로 생성
                    DFS(0, 0, 0, num_mat[i2][j2:j2+M])  # DFS(n, cnt, ssum, lst)
                    t2 = sol                            # t2에 두번째 일꾼의 수익 담기

                    ans = max(ans, t1+t2)           # 최댓값 갱신 (기존 최댓값 vs 현재 합계)

    # 결과 출력
    print(f'#{tc} {ans}')