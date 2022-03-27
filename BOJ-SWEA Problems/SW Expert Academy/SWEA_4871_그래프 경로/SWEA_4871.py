import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    cl = [0] * (V+1)
    cr = [0] * (V+1)

    for node in nodes:
        if cl[node[0]] == 0:
            cl[node[0]] = node[1]
        elif cr[node[0]] == 0:
            cr[node[0]] = node[1]

    visited = [0] * (V+1)
    stack = []

    stack.append(S)
    rlt = 0

    while stack:
        v = stack.pop()
        visited[v] = 1
        if v == G:
            rlt = 1
            break
        else:
            if cl[v] != 0 and visited[cl[v]] == 0:
                stack.append(cl[v])
            if cr[v] != 0 and visited[cr[v]] == 0:
                stack.append(cr[v])

    # 결과 출력
    print(f'#{tc} {rlt}')