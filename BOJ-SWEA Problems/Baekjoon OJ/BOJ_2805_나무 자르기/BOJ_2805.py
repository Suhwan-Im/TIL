import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

highest = max(tree_list)
lowest = 0

# 이분탐색을 이용해 정답 구하기
while highest >= lowest:
    mid = (lowest + highest) // 2
    total = 0
    for tree in tree_list:
        if tree > mid:
            total += (tree - mid)

    if total < M:
        highest = mid - 1
    else:
        lowest = mid + 1

# 결과 출력
print(highest)