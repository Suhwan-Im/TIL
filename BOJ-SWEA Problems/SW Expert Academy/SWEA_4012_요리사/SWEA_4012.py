import sys
sys.stdin = open('input.txt')


# DFS 함수 정의하기
def DFS(n, a_list, b_list):
    global ans
    if n == N:  # DFS가 N개의 깊이까지 도달했을때,
        if len(a_list) == len(b_list):  # a_list와 b_list가 같은 개수를 나눠갖은 경우에만
            asum = bsum = 0             # asum 변수와 bsum 변수를 0으로 생성
            # 이중 for 문을 이용해 각 리스트에 있는 레시피의 조합 값들의 합 구하기
            for i in range(int(N/2)):
                for j in range(int(N/2)):
                    asum += num_mat[a_list[i]][a_list[j]]
                    bsum += num_mat[b_list[i]][b_list[j]]
            if ans > abs(asum - bsum):  # 두 레시피 합의 차가 현존 최소 값인 경우
                ans = abs(asum - bsum)  # -> ans 변수에 새로운 레시피의 차를 갱신
        return

    DFS(n+1, a_list+[n], b_list)    # a_list에 레시피를 담는 경우
    DFS(n+1, a_list, b_list+[n])    # b_list에 레시피를 담는 경우

# input값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    ans = 1e100
    # DFS 함수 사용하기
    DFS(0, [], [])  # DFS(시작인덱스, 빈 A리스트, 빈 B리스트)

    # 결과 출력
    print(f'#{tc} {ans}')