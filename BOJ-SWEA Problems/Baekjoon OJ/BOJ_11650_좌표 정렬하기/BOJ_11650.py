import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
point_list = []

for _ in range(N):
    point = list(map(int, input().split()))
    point_list.append(point)

point_list = sorted(point_list, key=lambda x: (x[0], x[1]))

# 결과 출력
for point in point_list:
    print(*point[:])