import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
sentence = str(input())

cnt = 0
switch = 0

for letter in sentence:
    if letter == ' ':
        switch = 0
    elif switch == 0 and letter:
        cnt += 1
        switch = 1

# 결과 출력
print(cnt)