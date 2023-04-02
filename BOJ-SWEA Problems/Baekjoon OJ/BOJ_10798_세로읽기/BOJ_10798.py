import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
words = [str(input()) for _ in range(5)]
new_word = ''

i, j = 0, 0
while True:
    if len(words[i]) >= (j + 1):
        new_word += words[i][j]

    i += 1
    if i == 5:
        i = 0
        j += 1

    if j == 15:
        break

# 결과 출력
print(new_word)