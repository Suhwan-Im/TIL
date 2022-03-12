import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    num_max = -1 # 최대값을 담을 num_max 변수 -1로 생성 (단조 증가하는 수가 없으면 -1 반환)
    # for문을 이용해 모든 조합의 두 수의 곱 구하기
    for i in range(len(num_list)):
        for num_2 in num_list[i + 1:]:
            num_1 = num_list[i]
            mult_num = num_1 * num_2

            status = 0 # 단조 증가하는 수를 나타내는 status 변수 0으로 정의 (단조 증가하는 수일 경우 1)
            while mult_num != 0:
                digit = mult_num % 10       # 1의 자리수
                mult_num //= 10             # 1의 자리를 제거한 나머지 수
                digit_10 = mult_num % 10    # 10의 자리수
                if digit < digit_10:        # 만약 10의 자리수가 더 큰 경우 (단조 증가하는 수가 아닐 경우)
                    break                   # -> while문 종료
                elif mult_num == 0:         # 모든 자리수를 확인한 경우 (단조 증가하는 수인 경우)
                    status = 1              # -> status 변수를 1로 지정

            if status == 1:                 # 단조 증가하는 수인 경우
                mult_num = num_1 * num_2    # -> 두 수의 곱을 mult_num 변수에 다시 지정
                if mult_num > num_max:      # 두 수의 곱이 num_max의 값보다 큰 경우
                    num_max = mult_num      # -> num_max에 두 수의 곱을 갱신하기

    # 결과 출력
    print(f'#{tc} {num_max}')