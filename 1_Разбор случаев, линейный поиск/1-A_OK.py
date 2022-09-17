# Летние школы Академии Яндекса 2022. Занятие 1 (Разбор случаев, линейный поиск)
# A. Строительство лесенок

n_blocks = int(input())

n_blocks_max = (2 ** 31) - 1  # 2_147_483_647

my_dict = {}
for i in range(1, 65_535 + 1):  # max steps 65_535
    sum_blocks = (i * (i + 1)) / 2  # формула для i-ого треугольного числа
    my_dict[sum_blocks] = i  # делаем словарь {количество_блоков: номер ступеньки или число ступенек}

for i in my_dict.keys():
    if i <= n_blocks:
        # print(f'{i} <= {n_blocks}')
        steps = (my_dict[i])

print(steps)
