import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
num_list = []   # 숫자를 담을 빈 리스트 생성
for i in range(N):
    num_list.append(int(input()))   # 숫자 담기

# for문을 이용해 삽입정렬 수행
for i in range(1, N):
    for j in range(i, 0, -1):
        if num_list[j] < num_list[j-1]:
            num_list[j], num_list[j-1] = num_list[j-1], num_list[j]

# for문을 이용해 정렬된 결과 출력
for num in num_list:
    print(num)