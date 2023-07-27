import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
M = int(input())
S = set()  # 세트 생성

# for문을 이용해 한 줄씩 연산 수행
for _ in range(M):
    # 입력값 받기
    textline = list(map(str, input().split()))
    try:        # '명령+숫자' 양식
        command, num = textline[0], int(textline[1])
    except:     # '명령' 양식
        command = textline[0]

    # add 명령어
    if command == "add":
        if num not in S:
            S.add(num)

    # remove 명령어
    elif command == "remove":
        if num in S:
            S.remove(num)

    # check 명령어
    elif command == "check":
        if num in S:
            print(1)
        else:
            print(0)

    # toggle 명령어
    elif command == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)

    # all 명령어
    elif command == "all":
        S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    # empty 명령어
    elif command == "empty":
        S = set()