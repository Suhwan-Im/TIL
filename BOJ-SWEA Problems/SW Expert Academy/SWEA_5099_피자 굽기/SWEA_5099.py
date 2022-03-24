import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    baked = [0] * M     # 치즈가 모두 녹은 피자를 저장할 baked 리스트 생성

    pizza = []                          # 피자의 인덱스와 치즈의 양을 담을 pizza 리스트 생성
    for i in range(M):                  # for 문을 이용해 모든 피자를 조회
        pizza.append([i, num_list[i]])  # 피자의 순서 인덱스와 치즈의 양을 리스트 형식으로 저장

    que = []                            # 화덕을 나타내는 빈 큐 생성
    for i in range(N):                  # for 문을 이용해 화덕의 크기만큼의 피자를 넣기
        que.append(pizza[i])            # 큐에 순서대로 피자 넣기

    idx = N                             # 다음에 넣어줄 피자를 트래킹할 idx 변수를 N 값으로 생성

    # while 문을 이용해 화덕에서 피자를 돌려가며 치즈 녹여주기
    while que:
        if len(que) == 1:               # 만약 큐의 길이가 1이라면, (화덕에 피자가 1개 남은 경우)
            break                       # -> 반복문 종료
        elif len(que) < N and idx < M:  # 만약 화덕에 공간이 있고, 넣어줄 피자가 남은 경우,
            que.append(pizza[idx])      # -> 화덕에 다음 순서의 피자 넣기
            idx += 1                    # -> 다음에 넣어줄 피자의 번호 1 증가
        else:                                           # 위의 조건을 제외한 경우,
            cur_pizza = que.pop(0)                      # 가장 이전에 넣었던 피자 꺼내기
            cur_pizza = [cur_pizza[0], cur_pizza[1]//2] # 피자의 치즈의 양을 2로 나누어주기
            if cur_pizza[1] > 0:            # 만약 치즈가 다 안녹았다면,
                que.append(cur_pizza)       # -> 피자를 다시 화덕에 넣기
            else:                           # 치즈가 다 녹았다면,
                baked[cur_pizza[0]] = 1     # -> 피자의 순서 인덱스를 이용해 baked 리스트에 1로 갱신

    rlt = baked.index(0) + 1 # 반복문 종료 후, 유일하게 0으로 남아있는 피자 번호를 rlt 변수에 저장하기

    # 결과 출력
    print(f'#{tc} {rlt}')