import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
A, B, V = map(int, input().split())

if A == V:              # 만약 A=V인 경우, 하루만에 정상 등반
    day = 1
elif (V-A) > (A-B):     # 일반적인 경우 (V-A) 보다 일일등반량이 적은 경우, 계산
    day = (V-A) // (A-B)
    if (V-A) % (A-B) > 0:   # 나머지가 있는 경우, 나머지 등반일 + 마지막날 등반 추가 (총 2일 추가)
        day += 2
    else:                   # 나머지가 없는 경우, 마지막날 등반만 추가 (총 1일 추가)
        day += 1
elif (V-A) < (A-B):     # V-A 보다 일일등반량이 클 경우, 이틀만에 등반
    day = 2

print(day)