import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N = int(input())
nums = list(map(int, input().split()))
stack = []  # 순서가 다른 숫자를 담을 빈 스택 생성
n = 0       # 대기줄을 순회할 n값 생성
i = 1       # 스택을 순회할 i값 생성
nice = 1    # 결과 스위치 nice 변수 생성

# while 문을 이용해 가능여부 확인
while i <= N:
    if (n < N) and (nums[n] == i):  # 대기줄 맨 앞 숫자가 현재 순서인 경우,
        i += 1                          # -> i값 1 증가
        n += 1                          # -> n값 1 증가
    elif len(stack) == 0:           # 스택이 비어있을 경우,
        stack.append(nums[n])           # -> 스택에 대기줄 맨 앞 숫자 넣기
        n += 1                          # -> n값 1 증가
    elif stack[-1] == i:            # 스택의 맨 뒷 사람이 현재 순서인 경우,
        i += 1                          # -> i값 1 증가
        stack.pop()                     # -> 스택의 맨 뒷 숫자 제거
    elif stack[-1] > nums[n]:       # 스택의 맨 뒷 숫자가 대기줄 맨 앞 숫자보다 큰 경우,
        stack.append(nums[n])           # -> 스택에 대기줄 맨 앞 숫자 넣기
        n += 1                          # -> n값 1 증가
    else:                           # 그 외의 경우,
        nice = 0                        # -> 결과 스위치 nice 변수를 0으로 설정
        break                           # -> while 문 종료

# 결과 출력
if nice == 1:
    print("Nice")
else:
    print("Sad")