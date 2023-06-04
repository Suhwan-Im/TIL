import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N, B = map(int, input().split())
digits = []     # 각 자리수를 (역순으로) 저장할 digits 리스트 생성
ans = ''        # 최종 정답을 담을 ans 변수 생성

# while 문을 이용해서 뒷 자리수부터 구하기
while N > 0:
    d = N % B
    N = N // B
    digits.append(d)

# B 진법으로 변환하기
for i in range(len(digits)-1, -1, -1):
    if digits[i] > 9:
        ans += chr(digits[i] + 55)
    else:
        ans += str(digits[i])

# 정답 출력
print(ans)

#35 --> Z
#36 --> 10
#71 --> 1Z
#72 --> 20