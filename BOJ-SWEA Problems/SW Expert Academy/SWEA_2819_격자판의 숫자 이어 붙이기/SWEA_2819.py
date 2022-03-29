import sys
sys.stdin = open('input.txt')


# BFS 함수 정의
def DFS(n, num, i, j):
    if n == 7:          # 깊이가 7까지 내려가면
        sset.add(num)   # -> 현재 만든 숫자를 set에 추가
        return          # -> DFS 종료
    for k in range(4):                      # for 문을 이용해 인접칸 탐색
        ni, nj = i + di[k], j + dj[k]       # -> 새로운 4방향 좌표 생성
        if 0 <= ni < 4 and 0 <= nj < 4:     # 만약 새로운 좌표가 범위내에 위치하면
            DFS(n+1, num*10 + num_mat[ni][nj], ni, nj)      # DFS 함수 이용 (n+1번째 칸, 숫자 누적, 새 i좌표. 새 j좌표)

# input 값 입력 받기
T = int(input())
for tc in range(1, T+1):
    num_mat = [list(map(int, input().split())) for _ in range(4)]

    sset = set()        # 중복되지 않는 경우의 값들을 담아줄 sset 세트 생성

    # 4방향 좌표 설정
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 이중 for 문을 이용해 매트릭스내 모든 원소에서 DFS 진행
    for i in range(len(num_mat)):
        for j in range(len(num_mat[i])):
            DFS(0, 0, i, j)     # DFS 함수 이용 (n번째 칸, 숫자누적, i좌표, j좌표)

    rlt = len(sset)     # sset의 길이를 rlt 변수에 저장

    # 결과 출력
    print(f'#{tc} {rlt}')