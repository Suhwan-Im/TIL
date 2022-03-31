import sys
sys.stdin = open('input.txt')


# 퀵 정렬 함수 정의
def quicksort(A, left, right):
    if left < right:
        s = partition(A, left, right)
        quicksort(A, left, s-1)
        quicksort(A, s+1, right)

# 피봇값을 기준으로 두 부분으로 분류하는 함수 정의
def partition(A, left, right):
    p = A[left]
    i, j = left, right
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[left], A[j] = A[j], A[left]
    return j

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # 퀵 정렬 함수 이용
    quicksort(num_list, 0, N-1)

    # 결과 출력
    print(f'#{tc} {num_list[N//2]}')