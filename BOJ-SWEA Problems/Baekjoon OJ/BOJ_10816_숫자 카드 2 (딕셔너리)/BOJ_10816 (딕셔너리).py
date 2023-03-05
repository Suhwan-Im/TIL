import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

fin_list = []       # 각 수가 적힌 숫자카드의 갯수를 담을 fin_list 생성

# 딕셔너리를 활용하여 문제 풀기
dic = dict()

for n in N_list:        # N_list를 순회하며 해당 숫자의 개수를 딕셔너리에 누적시키기
    try:                # 이미 딕셔너리에 정의되어 있는 경우
        dic[n] += 1         # -> 개수 1 증가
    except:             # 딕셔너리에 정의되지 않은 경우
        dic[n] = 1          # -> 개수를 1로 생성

for m in M_list:        # M_list를 순회하며 정답 개수를 fin_list에 누적하기
    try:                        # 딕셔너리에 등록 된 숫자인 경우
        fin_list.append(dic[m])     # -> 숫자의 개수를 fin_list에 누적
    except:                     # 딕셔너리에 없는 숫자인 경우
        fin_list.append(0)          # -> 0을 fin_list에 누적

# 결과 출력
print(*fin_list[:])