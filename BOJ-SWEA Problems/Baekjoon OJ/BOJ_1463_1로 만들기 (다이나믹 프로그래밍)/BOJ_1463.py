import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
X = int(input())
dp = [0] * (X + 1)      # X+1개의 0을 포함하는 dp 리스트 생성 (최소 연산횟수를 담을 리스트)

# 다이나믹 프로그래밍을 통해 dp 리스트 채우기
#  X  - 0 1 2 3 4 5 6 7 8 9 10
#  dp - 0 0 0 0 0 0 0 0 0 0 0 (초기값)
#  dp - 0 0 1 1 2 3 2 3 3 2 3 (결과값)

# for문을 이용해 2부터 X까지 오름차순으로 최소 연산횟수를 구해서 dp에 누적하기
for i in range(2, X+1):
    dp[i] = dp[i-1] + 1     # 현재 dp값을 (이전 dp값 + 1)로 채우기

    # 만약 현재수가 2로 나뉘면,
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)        # 현재 dp값과 ((i/2) + 1) 중 작은 값으로 갱신

    # 만약 현재수가 3으로 나뉘면,
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)        # 현재 dp값과 ((i/3) + 1) 중 작은 값으로 갱신

# 결과 출력
print(dp[X])

# 코드 참조: https://blog.naver.com/ai05024/222880937642