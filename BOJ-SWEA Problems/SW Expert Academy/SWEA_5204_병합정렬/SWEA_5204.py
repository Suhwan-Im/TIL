import sys
sys.stdin = open('input.txt')


# 분할 함수 정의
def merge_sort(L):
    global cnt
    if len(L) == 1:
        return L

    left, right = [], []
    mid = int(len(L) // 2)
    for idx1 in range(0, mid):
        left.append(L[idx1])
    for idx2 in range(mid, len(L)):
        right.append(L[idx2])

    if len(left) > 0 and len(right) > 0 and left[-1] > right[-1]:
        cnt += 1

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# 병합 함수 정의
def merge(left, right):
    rlt = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                rlt.append(left.pop(0))
            else:
                rlt.append(right.pop(0))
        elif len(left) > 0:
            rlt.append(left.pop(0))
        elif len(right) > 0:
            rlt.append(right.pop(0))
    return rlt


# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    cnt = 0
    s_list = merge_sort(num_list)
    ans = s_list[len(s_list)//2]

    # 결과 출력
    print(f'#{tc} {ans} {cnt}')