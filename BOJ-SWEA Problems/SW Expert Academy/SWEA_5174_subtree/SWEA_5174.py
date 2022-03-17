import sys
sys.stdin = open('input.txt')


# 전위 순회로 노드의 개수를 세는 함수 만들기
def pre_trav(T):
    if T:
        global cnt
        cnt += 1
        pre_trav(cl[T])
        pre_trav(cr[T])

# input 값 변수에 할당하기
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))

    # 자식 노드 리스트 생성
    cl = [0] * (E+2)    # 왼쪽 자식
    cr = [0] * (E+2)    # 오른쪽 자식

    # 부모 인덱스를 기준으로 자식 노드에 숫자 채우기
    for i in range(E):
        p = nodes[i*2]      # 부모 노드
        c = nodes[i*2 + 1]  # 자식 노드
        if cl[p] == 0:  # 만약 왼쪽 자식 노드가 비어있으면,
            cl[p] = c   # -> 왼쪽 자식 노드 리스트에 저장
        else:           # 만약 왼쪽 자식 노드가 비어있지 않으면,
            cr[p] = c   # -> 오른쪽 자식 노드 리스트에 저장

    # 서브 트리에 속한 노드 개수 세기
    cnt = 0         # 개수를 셀 cnt 변수 0으로 지정
    pre_trav(N)     # 전위 순회로 개수를 세는 함수 사용

    # 결과 출력
    print(f'#{tc} {cnt}')