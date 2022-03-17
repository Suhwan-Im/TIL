import sys
sys.stdin = open('input.txt')


# 힙 트리 삽입 함수
def enq(n):
    global last
    last += 1
    tree[last] = n  # 트리의 가장 마지막 노드에 숫자 넣기
    c = last        # 가장 마지막 노드를 자식 노드인 c로 설정
    p = c // 2      # 가장 마지막 노드의 부모 노드를 p로 설정
    while p >= 1 and tree[p] > tree[c]:     # 부모 노드가 있고, 부모의 키값이 더 클때
        tree[p], tree[c] = tree[c], tree[p] # 부모 노드의 숫자와 자식 노드의 숫자 교환
        c = p		# 자식 노드 갱신
        p = c // 2  # 부모 노드 갱신

# input 값 변수에 할당하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    tree = [0] * (N+1)  # 힙 트리 생성
    last = 0            # 마지막 정점 번호
    # for문을 이용해 주어진 숫자를 모두 힙트리에 삽입
    for num in nums:
        enq(num)

    sum = 0     # 부모 노드의 합을 담을 sum 변수 0으로 생성
    curr = N    # 마지막 노드인 N을 curr 변수에 저장
    while curr > 1:         # 루트 노드를 만나기 전까지
        curr //= 2          # 부모 노드 번호를 curr 변수에 저장
        sum += tree[curr]   # sum 변수에 부모 노드의 숫자를 누적

    # 결과 출력
    print(f'#{tc} {sum}')