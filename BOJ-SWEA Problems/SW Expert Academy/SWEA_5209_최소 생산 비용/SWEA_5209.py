import sys
sys.stdin = open('input.txt')


# 순열을 만들어주는 DFS 함수 정의
def DFS(n, ssum, n_list, p_list):   # DFS(노드의 높이, 부분 합계, 숫자 리스트, 순열을 담을 리스트)
    global min_sum
    if ssum > min_sum:              # 현재 ssum 값이 min_sum 값보다 큰 경우
        return                      # -> DFS 함수 반환
    elif n == len(n_list):          # ssum 값이 min_sum 보다 작고, 리스트의 모든 숫자를 거친경우
        min_sum = ssum              # -> min_sum 변수에 현재 ssum 값 갱신
        return                      # -> DFS 함수 반환
    else:                           # 위의 조건들이 아니고, 아직 순열을 만들고 있을때
        for p in n_list:            # -> for 문을 이용해서 순열 만들기
            if p not in p_list:     # -> 리스트에서 뽑아낸 숫자가 순열 리스트에 없는 경우
                DFS(n+1, ssum + num_mat[p-1][n], n_list, p_list + [p])      # DFS 함수 반복해서 순열 만들기
                                                                            # DFS(노드의 높이 + 1, 부분 합계 + 현재 생산비용, n_list, 순열 리스트 + p값)

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat =[list(map(int, input().split())) for _ in range(N)]

    # 1부터 N까지의 숫자 리스트 만들기
    N_list = []                 # 숫자 리스트를 담아줄 N_list 생성
    for n in range(1, N+1):     # for 문을 이용해 1부터 N까지 숫자 만들기
        N_list.append(n)        # N_list에 순서대로 누적하기

    min_sum = 1e100             # 최소 생산 비용을 담아줄 min_sum 변수를 큰 수로 생성
    DFS(0, 0, N_list, [])       # DFS 함수를 이용해 최소 생산 비용 찾기 -- DFS(시작노드 높이, 합계 변수, N_list, 순열 리스트)

    # 결과 출력
    print(f'#{tc} {min_sum}')