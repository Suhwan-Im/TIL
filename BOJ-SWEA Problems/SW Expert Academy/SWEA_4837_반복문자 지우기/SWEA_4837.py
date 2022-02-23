import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    text = str(input())

    # 스택 생성
    stack = []
    # 주어진 글자를 하나씩 대조하기
    for t in text:
        if len(stack) == 0:     # 스택이 비어있으면 스택에 넣기
            stack.append(t)
        elif t == stack[-1]:    # 주어진 글자가 스택의 맨 위의 글자와 일치하면 둘다 제거
            stack.pop()
        else:                   # 그렇지 않으면, 스택에 이어서 쌓기
            stack.append(t)

    rlt = len(stack)            # 반복문 종료 후, 스택의 길이를 rlt 변수에 저장

    # 결과 출력
    print(f'#{tc} {rlt}')