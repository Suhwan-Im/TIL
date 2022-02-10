import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input()))

    # 인덱스 리스트 생성
    index_list = [0] * 10

    # for문을 이용해 각 숫자의 카드개수 누적하기
    for num in num_list:
        index_list[num] += 1

    # for문과 if문을 이용해 카드개수가 가장 많은 숫자 찾기
    max_index = 0
    for i in range(len(index_list)):
        if index_list[i] >= index_list[max_index]:
            max_index = i

    # 가장 많은 숫자카드의 개수 구하기
    count = index_list[max_index]

    # 결과 출력
    print(f'#{tc} {max_index} {count}')