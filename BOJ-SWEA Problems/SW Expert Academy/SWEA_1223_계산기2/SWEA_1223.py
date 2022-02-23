import sys
sys.stdin = open('input.txt')


T = 10
for tc in range(1, T + 1):
    N = int(input())
    calc_str = list(map(str, input()))

    ### 후위 표기식으로 바꾸기 ###

    postfix = ''            # 후위표기식을 담을 postfix 리스트 생성
    stack = []              # 스택 생성
    symbols = ["+", "*"]    # 연산기호를 담은 symbols 리스트 생성
    for s in calc_str:
        if s in symbols:    # 연산기호일 경우
            if len(stack) == 0:                 # 스택에 아무것도 없는 경우
                stack.append(s)                 # -> 기호 문자열을 스택에 push
            elif s == stack[-1]:                # 기호 문자열이 스택의 탑과 일치할 경우
                postfix += stack.pop()          # -> 스택탑을 pop하여 postfix에 추가
                if len(stack) != 0 and s == stack[-1]:  # 다음 스택탑이 기호 문자열과 또 일치할 경우
                    postfix += stack.pop()      # -> 다음 스택탑을 pop하여 postfix에 추가하고
                stack.append(s)                 # -> 기호 문자열은 스택에 push
            elif s == "+" and stack[-1] == "*": # 기호 문자열은 '+', 스택탑은 '*'일 경우
                postfix += stack.pop()          # -> 스택탑을 pop하여 postfix에 추가
                if len(stack) != 0 and s == stack[-1]:  # 다음 스택탑이 기호 문자열과 일치할 경우
                    postfix += stack.pop()      # -> 다음 스택탑을 pop하여 postfix에 추가하고
                stack.append(s)                 # -> 기호 문자열은 스택에 push
            elif s == "*" and stack[-1] == "+": # 기호 문자열은 '*', 스택탑은 '+'일 경우
                stack.append(s)                 # -> 기호 문자열을 스택에 push
        else:               # 숫자일 경우
            postfix += s    # -> postfix에 숫자 문자열 추가

    while len(stack) > 0:       # 스택에 기호 문자열이 남아있는 경우
        postfix += stack.pop()  # -> 남은 기호 문자열을 모두 postfix에 추가


    ### 후위 표기식 계산하기 ###

    stack = []              # 스택 생성
    symbols = ["+", "*"]    # 연산기호를 담은 symbols 리스트 생성
    for p in postfix:           # 후위 표기식으로 저장한 문자열 순서대로 불러오기
        if p not in symbols:    # 숫자일 경우
            stack.append(p)     # -> 스택에 push
        elif p == "+":                      # "+"일 경우
            num2 = int(stack.pop())         # 스택을 pop하고 int타입으로 num2 변수에 저장
            num1 = int(stack.pop())         # 스택을 pop하고 int타입으로 num1 변수에 저장
            stack.append(str(num1 + num2))  # num1과 num2의 합을 str타입으로 스택에 push
        elif p == "*":                      # "*"일 경우
            num2 = int(stack.pop())         # 스택을 pop하고 int타입으로 num2 변수에 저장
            num1 = int(stack.pop())         # 스택을 pop하고 int타입으로 num1 변수에 저장
            stack.append(str(num1 * num2))  # num1과 num2의 곱을 str타입으로 스택에 push

    # 스택에 남겨진 최종 계산값을 rlt변수에 저장
    rlt = stack[-1]


    # 결과 출력
    print(f'#{tc} {rlt}')