import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
class_list = [list(map(str, input().split())) for _ in range(20)]

# 성적을 학점으로 변환해주는 딕셔너리 생성
grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0,
         'D+': 1.5, 'D0': 1.0, 'F': 0.0}

earned = 0      # 취득한 학점을 담을 earned 변수 생성
base = 0        # 수강한 학점의 총합을 담을 base 변수 생성

# for 문을 이용해 학점 누적하기
for cls in class_list:
    if cls[2] != "P":       # 성적이 P가 아닌경우 학점 누적 (P인 경우 배제)
        base += float(cls[1])
        earned += float(cls[1]) * grade[cls[2]]

# 최종 학점 계산
GPA = earned / base

# 결과 출력
print(GPA)