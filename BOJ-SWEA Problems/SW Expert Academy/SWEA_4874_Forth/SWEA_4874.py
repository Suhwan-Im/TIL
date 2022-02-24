import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    cal_str = list(map(str, input().split()))

    stack = []                          # 피연산자를 담을 빈스택 생성
    symbols = ["+", "-", "*", "/"]      # 연산기호를 담고있는 symbols 리스트 생성
    for s in cal_str:
        if s == ".":                    # s가 "."인 경우, stack의 값을 rlt변수에 반환하기
            if len(stack) > 1:          # -> 만약 stack에 숫자가 1개 이하이면, rlt값에 "error"를 반환하고 반복문 종료
                rlt = "error"
                break
            rlt = stack.pop()
        elif s not in symbols:          # s가 연산기호가 아닌경우, stack에 int형으로 push
            stack.append(int(s))
        elif s in symbols:              # s가 연산기호인 경우
            if len(stack) <= 1:         # -> 만약 stack에 숫자가 1개 이하이면, rlt값에 "error"를 반환하고 반복문 종료
                rlt = "error"
                break
            num2 = stack.pop()          # stack에서 pop하여 num2변수에 저장
            num1 = stack.pop()          # stack에서 pop하여 num1변수에 저장
            if s == "+":                # s가 "+"인 경우, num1 + num2의 값을 stack에 push
                stack.append(int(num1 + num2))
            elif s == "-":              # s가 "-"인 경우, num1 - num2의 값을 stack에 push
                stack.append(int(num1 - num2))
            elif s == "*":              # s가 "*"인 경우, num1 * num2의 값을 stack에 push
                stack.append(int(num1 * num2))
            elif s == "/":              # s가 "/"인 경우, num1 / num2의 값을 stack에 push
                stack.append(int(num1 / num2))

    # 결과 출력
    print(f'#{tc} {rlt}')