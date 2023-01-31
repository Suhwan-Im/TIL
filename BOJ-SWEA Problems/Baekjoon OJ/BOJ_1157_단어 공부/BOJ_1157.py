import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
word = str(input())

# for문을 이용해 알파벳 개수 담기
cnt_list = [0 for _ in range(26)]   # 알파벳 개수를 담을 cnt_list 생성
for letter in word:
    if (ord(letter) >= 65) and (ord(letter) <= 90):
        cnt_list[ord(letter) % 65] += 1
    elif (ord(letter) >= 97) and (ord(letter) <= 122):
        cnt_list[ord(letter) % 97] += 1

# for문을 이용해 가장 많이 사용된 알파벳 찾기
popular_word = []   # 가장 많이 사용된 단어의 인덱스를 담을 빈리스트 생성
for i in range(26):
    if cnt_list[i] == max(cnt_list):
        popular_word.append(i)

# 결과 출력
if len(popular_word) > 1:   # 두개 이상이면 물음표 출력
    print("?")
else:                       # 하나인 경우 대문자 문자 출력
    pop_word = chr(65 + popular_word[0])
    print(pop_word)