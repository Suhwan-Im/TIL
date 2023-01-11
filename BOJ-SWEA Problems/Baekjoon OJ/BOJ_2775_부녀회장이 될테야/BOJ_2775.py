import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
T = int(input())
num_set = []
for _ in range(T):
    k = int(input())
    n = int(input())
    num_set.append([k, n])

# Test case 순회
for nums in num_set:
    # 층별 거주민 수를 담을 ans_set 생성 (초기값은 0층)
    ans_set = []
    people = 0
    for _ in range(14):
        people += 1
        ans_set.append(people)
    
    # 특정 호수의 거주민 수 계산하기
    for i in range(nums[0]):
        for j in range(nums[1]-1, -1, -1):
            pop = 0
            for k in range(j+1):
                pop += ans_set[k]
            ans_set[j] = pop

    # 결과 출력
    print(ans_set[nums[1]-1])