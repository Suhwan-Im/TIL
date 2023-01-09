import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())        # 색종이 개수
num_mat = []            # 색종이 좌표를 담을 빈리스트
for _ in range(N):      # for문을 이용해 색종이 좌표 담기
    num_mat.append(list(map(int, input().split())))

# 100 x 100의 0 매트릭스 생성
check_mat = []
for i in range(100):
    check_list = []
    for j in range(100):
        check_list.append(0)
    check_mat.append(check_list)

# 색종이 범위는 check_mat 매트릭스에 1로 표기
for nums in num_mat:
    for i in range(nums[0], nums[0]+10):
        for j in range(nums[1], nums[1]+10):
            check_mat[i][j] = 1

# 색종이 영영의 넓이 계산 (check_mat 매트릭스상 1의 개수 합산)
ans = 0
for i in range(100):
    for j in range(100):
        if check_mat[i][j] == 1:
            ans += 1

# 결과 출력
print(ans)