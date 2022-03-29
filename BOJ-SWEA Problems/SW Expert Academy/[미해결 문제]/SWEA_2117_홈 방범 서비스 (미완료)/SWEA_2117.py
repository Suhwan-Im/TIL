import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_mat = [list(map(int, input().split())) for _ in range(N)]





    # 결과 출력
    print(f'#{tc} {num_mat}')