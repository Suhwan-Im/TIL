import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
dp = [0] * (N + 1)      # 다이나믹 프로그래밍에 의한 값을 담을 dp 리스트 생성

# 2xn 타일의 경우의 수는 n이 증가할때 마다 (n-2 개수)+(n-1개수)와 같음

# for 문을 이용해 dp 리스트 채우기
for n in range(1, N+1):
    if n == 1:
        dp[n] = 1
    elif n == 2:
        dp[n] = 2
    else:
        dp[n] = dp[n-2] + dp[n-1]

# 결과 출력
print(dp[N] % 10007)