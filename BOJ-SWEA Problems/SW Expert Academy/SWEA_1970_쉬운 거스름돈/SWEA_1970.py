import sys
sys.stdin = open('input.txt')

# input값 입력 받기
T = int(input())
for tc in range(1, T+1):
    amt = int(input())

    # 종류별 지폐/동전의 개수를 담을 변수 생성
    cnt_A, cnt_B, cnt_C, cnt_D, cnt_E, cnt_F, cnt_G, cnt_H = 0, 0, 0, 0, 0, 0, 0, 0

    # 50,000원
    if amt >= 50000:
        cnt_A = amt // 50000
        amt = amt % 50000

    # 10,000원
    if amt >= 10000:
        cnt_B = amt // 10000
        amt = amt % 10000

    # 5,000원
    if amt >= 5000:
        cnt_C = amt // 5000
        amt = amt % 5000

    # 1,000원
    if amt >= 1000:
        cnt_D = amt // 1000
        amt = amt % 1000

    # 500원
    if amt >= 500:
        cnt_E = amt // 500
        amt = amt % 500

    # 100원
    if amt >= 100:
        cnt_F = amt // 100
        amt = amt % 100

    # 50원
    if amt >= 50:
        cnt_G = amt // 50
        amt = amt % 50

    # 10원
    if amt >= 10:
        cnt_H = amt // 10
        amt = amt % 10

    # 지폐/동전 종류별 개수를 bill_list라는 리스트에 담기
    bill_list = [cnt_A, cnt_B, cnt_C, cnt_D, cnt_E, cnt_F, cnt_G, cnt_H]

    # 결과 출력
    # print(f'#{tc}\n', *bill_list[:])
    print(f'#{tc}')
    print(f'{cnt_A} {cnt_B} {cnt_C} {cnt_D} {cnt_E} {cnt_F} {cnt_G} {cnt_H}')