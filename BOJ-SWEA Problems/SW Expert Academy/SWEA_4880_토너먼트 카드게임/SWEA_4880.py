import sys
sys.stdin = open('input.txt')


# 무승부가 없는 가위바위보 함수 정의
def rsp(left, right):
    if nl[left] == 1:                           # 왼쪽이 가위인 경우
        if nl[right] == 1 or nl[right] == 3:        # -> 오른쪽이 가위 또는 보를 내면
            return left                             # -> 왼쪽 승
        elif nl[right] == 2:                        # -> 오른쪽이 바위를 내면
            return right                            # -> 오른쪽 승
    elif nl[left] == 2:                         # 왼쪽이 바위인 경우
        if nl[right] == 2 or nl[right] == 1:        # -> 오른쪽이 바위 또는 가위를 내면
            return left                             # -> 왼쪽 승
        elif nl[right] == 3:                        # -> 오른쪽이 보를 내면
            return right                            # -> 오른쪽 승
    elif nl[left] == 3:                         # 왼쪽이 보인 경우
        if nl[right] == 3 or nl[right] == 2:        # -> 오른쪽이 보 또는 바위를 내면
            return left                             # -> 왼쪽 승
        elif nl[right] == 1:                        # -> 오른쪽이 가위를 내면
            return right                            # -> 오른쪽 승

# 토너먼트 형식으로 승자를 찾는 함수 정의
def winner(i, j):
    if i == j:                      # 한 명만 남은 경우
        return i                        # -> i 반환
    else:                           # 두 명 이상인 경우
        left = winner(i, (i+j)//2)      # -> 왼쪽 그룹을 winner함수에 넣기
        right = winner((i+j)//2+1, j)   # -> 오른쪽 그룹을 winner함수에 넣기
        return rsp(left, right)         # 두 그룹중 가위바위보 승자를 반환


# 테스트 케이스를 통한 코드 실행
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    nl = num_list           # rsp함수에서 num_list를 읽어주기위해 nl 변수 지정
    rlt = winner(0, N-1)    # winner함수에 인덱스 (i = 0, j = N-1) 넣기

    # 결과 출력
    print(f'#{tc} {rlt+1}')