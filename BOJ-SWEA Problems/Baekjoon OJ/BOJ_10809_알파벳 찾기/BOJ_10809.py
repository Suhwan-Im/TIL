import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
word = str(input())

# 이중 for문을 이용해 정답 리스트 만들기
ans_list = []   # 정답을 담을 ans_list 생성
for i in range(97, 123):    # 아스키코드를 이용해 소문자 a~z 순회
    for j in range(len(word)):  # 주어진 단어를 순회
        if ord(word[j]) == i:       # 주어진 단어중 현재 알파벳과 일치하는 경우,
            ans_list.append(j)          # -> 단어내의 위치를 ans_list에 누적 후 반복문 종료
            break
        elif len(word)-1 == j:      # 주어진 단어중 현재 알파벳이 없는 경우,
            ans_list.append(-1)         # -> ans_list에 -1 누적
            break

# 결과 출력
print(*ans_list[:])