import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 영역의 개수
    num_list = []
    for i in range(N):
        num_list.append(list(map(int, input().split())))

    # 10x10의 0 매트릭스 만들기
    num_mat = [[0] * 10 for _ in range(10)]

    # for문을 이용해 영역별로 색깔 지정 (0: 무색 / 1: 빨강 / 2: 파랑 / 3: 보라)
    for nums in num_list:
        for r in range(nums[0], nums[2] + 1):
            for c in range(nums[1], nums[3] + 1):
                if num_mat[r][c] == 0:
                    num_mat[r][c] = nums[4]
                elif num_mat[r][c] == 1:
                    if nums[4] == 2:
                        num_mat[r][c] = 3
                elif num_mat[r][c] == 2:
                    if nums[4] == 1:
                        num_mat[r][c] = 3

    # 색깔을 채운 매트릭스에서 보라색인 칸 세기
    cnt = 0
    for i in range(10):
        for j in range(10):
            if num_mat[i][j] == 3:
                cnt += 1

    # 결과 출력
    print(f'#{tc} {cnt}')