import sys
sys.stdin = open('input.txt')


# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))

    # 두 리스트를 내림차순으로 정렬하기
    w_list.sort(reverse=T)
    t_list.sort(reverse=T)

    # while 문을 이용해 실을 수 있는 화물의 최대무게 구하기
    weight = 0          # 화물의 총 무게를 담을 weight 변수를 0으로 생성
    while w_list:       # w_list 에 원소가 있다면 반복문 진행
        if len(t_list) == 0:            # 더 이상 트럭이 남아있지 않다면,
            break                       # -> 반복문 종료
        elif w_list[0] <= t_list[0]:    # 현재 가장 무거운 화물이 현존 최대 적재량 트럭보다 가벼우면,
            weight += w_list[0]         # -> 화물의 총 무게를 나타내는 weight 변수에 현재 화물의 무게 누적
            w_list.pop(0)               # -> 현재 화물의 무게를 리스트에서 제거
            t_list.pop(0)               # -> 현재 트럭의 적재무게를 리스트에서 제거
        elif w_list[0] > t_list[0]:     # 현재 가장 무거운 화물이 현존 최대 적재량 트럭보다 무거우면,
            w_list.pop(0)               # -> 현재 화물의 무게를 리스트에서 제거

    # 결과 출력
    print(f'#{tc} {weight}')