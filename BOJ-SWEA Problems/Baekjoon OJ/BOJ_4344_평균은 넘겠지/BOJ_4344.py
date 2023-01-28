import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
C = int(input())
cases = []
for _ in range(C):
    cases.append(list(map(int, input().split())))

# for문을 이용해 정답 구하기
for case in cases:
    avg = sum(case[1:]) / case[0]
    cnt = 0
    for i in range(1, len(case)):
        if case[i] > avg:
            cnt += 1
    ans = cnt / case[0] * 100
    print("%.3f"%ans + "%")     # 소수점 셋째 자리까지 출력