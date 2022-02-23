import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # N이 10, 20 일때의 경우의 수 입력
    memo = [1, 3]

    # N이 30 이상일때부터 계산
    for i in range(2, (N // 10)):
        memo.append(memo[i - 1] + memo[i - 2] * 2)  # 특정 N값의 경우의 수는 [P(N-10) + P(N-20)*2]와 같음

    # N값의 경우의 수를 rlt변수에 저장
    rlt = memo[-1]

    # 결과 출력
    print(f'#{tc} {rlt}')