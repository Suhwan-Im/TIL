import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
paper_mat = [list(map(int, input().split())) for _ in range(N)]

blue, white = 0, 0      # 각 색종이 개수를 담을 blue, white 변수 생성
i, j = 0, 0             # 현재 위치 정보를 포함할 i, j 변수 생성

# 재귀함수 이용해서 색종이 개수 구하기
def paper_cut(N, i, j):
    global blue, white
    if N == 1:                          # N값이 1인 경우 (1x1 색종이 -> 해당 색깔에 개수 누적)
        if paper_mat[i][j] == 0:
            white += 1
        else:
            blue += 1
    else:                               # N값이 1이 아닌 경우,
        color = paper_mat[i][j]             # 좌측상단의 색깔 정보를 color 변수에 저장
        one_paper = 1                       # 현재 종이가 모두 같은 색깔인지를 판단할 one_paper 변수를 1로 생성 (1: 단색, 0: 다색)
        for k in range(i, i+N):             # 이중 for문을 이용하여 현재 종이 순회하며 색깔 판단하기
            for l in range(j, j+N):
                if color != paper_mat[k][l]:    # 현재 위치의 색깔이 좌측상단 색깔과 불일치인 경우,
                    one_paper = 0                   # -> one_paper 변수 0으로 변경
                    paper_cut(N//2, i, j)                   # 좌측상단 재귀함수
                    paper_cut(N//2, i + N//2, j)            # 우측상단 재귀함수
                    paper_cut(N//2, i, j + N//2)            # 좌측하단 재귀함수
                    paper_cut(N//2, i + N//2, j + N//2)     # 우측하단 재귀함수
                    break                           # -> break 하여 내부 for문 종료
            if one_paper == 0:                  # 다색 색종이인 경우,
                break                               # -> 한번 더 break 하여 외부 for문 종료 (이중 for문 모두 종료)

        if one_paper == 1:                  # 단색 색종이인 경우, 해당 색깔에 개수 누적
            if color == 0:
                white += 1
            else:
                blue += 1

# paper_cut 함수 구동하기
paper_cut(N, i, j)

# 결과 출력
print(white)
print(blue)