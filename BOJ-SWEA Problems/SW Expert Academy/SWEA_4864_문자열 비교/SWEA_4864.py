import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    key = input()
    words = input()
    rlt = 0

    # for문을 이용해 전제 문장에서 한칸씩 뒤로가며 key와 비교 후 일치하면 1을 리턴 후 반복문 종료
    for i in range(len(words) - len(key) + 1):
        if words[i: i + len(key)] == key:
            rlt = 1
            break

    # 결과 출력
    print(f'#{tc} {rlt}')