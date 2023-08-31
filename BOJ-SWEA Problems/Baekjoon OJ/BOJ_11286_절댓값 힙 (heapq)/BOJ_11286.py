import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입려 받기
N = int(input())
heap = []

# for문을 이용해 한줄씩 진행
for _ in range(N):
    num = int(input())              # input 숫자 입력 받기

    # 숫자가 0인 경우,
    if num == 0:
        if heap:                            # heap에 숫자가 있다면,
            ans = heapq.heappop(heap)           # -> heapq를 이용해 heap 리스트에서 숫자 꺼내기
            if ans[1] < 0:                      # -> 꺼낸 숫자가 음수인 경우,
                print(ans[0] * (-1))                # -> 음수로 출력
            else:                               # -> 꺼낸 숫자가 양수인 경우,
                print(ans[0])                       # -> 숫자 그대로 출력
        else:                               # heap에 숫자가 없다면,
            print(0)                            # -> 0 출력
    # 숫자가 양수인 경우,
    elif num > 0:
        heapq.heappush(heap, (num, 1))      # heap 리스트에 (숫자, 1)의 양식으로 삽입
    # 숫자가 음수인 경우,
    elif num < 0:
        heapq.heappush(heap, (abs(num), -1))    # heap 리스트에 (절댓값, -1)의 양식으로 삽입