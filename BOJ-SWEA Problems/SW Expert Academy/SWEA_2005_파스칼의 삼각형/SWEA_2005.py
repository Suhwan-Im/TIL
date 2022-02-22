import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 파스칼의 삼각형을 담을 num_tri 매트릭스 생성
    num_tri = []
    # for문을 이용해서 코드 구현
    for i in range(N):
        num_row = []
        # 첫 두줄은 [1]과 [1, 1]로 지정
        if i < 2:
            for j in range(i + 1):
                num_row.append(1)
        # 세번째줄부터는 시작과 끝은 1로, 사이값은 윗줄 두수의 합으로 넣기
        else:
            num_row.append(1)
            for j in range(1, i):
                num_row.append(num_tri[i - 1][j - 1] + num_tri[i - 1][j])
            num_row.append(1)
        # 파스칼의 삼각형 매트릭스에 누적
        num_tri.append(num_row)

    # 결과 출력
    print(f'#{tc}')
    # for문을 이용해서 특정 양식으로 출력
    for num_row in num_tri:
        print(*num_row[:])