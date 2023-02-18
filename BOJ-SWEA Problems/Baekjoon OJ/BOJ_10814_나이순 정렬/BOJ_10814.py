import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
stack = []

for i in range(N):
    member = list(map(str, input().split()))
    member.append(i+1)
    stack.append(member)

mem_list = sorted(stack, key=lambda x: (int(x[0]), x[2]))

for member in mem_list:
    print(int(member[0]), member[1])