import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    elif (B // A > 0) and (B % A == 0):
        print('factor')
    elif (A // B > 0) and (A % B == 0):
        print('multiple')
    else:
        print('neither')