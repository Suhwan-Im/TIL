import sys
sys.stdin = open('input.txt')


N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]


col_max = 0     # 기둥의 최대 범위
row_max = 0     # 기둥의 최대 높이
idx_max = 0     # 최대 높이 기둥의 인덱스
# for문을 이용해 위의 변수들에 알맞은 값 담기
for i in range(len(num_list)):
    if num_list[i][0] > col_max:
        col_max = num_list[i][0]
    if num_list[i][1] > row_max:
        row_max = num_list[i][1]
        idx_max = num_list[i][0]

# 모든 기둥을 포함할 수 있는 0의 숫자 매트릭스 생성
num_mat = [[0]*(row_max) for _ in range(col_max+1)]

# for문을 이용해 지붕아래의 범위는 1로 변경하기
for num in num_list:
    if num[0] < idx_max:                    # 현재 기둥이 최대높이 기둥보다 앞에 있을 경우
        for i in range(num[0], idx_max):        # 현재 기둥부터 최대높이 기둥 사이의 모든 공간 중
            for j in range(num[1]):             # 현재 기둥 높이만큼의 범위를 모두 1로 변경
                num_mat[i][j] = 1
    elif num[0] == idx_max:                 # 현재 기둥이 최대높이 기둥일 경우
        for j in range(num[1]):                 # 현재 기둥에 해당하는 공간을 1로 변경
            num_mat[num[0]][j] = 1
    elif num[0] > idx_max:                  # 현재 기둥이 최대높이 기둥보다 뒤에 있을 경우
        for i in range(num[0], idx_max, -1):    # 현재 기둥부터 취대높이 기둥 사이의 모든 공간 중
            for j in range(num[1]):             # 현재 기둥 높이만큼의 범위를 모두 1로 변경
                num_mat[i][j] = 1

cnt = 0     # 지붕 아래 넓이의 총합을 담을 cnt변수 0으로 지정
for i in range(len(num_mat)):
    for j in range(len(num_mat[0])):
        if num_mat[i][j] == 1:
            cnt += 1    # 1의 개수를 cnt변수에 누적하기

# 결과 출력
print(cnt)