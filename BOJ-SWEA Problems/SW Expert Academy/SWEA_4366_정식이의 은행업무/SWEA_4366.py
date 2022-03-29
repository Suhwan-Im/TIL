import sys
sys.stdin = open('input.txt')


# solve 함수 생성
def solve(lst2, lst3):
    for i in range(len(lst2)):
        # 1비트 값만 바꿔서 10진수 값으로 변환하기
        lst2[i] = (lst2[i]+1) % 2

        # 10진수로 변환
        dec = 0
        for idx in range(len(lst2)):
            dec = dec*2 + lst2[idx]
        
        # 3진수로 변환
        s = []
        ret = dec
        while dec > 0:
            s.append(dec % 3)
            dec //= 3
            
        lst3 = lst3[::-1]           # lst3 뒤집기
        
        cnt = 0
        for idx in range(min(len(s), len(lst3))):
            if s[idx] != lst3[idx]:
                cnt += 1
        cnt += abs((len(s) - len(lst3))) # 길이의 차 더해주기

        if cnt == 1:
            return ret

        lst2[i] = (lst2[i]+1) % 2   # 원상복구

# input값 입력하기
T = int(input())
for tc in range(1, T+1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))

    ans = solve(lst2, lst3)     # solve 함수 사용

    # 결과 출력
    print(f'#{tc} {ans}')