import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    start, stop = map(int, input().split())

    visited = [[0, 0] for _ in range(E)]    # 방문한 위치를 표시할 nodes와 같은 크기의 visited 리스트 생성
    V_cnt = [0] * (V+1)                     # 인덱스 기준 각 노드별 지나온 간선의 갯수를 저장할 V_cnt 리스트 생성

    que = []            # 빈 큐 생성
    que.append([start]) # 큐에 시작점을 리스트 형식으로 삽입
    cnt = 0             # 회전수를 셀 cnt 변수 0으로 생성
    status = 0          # while문을 종료시킬 status 변수 0으로 생성

    # while문을 이용해 BFS 구현하기
    while status == 0 and que:
        curr_n = que.pop(0)             # 큐의 첫번째 인자 꺼내기
        sub_que = []                    # BFS 회전수별 인자를 담을 sub_que 리스트 생성
        for k in range(len(curr_n)):    # 큐에서 꺼낸 인자를 순회하기
            n = curr_n[k]               # 현재 값
            V_cnt[n] = cnt              # 현재 지나온 간선의 갯수를 노드 번호에 저장
            if n == stop:               # 만약 현재 값이 종료값인 경우,
                status = 1              # -> while문 종료 (status 변수를 1로 변경)
            for i in range(len(nodes)):             # 노드 리스트를 순회하며
                if nodes[i][0] == n and visited[i][0] == 0:     # 현재값이 노드의 첫번째 원소와 일치하고 방문하지 않은 곳일때,
                    sub_que.append(nodes[i][1])                 # -> 노드의 두번째 값을 sub_que에 누적
                    visited[i][0], visited[i][1] = 1, 1         # -> visited 리스트에 방문여부 1로 표시
                elif nodes[i][1] == n and visited[i][1] == 0:   # 현재값이 노드의 두번째 원소와 일치하고 방문하지 않은 곳일때,
                    sub_que.append(nodes[i][0])                 # -> 노드의 첫번째 값을 sub_que에 누적
                    visited[i][0], visited[i][1] = 1, 1         # -> visited 리스트에 방문여부 1로 표시
        if len(sub_que) > 0:            # sub_que에 값이 있는 경우,
            que.append(sub_que)         # -> 큐에 이번회차 sub_que 원소를 누적
        cnt += 1    # 회전수 1 증가

    # 결과 출력
    print(f'#{tc} {V_cnt[stop]}')