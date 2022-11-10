import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
num_mat_A = [list(map(int, input().split())) for _ in range(N)]
num_mat_B = [list(map(int, input().split())) for _ in range(N)]

new_mat = []
for i in range(N):
    new_row = []
    for j in range(M):
        new_row.append(num_mat_A[i][j] + num_mat_B[i][j])
    new_mat.append(new_row)

# 결과 출력
for i in range(N):
    print(*new_mat[i][:])