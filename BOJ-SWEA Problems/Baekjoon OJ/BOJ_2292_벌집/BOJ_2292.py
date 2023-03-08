import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
max_num = 1
layer = 1

while N > max_num:
    max_num += layer * 6
    layer += 1

# 결과 출력
print(layer)