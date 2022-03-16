import sys
sys.stdin = open('input.txt')


# 중위 순회 출력 함수 만들기
def ino_trav(T):
    if T:
        ino_trav(cl[T])
        print(w[T], end='')
        ino_trav(cr[T])

# input 값 받기
T = 10
for tc in range(1, T+1):
    V = int(input())
    nodes = [list(input().split()) for _ in range(V)]

    # 단어 & 자식 리스트 생성
    w = [0] * (V+1)     # 단어 리스트
    cl = [0] * (V+1)    # 왼쪽 자식 리스트
    cr = [0] * (V+1)    # 오른쪽 자식 리스트

    for node in nodes:
        p = int(node[0])            # 노드줄의 첫번째 항목은 부모노드
        w[p] = str(node[1])         # 노드줄의 두번째 항목은 단어
        if len(node) == 4:          # 만약 노드줄의 길이가 4인 경우,
            cl[p] = int(node[2])    # -> 노드줄의 세번째 항목은 왼쪽 자식노드에 넣기
            cr[p] = int(node[3])    # -> 노드줄의 네번째 항목은 오른쪽 자식노드에 넣기
        elif len(node) == 3:        # 만약 노드줄의 길이가 3인 경우,
            cl[p] = int(node[2])    # -> 노드줄의 세번째 항목은 왼쪽 자식노드에 넣기

    # 결과 출력
    print(f'#{tc}', end=' ')
    ino_trav(1)     # 중위순회 출력함수 실행
    print('')       # 테스트케이스 사이를 한칸씩 띄어주기