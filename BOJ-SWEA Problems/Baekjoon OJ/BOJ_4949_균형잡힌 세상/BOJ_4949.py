import sys
sys.stdin = open('input.txt')

# while 문을 이용해 문제 풀기
while True:
    sentence = str(input())
    if sentence == '.':
        break
    else:
        ans = 'yes'
        paren = []
        for word in sentence:
            if word == "(":
                paren.append("(")
            elif word == "[":
                paren.append("[")
            elif word == ")":
                if (len(paren) > 0) and (paren[-1] == "("):
                    paren.pop()
                else:
                    ans = 'no'
                    break
            elif word == "]":
                if (len(paren) > 0) and (paren[-1] == "["):
                    paren.pop()
                else:
                    ans = 'no'
                    break

        if len(paren) != 0:
            ans = 'no'

        print(ans)