import sys
sys.stdin = open('input.txt')

# while문을 이용해 테스트케이스 진행
while True:
    num = int(input())

    # -1이 나오면 반복문 종료
    if num == -1:
        break

    # 그렇지 않으면 정답 구하기
    else:
        min, max = 1, int(num ** (1 / 2))
        factors = []

        # for문을 이용해서 약수 구하기
        for i in range(min, max + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(int(num / i))

        # 만약 마지막으로 찾은 두 약수가 같은 경우 하나 제거 (9의 약수로 3x3을 찾은 경우 등)
        if factors[-2] == factors[-1]:
            factors.pop()

        # 약수들 오름차순으로 정렬 후 초기숫자 제거 (맨 뒤의 숫자)
        factors = sorted(factors)
        factors.pop()

        # 약수의 합이 초기숫자와 같은 경우, '초기값 = 약수1 + 약수2 + ...' 출력
        if sum(factors) == num:
            print(f'{num} = {" + ".join(map(str, factors))}')
        # 약수의 합이 초기숫자와 다른 경우, '초기값 is NOT perfect.' 출력
        else:
            print(f'{num} is NOT perfect.')