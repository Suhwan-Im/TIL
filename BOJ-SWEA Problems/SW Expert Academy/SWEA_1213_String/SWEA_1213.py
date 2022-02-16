import sys
sys.stdin = open('input.txt', encoding="utf-8")


# key_finding 함수 정의
def key_finding(key, text):
    key_list = list(map(str, key))
    text_list = list(map(str, text))

    # 변수 0으로 지정
    found = 0
    cnt = 0

    # for문을 이용해 한칸씩 이동하며 일치여부 확인
    for t in range(len(text_list)-len(key_list)+1):
        for k in range(len(key_list)):
            if text_list[t+k] == key_list[k]:
                found += 1
            else:
                found = 0
        # key 전체가 일치하면 cnt 숫자 1씩 증가
        if found == len(key_list):
            cnt += 1

    # 찾은 개수 반환
    return cnt


# 테스트 케이스를 통한 코드 실행
T = 10
for tc in range(1, T + 1):
    N = int(input()) # 테스트 케이스 번호
    key = input()
    text = input()

    # key_finding 함수 이용해 계산하기
    rlt = key_finding(key, text)

    # 결과 출력
    print(f'#{tc} {rlt}')