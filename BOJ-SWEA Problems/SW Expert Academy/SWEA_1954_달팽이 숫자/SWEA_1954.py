import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 0으로 이루어진 NxN 배열 만들기
    num_mat = [[0] * N for _ in range(N)]

    # 변수 초기화
    curr_N = N  # 4 -> 3 -> 3 -> 2 -> 2 -> 1 의 방식을 담는 변수
    curr_i = -1  # 인덱스 i의 현재 위치
    curr_j = -1  # 인덱스 j의 현재 위치
    num = 1  # 리스트에 출력할 숫자
    way = 1  # 방향 (좌: -1 / 우: 1 / 상 : 2 / 하: -2)

    # while문을 이용해 달팽이 구조로 접근하여 매트릭스의 모든 값을 업데이트 한 후 중앙에서 반복문 정지
    while curr_N > 0:
        # 우측 방향으로 진행 (curr_N 값에서 1을 뺌)
        if way == 1:
            curr_i += 1
            curr_j += 1
            for _ in range(curr_N):
                num_mat[curr_i][curr_j] = num
                curr_j += 1
                num += 1
            curr_N -= 1
            way = -2

        # 아래 방향으로 진행
        elif way == -2:
            curr_j -= 1
            curr_i += 1
            for _ in range(curr_N):
                num_mat[curr_i][curr_j] = num
                curr_i += 1
                num += 1
            way = -1

        # 좌측 방향으로 진행 (curr_N 값에서 1을 뺌)
        elif way == -1:
            curr_i -= 1
            curr_j -= 1
            for _ in range(curr_N):
                num_mat[curr_i][curr_j] = num
                curr_j -= 1
                num += 1
            curr_N -= 1
            way = 2

        # 위 방향으로 진행
        elif way == 2:
            curr_j += 1
            curr_i -= 1
            for _ in range(curr_N):
                num_mat[curr_i][curr_j] = num
                curr_i -= 1
                num += 1
            way = 1
        else:
            pass

    # 결과 출력
    print(f'#{tc}')

    for i in range(N):
        for j in range(N):
            print(num_mat[i][j], end=' ')
        print()