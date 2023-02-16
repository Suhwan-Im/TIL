import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N, M = map(int, input().split())
chess_mat = [list(map(str, input())) for _ in range(N)]
min_fix = 1e100

# 이중 for문을 이용해 모든 경우의 8x8 배열 체크
for i in range(N - 7):
    for j in range(M - 7):
        cnt_fix = 0             # 현재 경우의 수정칸의 개수를 담을 변수 생성
        # 이중 for문을 이용해 배열내의 수정칸 개수 구하기 (0,0 자리가 흰색칸이라고 가정)
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x % 2 == 0) and (y % 2 == 0) and (chess_mat[x][y] == "W"):
                    cnt_fix += 1
                elif (x % 2 == 0) and (y % 2 == 1) and (chess_mat[x][y] == "B"):
                    cnt_fix += 1
                elif (x % 2 == 1) and (y % 2 == 0) and (chess_mat[x][y] == "B"):
                    cnt_fix += 1
                elif (x % 2 == 1) and (y % 2 == 1) and (chess_mat[x][y] == "W"):
                    cnt_fix += 1

        # if문을 이용해 0,0 자리가 검정칸인 경우 수정칸의 개수 고쳐주기
        if cnt_fix > 32:
            cnt_fix = 64 - cnt_fix

        # 만약 현재 경우의 수정칸의 개수가 기존 최소값보다 작은 경우, 최소값 갱신
        if cnt_fix < min_fix:
            min_fix = cnt_fix

# 결과 출력
print(min_fix)