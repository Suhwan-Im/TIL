import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
# N_list = sorted(N_list)     # N_list를 오름차순으로 정렬
M = int(input())
M_list = list(map(int, input().split()))

fin_list = []       # 각 수가 적힌 숫자카드의 갯수를 담을 fin_list 생성

# for문을 이용해 M_list 순회 + while문을 이용해 이분탐색 실시
for m in M_list:
    start = 0
    end = N-1
    while True:
        mid = (start + end) // 2
        if m == N_list[mid]:    # 해당 숫자를 찾은 경우 인근을 조회하며 같은 숫자 개수 누적하기
            count = 1
            up, down = mid+1, mid-1
            while (up <= (N-1)) and (m == N_list[up]):
                count += 1
                up += 1
            while (down >= 0) and (m == N_list[down]):
                count += 1
                down -= 1
            fin_list.append(count)
            break
        elif start >= end:
            fin_list.append(0)
            break
        elif m > N_list[mid]:
            start = mid + 1
        elif m < N_list[mid]:
            end = mid - 1

# 결과 출력
print(*fin_list[:])