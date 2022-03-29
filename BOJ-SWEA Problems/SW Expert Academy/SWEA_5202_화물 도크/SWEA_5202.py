import sys
sys.stdin = open('input.txt')


# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]

    # times 리스트를 종료시간 오름차순으로 정렬
    times_sort = []                 # 종료시간을 기준으로 정렬된 시간들을 담을 times_sort 리스트 생성
    temp_stack = []                 # 정렬 과정에서 사용할 임시 리스트 생성
    for t in times:                 # for 문을 이용해 모든 신청 시간을 조회하기
        if len(times_sort) == 0:    # times_sort 리스트가 비어있는 경우 (첫번째 사이클에만 해당)
            times_sort.append(t)    # -> 현재 신청 시간을 times_sort 리스트에 넣기
        else:                                                           # (두번째 사이클 부터는)
            while len(times_sort) > 0 and times_sort[-1][1] > t[1]:     # times_sort의 맨 마지막 원소의 종료시간이 현재 신청시간의 종료시간보다 더 큰 경우,
                temp_stack.append(times_sort.pop())                     # 해당 신청시간들을 모두 temp_sort 리스트에 역순으로 쌓은 후
            times_sort.append(t)                                        # 현재 신청시간을 times_sort 리스트에 넣기
            while temp_stack:                                           # temp_sort 리스트에 임시로 저장했던 신청시간들을
                times_sort.append(temp_stack.pop())                     # 아까와 일치하는 순서대로 다시 times_sort 리스트에 넣기

    # 종료시간을 기준으로 이용 가능 개수 누적해가기
    cnt = 0                             # 이용 가능한 화물차의 대수를 누적할 cnt 변수를 0으로 생성
    end_time = 0                        # 종료시간을 갱신해 줄 end_time 변수를 0으로 생성
    while times_sort:                   # while 문을 이용해 개수 누적하기
        curr_times = times_sort.pop(0)  # times_sort 리스트의 앞에서부터 신청시간을 꺼내서 curr_times 변수에 저장
        if curr_times[0] >= end_time:   # 현재 신청시간의 시작시간이 기존 종료시간 이후인 경우 (같은 경우도 포함)
            end_time = curr_times[1]    # end_time을 현재 신청시간의 종료시간으로 갱신하기
            cnt += 1                    # 이용 가능한 화물차의 대수를 1 증가 시키기

    # 결과 출력
    print(f'#{tc} {cnt}')