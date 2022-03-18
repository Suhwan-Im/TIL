import sys
sys.stdin = open('input.txt')


# 후위 순회로 피연산자와 연산자를 채워주는 함수 만들기
def postorder(T):
    if T:
        postorder(cl[T])
        postorder(cr[T])
        calc.append(num_list[T])

# input값 입력하기
T = 10
for tc in range(1, T+1):
    N = int(input())

    num_list = [0] * (N+1)  # 연산자와 피연산자를 받을 num_list 리스트 생성
    cl = [0] * (N+1)        # 왼쪽 자식 노드 리스트 생성
    cr = [0] * (N+1)        # 오른쪽 자식 노드 리스트 생성

    # for문을 이용해 연산자와 피연산자, 트리 노드 정보들을 알맞은 리스트에 누적
    for _ in range(N):
        val = list(input().split())
        if len(val) == 2:                           # input 값이 두개인 경우
            num_list[int(val[0])] = float(val[1])   # -> num_list에 피연산자 누적 (float 타입)
        else:                                       # input 값이 네개인 경우
            num_list[int(val[0])] = str(val[1])     # -> num_list에 연산자 누적 (str 타입)
            cl[int(val[0])] = int(val[2])           # -> 부모 노드 번호를 왼쪽 자식 노드 리스트에 넣기
            cr[int(val[0])] = int(val[3])           # -> 부모 노드 번호를 오른쪽 자식 노드 리스트에 넣기

    calc = []       # 연산자와 피연산자를 계산할 순서로 담을 calc 리스트 생성
    postorder(1)    # 후위 순회 함수를 이용해 calc 리스트에 담기

    calc_stack =[]  # 계산을 할때 활용할 calc_stack 이라는 빈 스택 생성

    # while문을 이용해 계산 진행하기
    while calc:
        curr = calc.pop(0)              # calc 리스트에서 첫번째 인자 꺼내기
        if type(curr) == float:         # 꺼낸 인자가 숫자인 경우,
            calc_stack.append(curr)     # -> 해당 숫자를 calc_stack 에 쌓기
        else:                           # 꺼낸 인자가 연산자인 경우,
            num2 = calc_stack.pop()     # calc_stack에서 숫자를 꺼내서 num2로 지정
            num1 = calc_stack.pop()     # calc_stack에서 숫자를 꺼내서 num1으로 지정
            if curr == '+':                         # 인자가 + 인 경우,
                calc_stack.append(num1 + num2)      # -> 두 수의 합을 calc_stack에 쌓기
            elif curr == '-':                       # 인자가 - 인 경우,
                calc_stack.append(num1 - num2)      # -> 두 수의 차를 calc_stack에 쌓기
            elif curr == '*':                       # 인자가 * 인 경우,
                calc_stack.append(num1 * num2)      # -> 두 수의 곱을 calc_stack에 쌓기
            elif curr == '/':                       # 인자가 / 인 경우,
                calc_stack.append(num1 / num2)      # -> 두 수의 비를 calc_stack에 쌓기

    rlt = int(calc_stack[0])    # calc_stack에 남아있는 하나의 숫자를 int 형식으로 변환 후, rlt 변수에 저장

    # 결과 출력
    print(f'#{tc} {rlt}')