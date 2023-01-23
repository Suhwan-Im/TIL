import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
ppl_list = []
for _ in range(N):
    person = list(map(int, input().split()))
    ppl_list.append(person)

# 이중 for문을 이용해 각 사람의 덩치 랭킹 구하기
ans_list = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if (ppl_list[i][0] < ppl_list[j][0]) and (ppl_list[i][1] < ppl_list[j][1]):
                rank += 1
    ans_list.append(rank)

# 결과 출력
print(*ans_list[:])