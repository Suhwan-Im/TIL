import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
num_list = []
for _ in range(5):
    num_list.append(int(input()))

# 버블 정렬을 통해 숫자 리스트를 오름차순으로 정렬하기
for i in range(1, 5):
    for j in range(i, 0, -1):
        if num_list[j] < num_list[j-1]:
            num_list[j], num_list[j-1] = num_list[j-1], num_list[j]

# 결과값 출력하기
print(int(sum(num_list)/5))     # 평균값
print(num_list[2])              # 중앙값