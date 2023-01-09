import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N, M = map(int, input().split())
n_list = list(map(int, input().split()))

ans = 0     # 정답을 담을 변수 생성
for i in range(N):              # 첫번째 숫자를 순회할 for문
    for j in range(1, N):       # 두번째 숫자를 순회할 for문
        for k in range(2, N):   # 세번째 숫자를 순회할 for문
            if (i == j) or (j == k) or (i == k):    # 각 자리의 숫자가 중복되는 경우, pass
                pass
            else:                                   # 중복되지 않는 경우
                num = n_list[i] + n_list[j] + n_list[k]     # 세 수의 합을 num 변수에 저장
                if num <= M and num > ans:          # 세 수의 합이 M 이하이고, 지금까지의 정답보다 큰 경우
                    ans = num                               # ans에 새로운 합을 저장

# 결과 출력
print(ans)