import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
T = int(input())

# 파도반 수열 구하기
padovan = [0] * 101                     # 파도반 수열을 담을 padovan 리스트 생성
padovan[1], padovan[2], padovan[3], padovan[4], padovan[5] = 1, 1, 1, 2, 2  # 첫 5개 숫자 입력

for i in range(6, 101):                 # for문을 이용해 6번째부터 100번째까지 파도반 수열을 누적해가기 (다이나믹 프로그래밍)
    padovan[i] = padovan[i-1] + padovan [i-5]       # i 위치의 값은 [(i-1) + (i-5)] 위치의 값

# 테스트 케이스 별 정답 출력
for _ in range(T):
    N = int(input())
    print(padovan[N])