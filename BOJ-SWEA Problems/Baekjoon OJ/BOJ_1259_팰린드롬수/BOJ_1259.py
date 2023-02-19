import sys
sys.stdin = open('input.txt')

while True:
    num = str(input())

    if num == '0':
        break
    elif len(num) == 1:     # 한자리 숫자인 경우도 팰린드롬 !!!
        print('yes')
    else:
        for i in range(len(num) // 2):
            if num[i] == num[-1 - i]:
                if i == (len(num) // 2 - 1):
                    print('yes')
            else:
                print('no')
                break