import sys
sys.stdin = open('input.txt')

# input 값 받아서 2차원 리스트 num_mat에 저장
num_mat = [list(map(int, input().split())) for _ in range(9)]

# 정답을 담을 변수 생성
max_num = 0
max_i = 0
max_j = 0

# 이중 for문으로 최댓값 탐색
for i in range(9):
    for j in range(9):
        if num_mat[i][j] >= max_num:
            max_num = num_mat[i][j]     # 최댓값 저장
            max_i, max_j = i+1, j+1     # 좌표 저장

# 정답 출력
print(max_num)
print(max_i, max_j)