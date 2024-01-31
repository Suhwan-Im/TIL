import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N = int(input())
M = int(input())
S = str(input())

### 이 방법은 부분통과 (두번째 조건에서 시간초과)
# # 정답 문자열 생성하기
# ans = "I" + ("OI" * N)
# count = 0
#
# # for 문을 이용해 S를 순회하며 정답 문자열과 일치하는 개수 구하기
# for i in range(0, M-(N*2)):
#     if S[i:i+(N*2)+1] == ans:
#         count += 1

i = 0           # 인덱스 정보를 담을 변수 생성
sub_cnt = 0     # 중간 개수를 담을 변수 생성 (sub_cnt는 'I' 뒤에 붙는 'OI'의 개수와 동일)
ans_cnt = 0     # 최종 개수를 담을 변수 생성

# while 문을 이용해 정답 개수 찾기
while i < M-1:
    if S[i:i+3] == "IOI":   # 문자열을 순회하며 3단어씩 조회하기, 만약 해당 문자열이 "IOI"라면,
        i += 2                  # -> 인덱스 2 증가 ("IOI"의 세번째 "I"에서 다음 "IOI" 찾기)
        sub_cnt += 1            # -> 중간 개수 1 증가

        if sub_cnt == N:        # 만약 중간 개수가 N값과 같다면 (정답 문자열과 같다면)
            sub_cnt -= 1            # -> 중간 개수 1 감소 (누적된 문자열의 첫 "IOI"를 제거하는 의미 -> 이후 누적될 "IOI"의 개수를 세기 위함)
            ans_cnt += 1            # -> 최종 개수 누적

    else:                   # 해당 문자열이 "IOI"가 아니라면,
        i += 1                  # -> 인덱스 1 증가
        sub_cnt = 0             # -> 중간 개수 리셋

# 결과 출력
print(ans_cnt)