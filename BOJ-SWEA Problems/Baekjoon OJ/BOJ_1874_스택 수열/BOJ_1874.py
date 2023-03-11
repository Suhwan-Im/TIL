import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
N_list = [int(input()) for _ in range(N)]
ans_list = []       # 스택의 push('+')와 pop('-') 기호를 담을 리스트
num_list = []       # 아직 매칭되지 않은 숫자를 담을 스택
idx = 0             # 수열의 인덱스를 트래킹하는 idx 변수 0으로 생성

# for문을 이용해 1~N 순서대로 숫자 대조하기
for num in range(1, N+1):
    # 현재 숫자와 수열 숫자 비교
    if num == N_list[idx]:
        ans_list.append('+')
        ans_list.append('-')
        idx += 1
    else:
        ans_list.append('+')
        num_list.append(num)
    
    # 스택에 넣어둔 숫자(뒤에서부터)를 수열 숫자와 비교
    while (len(num_list) > 0) and (num_list[-1] == N_list[idx]):
        idx += 1
        num_list.pop()
        ans_list.append('-')
    
    # 만약 N까지의 숫자를 돌았는데 스택에 숫자가 남아있으면, ans_list를 'NO'로 교체
    if (num == N) and (len(num_list) > 0):
        ans_list = ['NO']

# 결과 출력
for ans in ans_list:
    print(ans)