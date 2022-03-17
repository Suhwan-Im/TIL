import sys
sys.stdin = open('input.txt')


# 중위 순회로 이진탐색트리를 채워주는 함수 만들기
def inorder(T):
    if T:
        inorder(cl[T])
        global cnt
        num[T] = cnt
        cnt += 1
        inorder(cr[T])

# input 값 변수에 할당하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 자식 노드 리스트 생성
    cl = [0] * (N+1)    # 왼쪽 자식
    cr = [0] * (N+1)    # 오른쪽 자식

    # 완전 이진트리 노드 번호를 자식 노드 리스트에 넣기
    for i in range(1, N+1):
        if cl[i] == 0 and (i*2) <= N:       # 왼쪽 자식이 비어있고 N 범위 내일때,
            cl[i] = i*2                     # -> 왼쪽 자식에 (부모 번호 * 2) 를 넣기
        if cr[i] == 0 and (i*2 + 1) <= N:   # 오른쪽 자식이 비어있고 N 범위 내일때,
            cr[i] = i*2 + 1                 # -> 오른쪽 자식에 (부모 번호 * 2 + 1) 을 넣기

    # 이진탐색트리의 숫자를 담을 num 리스트 생성
    num = [0] * (N+1)

    cnt = 1     # cnt 변수 지정
    inorder(1)  # 중위 순회 함수 이용해서 이진탐색트리 숫자 채워주기

    # 결과 출력
    print(f'#{tc} {num[1]} {num[N//2]}')    # 루트 노드의 값 & (N/2)번 노드 값 출력