import sys
sys.stdin = open('input.txt')

# input값 입력 받기
N = int(input())
N_list = sorted(list(map(int, input().split())))
length = len(N_list)
M = int(input())
M_list = list(map(int, input().split()))

ans_list = []       # 정답을 담을 빈 리스트 생성

for m in M_list:
    left = 0
    right = length - 1
    ans = 0
    
    # 이진 탐색으로 카드 찾기
    while left <= right:
        mid = (left + right) // 2
        if N_list[mid] == m:
            ans = 1
            break
        elif N_list[mid] > m:
            right = mid - 1
        else:
            left = mid + 1

    ans_list.append(ans)

# 결과 출력
print(*ans_list[:])