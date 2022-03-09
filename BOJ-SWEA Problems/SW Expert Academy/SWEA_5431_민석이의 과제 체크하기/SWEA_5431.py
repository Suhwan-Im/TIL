import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    # 전체 학생 번호 리스트 만들기
    students = [x for x in range(1, N+1)]

    # for문을 이용해 과제를 제출한 학생은 리스트에서 제외하기
    for num in num_list:
        if num in students:
            students.remove(num)

    # 결과 출력
    print(f'#{tc}', *students[:])