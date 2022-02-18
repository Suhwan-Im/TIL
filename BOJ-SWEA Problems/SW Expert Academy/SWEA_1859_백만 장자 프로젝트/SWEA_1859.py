import sys
sys.stdin = open('input.txt')


# mymax 함수 정의
def mymax(num_list):
    curr_max = -1e100
    for num in num_list:
        if num > curr_max:
            curr_max = num
    return curr_max


# myindex 함수 정의
def myindex(num_list, key):
    for i in range(len(num_list)):
        if num_list[i] == key:
            return i


# 테스트 케이스를 통한 코드 실행
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # while문과 for문을 이용해 수익 누적하기
    profit = 0                                  # 수익을 나타내는 profit 변수 0으로 설정
    while len(num_list) > 0:
        num_max = mymax(num_list)               # mymax함수 이용해 숫자리스트내 최댓값 구하기
        max_i = myindex(num_list, num_max)      # myindex함수 이용해 최대값의 인덱스 구하기
        for i in range(max_i):
            profit += num_list[max_i] - num_list[i]     # 최대값 이전의 숫자들의 (최댓값 - 현재값)을 profit 변수에 누적하기
        num_list = num_list[max_i + 1:]         # 숫자 리스트를 최댓값 이후의 리스트로 갱신하기

    # 결과 출력
    print(f'#{tc} {profit}')