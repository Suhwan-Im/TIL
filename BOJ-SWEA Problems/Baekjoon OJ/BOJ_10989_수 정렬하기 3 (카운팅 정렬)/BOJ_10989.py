import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N = int(input())

# # 버블 정렬
# num_list = [int(input()) for _ in range(N)]
#
# # for 문을 이용해서 숫자 정렬하기
# for i in range(N-1, 0, -1):
#     for j in range(0, i):
#         if num_list[j] > num_list[j+1]:
#             num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
#
# # 결과 출력
# for num in num_list:
#     print(num)

# 카운팅 정렬
count = [0] * 10001

# for 문을 이용해 count 리스트에 개수 누적하기 (카운팅 정렬)
for _ in range(N):
    count[int(input())] += 1

# 결과 출력
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)