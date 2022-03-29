import sys
sys.stdin = open('input.txt')


# babygin 함수 정의
def babygin(L):
    nums = [0] * 10         # 0~9의 숫자카드의 개수를 담을 nums 리스트 생성
    for n in L:             # 입력받은 리스트의 숫자 순회
        nums[n] += 1        # 각 숫자를 인덱스로 하여 nums에 개수 누적해주기
    for num in nums:        # for문을 이용해 triplet 검색
        if num >= 3:        # 같은 숫자가 3개 이상 있는 경우
            return True     # -> True를 반환
    for i in range(len(nums)-2):                                # for 문을 이용해 run 검색
        if nums[i] >= 1 and nums[i+1] >= 1 and nums[i+2] >= 1:  # 만약 숫자 세개가 연속인 경우
            return True                                         # -> True를 반환

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int, input().split()))

    p1, p2 = [], []     # 두 플레이어의 덱을 의미하는 p1, p2라는 빈 리스트 생성
    result = 0          # 승자를 넣어줄 result 변수를 0으로 생성

    # 일단 2장의 카드를 먼저 배분해주기
    for _ in range(2):
        p1.append(num_list.pop(0))      # 플레이어 1
        p2.append(num_list.pop(0))      # 플레이어 2

    # while 문을 이용해 승자 찾기
    while len(num_list) > 0:            # num_list에 숫자가 남아있으면 while 문 반복
        p1.append(num_list.pop(0))      # 플레이어 1 에게 카드 한장 배분
        if babygin(p1):                 # 만약 현재 플레이어 1 의 카드에 run이나 triplet이 있으면,
            result = 1                  # -> result 값을 1로 갱신
            break                       # -> 반복문 종료
        p2.append(num_list.pop(0))      # 플레이어 2 에게 카드 한장 배분
        if babygin(p2):                 # 만약 현재 플레이어 2 의 카드에 run이나 triplet이 있으면,
            result = 2                  # -> result 값을 2로 갱신
            break                       # -> 반복문 종료

    # 결과 출력
    print(f'#{tc} {result}')