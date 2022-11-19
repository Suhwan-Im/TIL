# 한수를 구하는 함수 정의
def han_num(N):
    if N <= 99:         # 입력값이 99 이하면 입력한 수가 한수
        return N
    else:               # 입력값이 100 이상이면 함수 개수 찾기
        cnt = 99        # 99까지의 한수 개수를 cnt 변수에 저장
        num_list = list(range(100, N+1))    # 100부터 N까지의 값을 num_list로 생성
        for num in num_list:                # num_list 순회하며 한수 개수 더하기
            num_str = str(num)
            diff = int(num_str[1]) - int(num_str[0])    # 앞의 두 숫자의 차이를 diff 변수에 저장
            switch = 0                                  # 한수임을 판단할 switch 변수 생성 및 0으로 리셋
            for i in range(1, len(num_str)-1):          # 숫자의 자릿수를 순회하며 연속된 두 자리 숫자의 차이 비교
                if (int(num_str[1+1]) - int(num_str[i])) == diff:   # 두 자리 숫자의 차이가 이전과 같을경우
                    switch = 1                                      # -> switch 값을 1로 변경
                else:                                               # 두 자리 숫자의 차이가 이전과 다를경우
                    switch = 0                                      # -> switch 값을 0으로 변경 후
                    break                                           # -> 해당 반복문 종료
            if switch == 1:         # 최종 switch 값이 1일 경우
                cnt += 1            # -> 한수 개수 1 증가
        return cnt              # 최종 한수 개수 반환


# input값 입력 받기
N = int(input())

# 한수를 구하는 함수 이용하여 결과값 출력하기
print(han_num(N))