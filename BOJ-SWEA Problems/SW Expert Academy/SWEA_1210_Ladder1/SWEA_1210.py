import sys
sys.stdin = open('input.txt')


# ladder 함수 정의
def ladder(num_mat):
    # index 메서드를 이용해서 X표시(숫자 2)의 인덱스를 curr_idx로 저장
    curr_i = num_mat[-1].index(2)
    curr_j = len(num_mat) - 1
    # 진행 방향 변수 설정 (상승: 0 / 좌측: -1 / 우측: 1)
    way = 0

    # 거꾸로 올라가면서 시작점 찾기
    while curr_j > 0:
        # i가 0인 경우
        if curr_i == 0:
            if num_mat[curr_j][curr_i + 1] == 1 and (way == 0 or way == 1):
                curr_i += 1
                way = 1
            else:
                curr_j -= 1
                way = 0

        # i가 99인 경우
        elif curr_i == 99:
            if num_mat[curr_j][curr_i - 1] == 1 and (way == 0 or way == -1):
                curr_i -= 1
                way = -1
            else:
                curr_j -= 1
                way = 0

        # i가 1~98인 경우
        else:
            if num_mat[curr_j][curr_i + 1] == 1 and (way == 0 or way == 1):
                curr_i += 1
                way = 1
            elif num_mat[curr_j][curr_i - 1] == 1 and (way == 0 or way == -1):
                curr_i -= 1
                way = -1
            else:
                curr_j -= 1
                way = 0

    # 시작점의 (첫째행) 인덱스 반환
    return curr_i


# 테스트 케이스를 통한 코드 실행
T = 10
for tc in range(1, T + 1):
    N = int(input())  # 테스트케이스 번호
    # 리스트내 for문을 이용해 100x100의 매트릭스 생성
    num_mat = [list(map(int, input().split())) for _ in range(100)]

    # ladder 함수를 통해 결과값 계산
    rlt = ladder(num_mat)

    print(f'#{N} {rlt}')