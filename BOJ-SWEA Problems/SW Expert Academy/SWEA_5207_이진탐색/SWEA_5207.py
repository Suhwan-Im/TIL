import sys
sys.stdin = open('input.txt')


# 이진 탐색 함수 정의
def binarysearch(N, N_list, key):
    global cnt
    left = 0
    right = N-1
    status = 0              # 왼쪽과 오른쪽을 번갈아가며 탐색하는지 트래킹할 status 변수를 0으로 생성
    while left <= right:
        mid = (right + left) // 2   # 중앙값 mid 변수 지정
        if N_list[mid] == key:      # 키값이 중앙값과 같으면,
            cnt += 1                # -> cnt 변수 1 증가
            break                   # -> 반복문 종료
        elif N_list[mid] > key:     # 키값이 중앙값보다 작으면,
            right = mid - 1         # -> right 값을 중앙값 직전값으로 변경
            if status != 1:         # -> 이때, status 가 1이 아닐때 (이전 탐색이 좌측이 아닌경우)
                status = 1          # -> -> status 변수를 1로 지정
            else:                   # -> 이전 탐색도 좌측이었던 경우
                break               # -> -> 반복문 종료
        elif N_list[mid] < key:     # 키값이 중앙값보다 크면,
            left = mid + 1          # -> left 값을 중앙값 직후값으로 변경
            if status != -1:        # -> 이때, status 가 -1이 아닌래 (이전 탐색이 우측이 아닌경우)
                status = -1         # -> -> status 변수를 -1로 지정
            else:                   # -> 이전 탐색도 우측이었던 경우
                break               # -> -> 반복문 종료

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    # N_list를 sort 함수 이용해서 정렬하기
    N_list.sort()

    # for 문과 이진탐색 함수를 이용해서 결과값 구하기
    cnt = 0                         # 조건에 일치하는 값의 개수를 담을 cnt 변수를 0으로 생성
    for m in M_list:
        binarysearch(N, N_list, m)

    # 결과 출력
    print(f'#{tc} {cnt}')