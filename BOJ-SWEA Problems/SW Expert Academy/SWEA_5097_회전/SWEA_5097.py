import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_que = list(map(int, input().split()))

    front, rear = 0, M

    for _ in range(M):
        front = (front+1) % N
        rear = (rear+1) % N


    # 결과 출력
    print(f'#{tc} {num_que[front]}')