import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    max_cnt = 0

    # for문을 이용해 str1의 단어 하나씩 str2에 대조해가며 갯수 구하기
    for key in str1:
        cnt_key = 0
        for letter in str2:
            if key == letter:
                cnt_key += 1
        # if문을 이용해 가장 많은 갯수 갱신하기
        if cnt_key > max_cnt:
            max_cnt = cnt_key

    # 결과 출력
    print(f'#{tc} {max_cnt}')