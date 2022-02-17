import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()

    # idx와 cnt변수 0으로 지정
    idx = 0
    cnt = 0
    # while문을 이용해 최소 타이핑 횟수 (cnt) 구하기
    while idx < len(A):
        # B와 일치하는 단어가 A에 있을경우, B의 갯수만큼 건너뛰고 진행
        if A[idx: idx + len(B)] == B:
            idx += len(B)
            cnt += 1
        # B와 일치하는 단어가 아니면 한칸 다음으로 가서 계속 진행
        else:
            idx += 1
            cnt += 1

    # 결과 출력
    print(f'#{tc} {cnt}')