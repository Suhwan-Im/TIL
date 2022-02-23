import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+ 1):
    test = str(input())
    rlt = 1

    stack = []
    for letter in test:
        # 여는 소괄호가 나오면 스택에 쌓기
        if letter == "(":
            stack.append("(")
        # 여는 중괄호가 나오면 스택에 쌓기
        elif letter == "{":
            stack.append("{")
        # 닫는 소괄호가 나올 경우
        elif letter == ")":
            # 스택의 맨 위에 여는 소괄호가 있다면 pop 해주기
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            # 그렇지 않다면 rlt값 0으로 바꾸고 반복문 종료
            else:
                rlt = 0
                break
        # 닫는 중괄호가 나올 경우
        elif letter == "}":
            # 스택의 맨 위에 여는 중괄호가 있다면 pop 해주기
            if len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            # 그렇지 않다면 rlt값 0으로 바꾸고 반복문 종료
            else:
                rlt = 0
                break

    # 반복문 종료 후, 스택에 괄호가 남아있으면 rlt값 0으로 바꾸기
    if len(stack) != 0:
        rlt = 0

    # 결과 출력
    print(f'#{tc} {rlt}')