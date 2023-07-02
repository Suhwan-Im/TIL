import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N, M, B = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
fin_time = 1e100
fin_height = 0


# 층별로 시간 계산하기
for h in range(257):
    add, delete = 0, 0
    for i in range(N):
        for j in range(M):
            if area[i][j] >= h:
                delete += area[i][j] - h
            else:
                add += h - area[i][j]

    # 만약 블록이 모자라서 해당 층을 만들 수 없을 경우, 이하코드 생략 (continue)
    if add > (delete + B):
        continue

    time = add + (delete * 2)
    if time <= fin_time:
        fin_time = time
        fin_height = h

print(fin_time, fin_height)