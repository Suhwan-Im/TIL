import sys
sys.stdin = open('input.txt')


# BFS 함수 생성
def BFS(s):
    que = []                # 빈 큐 생성
    visited = [0] * 101     # 통화 여부를 넣을 visited 리스트 생성

    que.append(s)           # 큐에 최초 발신자 넣기
    visited[s] = 1          # visited 리스트에 최초 발신자 1로 갱신
    sol = s                 # 마지막 최대 숫자의 발신자 번호를 담을 sol 변수에 현재 발신자 번호 넣기

    while que:
        caller = que.pop(0)     # que에서 발신인 번호를 꺼내서 caller 변수에 저장
        if (visited[sol] < visited[caller]) or (visited[sol] == visited[caller] and sol < caller):  # 만약 현재 발신자가 이후 순서이거나, 같은 순서에서 번호가 더 클때
            sol = caller                                                                            # -> sol변수에 발신자 번호 갱신
        # for문을 이용해 수신인 정보 갱신하기
        for receiver in range(1, 101):
            if adj_mat[caller][receiver] == 1 and visited[receiver] == 0:   # 현재 발신인 기준 수신자이고, 전화받은 적이 없으면
                que.append(receiver)                                        # -> 수신인 번호를 큐에 삽입
                visited[receiver] = visited[caller] + 1                     # -> visited 리스트에 순서 누적 (시간 흐름상 순서)
    return sol

T = 10
for tc in range(1, T+1):
    L, S = map(int, input().split())
    num_list = list(map(int, input().split()))

    # num_list를 2차원 배열에 저장
    adj_mat = [[0] * 101 for _ in range(101)]   # 연락 인원의 번호는 1~100
    for i in range(0, len(num_list), 2):
        adj_mat[num_list[i]][num_list[i+1]] = 1     # [발신인, 수신인]의 좌표에 1 넣기

    ans = BFS(S)

    # 결과 출력
    print(f'#{tc} {ans}')