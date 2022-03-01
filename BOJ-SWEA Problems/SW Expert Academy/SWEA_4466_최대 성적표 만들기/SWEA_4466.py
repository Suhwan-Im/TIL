import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+ 1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    sum_score = 0       # 최고 점수들의 합을 담을 sum_score 변수 0으로 생성
    for i in range(K):
        sum_score += max(num_list)          # 최고 점수를 sum_score변수에 누적 (max 함수 사용)
        num_list.remove((max(num_list)))    # num_list에서 최고 점수 삭제하기 (remove 메서드 사용)

    # 결과 출력
    print(f'#{tc} {sum_score}')