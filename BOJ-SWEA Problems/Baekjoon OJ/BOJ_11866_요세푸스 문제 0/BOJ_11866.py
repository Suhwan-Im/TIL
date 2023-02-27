import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N, K = map(int, input().split())
num_list = [i for i in range(1, N+1)]       # 1에서 N까지의 숫자를 담는 num_list 생성
check_list = [1 for _ in range(N)]          # 유효한 숫자인지 확인할 1의 check_list 생성
ans_list = []                               # 요세푸스 순열을 담을 ans_list 생성

pos = 0                             # 현재 위치를 트래킹할 pos 변수 0으로 생성
while len(ans_list) < N:            # 모든 순열을 찾기 전까지 반복문 순회
    cnt = 0                             # K번째 숫자를 찾을 cnt 변수 0으로 생성
    while cnt < K:                      # K번째 숫자 이전까지 반복문 순회
        if check_list[pos] == 1:            # 아직 유효한 숫자이면,
            cnt += 1                            # -> cnt 1 증가
            if cnt == K:                        # 현재 숫자가 K번째 순서이면,
                ans_list.append(num_list[pos])      # -> ans_list에 해당 숫자 누적
                check_list[pos] = 0                 # -> check_list에 해당 인덱스 0으로 갱신
        pos = (pos + 1) % N                 # 현재 위치 1 이동

# 결과 출력 (문제가 요구하는 양식으로 만들기)
answer = "<"
for ans in ans_list[:-1]:
    answer += (str(ans) + ", ")
answer += (str(ans_list[-1]) + ">")

print(answer)