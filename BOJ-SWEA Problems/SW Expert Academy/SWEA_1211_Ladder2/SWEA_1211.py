import sys
sys.stdin = open('input.txt')


# ladder 함수 정의
def ladder(num_mat):
    min_move = 1e100
    for i in range(len(num_mat[0])):
        if num_mat[0][i] == 1:
            # 현재의 i와 j 위치 지정
            curr_i = i
            curr_j = 0
            # 진행 방향 변수 설정 (좌측: -1 / 우측: 1 / 하강: 2)
            way = 2
            move = 0

            # 내려가면서 이동횟수 누적하기
            while curr_j < len(num_mat):
                # i가 0인 경우
                if curr_i == 0:
                    if num_mat[curr_j][curr_i + 1] == 1 and (way == 2 or way == 1):
                        curr_i += 1
                        way = 1
                        move += 1
                    else:
                        curr_j += 1
                        way = 2
                        move += 1

                # i가 99인 경우
                elif curr_i == 99:
                    if num_mat[curr_j][curr_i - 1] == 1 and (way == 2 or way == -1):
                        curr_i -= 1
                        way = -1
                        move += 1
                    else:
                        curr_j += 1
                        way = 2
                        move += 1

                # i가 1~98인 경우
                else:
                    if num_mat[curr_j][curr_i + 1] == 1 and (way == 2 or way == 1):
                        curr_i += 1
                        way = 1
                        move += 1
                    elif num_mat[curr_j][curr_i - 1] == 1 and (way == 2 or way == -1):
                        curr_i -= 1
                        way = -1
                        move += 1
                    else:
                        curr_j += 1
                        way = 2
                        move += 1

            # if문을 이용해 최단거리와 해당 인덱스 갱신하기
            if move <= min_move:
                min_move = move
                min_index = i

    # 최단거리의 시작점 인덱스 반환
    return min_index


# 테스트 케이스를 통한 코드 실행
T = 10
for tc in range(1, T + 1):
    N = int(input())  # 테스트케이스 번호
    # 리스트내 for문을 이용해 100x100의 매트릭스 생성
    num_mat = [list(map(int, input().split())) for _ in range(100)]

    # ladder 함수를 통해 결과값 계산
    rlt = ladder(num_mat)

    print(f'#{N} {rlt}')