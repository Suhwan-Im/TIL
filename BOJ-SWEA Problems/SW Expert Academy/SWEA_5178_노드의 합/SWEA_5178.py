import sys
sys.stdin = open('input.txt')


# input 값 변수에 할당하기
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N+1)     # 노드 인덱스를 기준으로 한 노드 리스트 만들기
    for _ in range(M):      # 입력받은 숫자를 노드 리스트내 알맞은 위치에 넣기
        node, num = map(int, input().split())
        nodes[node] = num

    curr = N    # 트리의 제일 마지막 노드번호를 curr 변수에 저장
    # while문을 이용해 트리를 거꾸로 올라오면서 모든 노드에 값을 넣어주기 
    while curr > 1:
        if curr % 2 == 0:                   # 만약 현재 노드 번호가 짝수라면, (형제 노드가 없는 경우)
            nodes[curr//2] = nodes[curr]    # -> 부모 노드 값에 현재 노드의 값 올려주기
            curr -= 1                       # -> 현재 노드 번호를 1개 앞으로 옮겨주기
        else:                                               # 만약 현재 노드 번호가 홀수라면, (형제 노드가 있는 경우)
            nodes[curr//2] = nodes[curr-1] + nodes[curr]    # -> 부모 노드 값에 형제 노드의 합을 올려주기
            curr -= 2                                       # -> 현재 노드 번호를 2개 앞으로 옯겨주기
    
    # rlt 변수에 찾고자 하는 위치의 노드 값을 저장해주기
    rlt = nodes[L]

    # 결과 출력
    print(f'#{tc} {rlt}')