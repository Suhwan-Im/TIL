import sys
sys.stdin = open('input.txt')


# my_max 함수 정의 (숫자 리스트에서 가장 큰 값을 반환)
def my_max(num_list):
    max_num = -1e100
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num


# 테스트 케이스를 통한 코드 실행
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    # 접근 방식:
    # 1. 전체 방의 갯수(400개)를 2로 나눈 길이 200의 0 리스트인 cnt_list를 만든다
    # 2. (각 방번호 - 1) // 2 값을 시작인덱스와 끝인덱스로 놓고 사이에 위치한 모든 값을 cnt_list에 1씩 증가시켜준다
    # 3. N번의 반복문이 종료되면 cnt_list내에 최댓값을 결과로 리턴한다 (학생이 지나갈때 중복되는 복도의 중복횟수)

    cnt_list = [0] * 200
    for nums in num_list:
        if nums[0] == nums[1]:
            pass
        elif nums[0] < nums[1]:
            for i in range((nums[0] - 1) // 2, ((nums[1] - 1) // 2) + 1):
                cnt_list[i] += 1
        else:
            for i in range((nums[1] - 1) // 2, ((nums[0] - 1) // 2) + 1):
                cnt_list[i] += 1

    rlt = my_max(cnt_list)

    # 결과 출력
    print(f'#{tc} {rlt}')