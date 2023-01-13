import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
T = int(input())

# for문을 이용해 새로운 문자열 P 만들기
for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)
    P = str()
    for string in S:
        P += string * R

    # 결과 출력
    print(P)