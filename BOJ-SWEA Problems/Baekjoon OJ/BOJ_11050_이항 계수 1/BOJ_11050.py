import sys
sys.stdin = open('input.txt')

# 팩토리얼 함수 구현
def factor(n):
    rlt = 1
    for i in range(n, 0, -1):
        rlt *= i
    return(rlt)

# input 값 입력 받기
N, K = map(int, input().split())
ans = factor(N) / (factor(K) * factor(N-K))     # 이항계수 계산

# 결과 출력
print(f'{ans:.0f}')