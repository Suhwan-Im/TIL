import sys
sys.stdin = open('input.txt')


# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    di, dj = (1, -1, 0, 0), (0, 0, -1, 1)   # 상하좌우 (이번 케이스에서는 y축의 양수가 위쪽)
    ans = 0                                 # 방출된 에너지의 총합을 누적할 ans 변수를 0으로 생성

    # for 문을 이용해 좌표를 2배로 늘려주기 (0.5 구간에서 소멸되는 것을 보완하기 위함)
    for i in range(len(num_mat)):
        num_mat[i][0] *= 2
        num_mat[i][1] *= 2

    # for 문을 이용해 2차원 평면의 끝에서 끝으로 가는데 걸리는 시간동안 반복문 진행
    for _ in range(4002):
        for i in range(len(num_mat)):           # 좌표를 이동하기
            num_mat[i][0] += dj[num_mat[i][2]]
            num_mat[i][1] += di[num_mat[i][2]]

        ddel, visited = set(), set()            # 중복되면 삭제해주기 위한 ddel 셋과 visited 셋 생성
        for i in range(len(num_mat)):
            ci, cj = num_mat[i][0], num_mat[i][1]
            if (ci, cj) in visited:
                ddel.add((ci, cj))
            visited.add((ci, cj))

        for i in range(len(num_mat)-1, -1, -1): # ddel에 포함되어 있으면 삭제
            if (num_mat[i][0], num_mat[i][1]) in ddel:
               ans += num_mat[i][3]
               num_mat.pop(i)

    # 결과 출력
    print(f'#{tc} {ans}')