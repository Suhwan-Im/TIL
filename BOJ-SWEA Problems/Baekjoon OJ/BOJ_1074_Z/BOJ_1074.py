import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N, r, c = map(int, input().split())

num = 0                 # 정답을 담을 num 변수 생성
half_len = 2 ** (N-1)   # 한 변의 절반 길이를 담을 half_len 변수 생성

# while 문을 이용해 위치 탐색하며 숫자 누적해가기
while half_len:
    if (r < half_len) and (c < half_len):       # 2 사분면
        pass
    elif (r < half_len) and (c >= half_len):    # 1 사분면
        num += (half_len ** 2)
        c -= half_len
    elif (r >= half_len) and (c < half_len):    # 3 사분면
        num += 2 * (half_len ** 2)
        r -= half_len
    elif (r >= half_len) and (c >= half_len):   # 4 사분면
        num += 3 * (half_len ** 2)
        r -= half_len
        c -= half_len

    if half_len == 1:
        break
    else:
        half_len //= 2

# 결과 출력
print(num)