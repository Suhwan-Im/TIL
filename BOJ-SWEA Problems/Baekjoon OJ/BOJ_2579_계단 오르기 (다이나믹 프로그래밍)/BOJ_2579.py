import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
dp = [0]            # 특정 위치까지의 최대합을 담을 dp 리스트 생성 (다이나믹 프로그래밍)
points = [0]        # 각 계단의 점수를 담을 points 리스트 생성
for _ in range(N):  # for 문을 이용해 points 리스트에 계단 점수 담기
    points.append(int(input()))

if N == 0:
    print(0)                            # N이 0인 경우 0점 출력
elif N == 1:
    print(points[1])                    # N이 1인 경우 계단 점수 출력
else:
    dp.append(points[1])                # 첫번째 dp에 첫번째 계단 점수 담기
    dp.append(points[1] + points[2])    # 두번째 dp에 첫번째 계단 + 두번째 계단 점수 담기

    # for 문을 이용해 dp 리스트의 세번째 값부터 채워나가기
    for i in range(3, N+1):
        dp.append(max((dp[i-3] + points[i-1] + points[i]), (dp[i-2] + points[i])))

    print(dp[N])