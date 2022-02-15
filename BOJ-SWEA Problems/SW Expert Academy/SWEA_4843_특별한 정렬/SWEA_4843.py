import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    new_list = []

    # 리스트를 오름차순으로 정렬 (버블정렬)
    for i in range(len(num_list), 1, -1):
        for j in range(0, i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    # 큰수와 작은수 번갈아가며 새 리스트에 누적
    if N % 2 == 0:  # 리스트가 짝수개인 경우
        for i in range(int(N/2)):
            new_list.append(num_list[N-1-i])
            new_list.append(num_list[i])
    else:  # 리스트가 홀수개인 경우
        for i in range(int(N/2)):
            new_list.append(num_list[N-1-i])
            new_list.append(num_list[i])
        new_list.append(num_list[(N+1)/2])


    # 결과 출력 (10개까지만)
    print(f"#{tc} {' '.join(map(str, new_list[:10]))}")