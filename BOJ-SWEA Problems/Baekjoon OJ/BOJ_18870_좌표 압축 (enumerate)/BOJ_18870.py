import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N = int(input())
nums = list(map(int, input().split()))

# 숫자 중복값 제거 및 정렬
arr = list(set(nums))
arr = sorted(arr)

# 숫자 dictionary 생성 및 enumerate 함수 이용해서 인덱스 부여
num_dict = dict()
for idx, num in enumerate(arr):
    num_dict[num] = idx

# 결과 출력
for num in nums:
    print(num_dict[num], end=' ')