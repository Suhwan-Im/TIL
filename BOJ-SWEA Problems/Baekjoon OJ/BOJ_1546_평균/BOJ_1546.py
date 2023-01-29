import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)

# for문을 이용해 새로운 점수 리스트 만들기
new_scores = []
for score in score_list:
    new_scores.append(score/max_score * 100)

# 결과 계산 및 출력
new_mean = sum(new_scores) / N
print(new_mean)