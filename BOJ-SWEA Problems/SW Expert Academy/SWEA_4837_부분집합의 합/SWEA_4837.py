import sys
sys.stdin = open('input.txt')

# mysum 함수 정의
def mysum(lst):
    total = 0
    for n in lst:
        total += n
    return total


# 테스트케이스 입력으로 문제 풀기
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    list_12 = list(range(1, 13))
    n = len(list_12)
    partial_list = []

    # 비트연산자를 이용해 부분집합 구하기
    for i in range(1 << n):
        temp_list = []
        for j in range(n):
            if i & (1 << j):
                temp_list.append(list_12[j])
        partial_list.append(temp_list)

    # 부분집합중 길이가 N이고 합이 K인 개수 구하기
    cnt = 0
    for nums in partial_list[1:]:
        if len(nums) == N and mysum(nums) == K:
            cnt += 1


    # 결과 출력
    print(f'#{tc} {cnt}')