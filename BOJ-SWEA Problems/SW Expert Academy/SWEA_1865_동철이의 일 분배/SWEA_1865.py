import sys
sys.stdin = open('input2.txt')


# 최고 성공률을 찾아주는 DFS 함수 정의
def DFS(n, pos, n_list, p_list):            # DFS(노드의 높이, 누적 성공률, 숫자 리스트, 순열을 담을 리스트)
    global max_pos
    if pos <= max_pos:                      # 만약 현재 성공률이 최고 성공률 이하인 경우
        return                              # -> DFS 함수 반환
    if n == len(n_list) and pos > max_pos:  # 리스트의 모든 숫자를 거친 후, pos 값이 max_pos 보다 큰 경우
        max_pos = pos                       # -> max_pos 변수에 현재 pos 값 갱신
        return                              # -> DFS 함수 반환
    else:                                   # 위의 조건들이 아니고, 아직 순열을 만들고 있을때
        for p in n_list:                    # -> for 문을 이용해서 순열 만들기
            if p not in p_list:             # -> 리스트에서 뽑아낸 숫자가 순열 리스트에 없는 경우
                DFS(n+1, (pos * num_mat[p-1][n]) / 100, n_list, p_list + [p])   # DFS 함수 반복해서 순열 만들기
                                                                        # DFS(노드의 높이 + 1, 누적 성공률 * 이번 성공률, n_list, 순열 리스트 + p값)

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    # 1부터 N까지의 직원 리스트 만들기
    N_list = []                 # 직원 리스트를 담아줄 N_list 생성
    for n in range(1, N+1):     # for 문을 이용해 1부터 N까지 숫자 만들기
        N_list.append(n)        # N_list에 순서대로 누적하기

    max_pos = 0                 # 최대 성공 확률을 담아줄 max_pos 변수를 0으로 생성
    DFS(0, 100, N_list, [])     # DFS 함수를 이용해 최대 성공 확률 찾기 -- DFS(시작노드 높이, 성공률, N_list, 순열 리스트)

    # 결과 출력
    print(f'#{tc} {max_pos:0.6f}')