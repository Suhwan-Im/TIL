import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
num_list = list(map(int, input().split()))

no_ans = 0  # 소수가 아닌 숫자의 개수를 담을 no_ans 변수 생성
for num in num_list:
    if num == 1:        # 1은 소수가 아니므로 no_ans 값 1 증가
        no_ans += 1
    elif num == 2:      # 2는 소수이므로 패스
        pass
    elif (num % 2) > 0: # 3 이상인 숫자중 2로 나누었을때 나머지가 생기는 경우
        div = 3
        new_num = num
        while new_num > div:    # while문을 통해 중복되기 전까지 3, 4, 5.. 로 나누어보기
            if (num % div) == 0:
                no_ans += 1
                break
            else:
                new_num = num // div
                div += 1
    else:               # 3 이상인 숫자중 2로 나누어지는 숫자면 no_ans 값 1 증가
        no_ans += 1

# 정답 출력 (전체 숫자 개수 중 소수가 아닌 숫자의 개수를 제외한 수)
print(len(num_list) - no_ans)