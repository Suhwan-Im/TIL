import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
words = []

for _ in range(N):
    word = str(input())
    if word not in words:
        words.append(word)

# 단어들을 사전순으로 정렬하기
words = sorted(words)

# 단어들을 길이 순으로 정렬하기
fin_list = []       # 최종으로 정렬된 단어를 담을 fin_list 생성
length = 0          # 1씩 증가하는 단어길이를 나타낼 length 변수 생성
while len(fin_list) < len(words):       # while문을 이용해 사전순으로 정렬된 단어들을 길이순으로 정렬하기
    length += 1
    for word in words:
        if len(word) == length:
            fin_list.append(word)

# 결과 출력
for word in fin_list:
    print(word)