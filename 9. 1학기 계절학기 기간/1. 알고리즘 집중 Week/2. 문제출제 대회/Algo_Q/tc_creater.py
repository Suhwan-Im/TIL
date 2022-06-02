import random

T = 50
for tc in range(1, T+1):
    N = random.randint(1, 100)
    M = random.randint(1, 100)

    N_list, M_list = [], []
    for i in range(N):
        N_list.append(random.randint(0,50))
    for j in range(M):
        M_list.append(random.randint(0,50))

    print(N, M)
    print(*N_list[:])
    print(*M_list[:])