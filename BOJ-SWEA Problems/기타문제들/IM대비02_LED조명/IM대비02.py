import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rlt_list = list(map(int, input().split()))

    light_list = [0] * N    # 현재 전등 상태를 반영하는 light_list 생성
    cnt = 0                 # 전등 조작 횟수를 세는 cnt 변수 생성

    # for문을 사용하여 패턴의 전등을 순서대로 확인하며 현재 전등 리스트와 비교하기
    for i in range(len(rlt_list)):
        # 패턴의 전등상태와 현재 전등 리스트가 일치하는 경우 반복문 종료
        if rlt_list == light_list:
            break
        # 패턴의 전등 상태와 현재 전등상태가 다를 경우, 전등을 조작하기
        elif (rlt_list[i] == 1 and light_list[i] == 0) or (rlt_list[i] == 0 and light_list[i] == 1):
            s = i + 1       # 스위치 숫자
            cnt += 1        # 전등 조작 횟수 누적하기
            for j in range(s-1, N, s):      # 스위치번호 이후의 전등 중 번호의 배수만 골라서 조작
                if light_list[j] == 0:      # 불이 꺼져있는 경우
                    light_list[j] = 1       # -> 불 켜기
                elif light_list[j] == 1:    # 불이 켜져있는 경우
                    light_list[j] = 0       # -> 불 끄기
        # 위의 조건이 아닌 경우, 다음 전등으로 이동
        else:
            pass

    # 결과 출력
    print(f'#{tc} {cnt}')