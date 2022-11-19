num_list = list(range(1, 10001))
fin_list = list(range(1, 10001))

for num in num_list:
    num_str = str(num)
    new_num = num
    for n in num_str:
        new_num += int(n)

    if new_num <= 10000 and new_num in fin_list:
        fin_list.remove(new_num)

for num in fin_list:
    print(num)