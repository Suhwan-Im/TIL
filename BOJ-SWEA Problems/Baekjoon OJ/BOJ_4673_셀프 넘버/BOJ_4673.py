num_list = list(range(1, 10001))    # 1 부터 10000까지 순회하기 위한 숫자 리스트
fin_list = list(range(1, 10001))    # 최종 정답만 남길 숫자 리스트

for num in num_list:
    num_str = str(num)
    new_num = num
    for n in num_str:
        new_num += int(n)

    if new_num <= 10000 and new_num in fin_list:
        fin_list.remove(new_num)

for num in fin_list:
    print(num)