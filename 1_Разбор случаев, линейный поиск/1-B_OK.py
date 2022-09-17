#Летние школы Академии Яндекса 2022. Занятие 1 (Разбор случаев, линейный поиск)
#B. Канонический путь

#на тест /a/../b ответ /b
#на тест /a/b/../c ответ /a/c
#на тест /1/../2/3/4/5/../3 ответ /2/3/4/3

input_str = input()

input_list = input_str.split('/')   # делим по /
print('input_list1: ', input_list)

while '.' in input_list:
    input_list.remove('.')  # удаляем . т.к. это таже директория

input_list = list(filter(None, input_list)) # удаялем пустые значения
print('input_list2: ', input_list)

# ищем ..(index n) и удаляем (index n и n-1)
# обрабатываем исключение index = 0
def fined(input_list):
    try:
        find_index = input_list.index('..')
        print('find_index = ', find_index)

        if find_index > 0:
            del input_list[find_index-1:find_index+1]
            print('input_list3: ', input_list)
        elif find_index == 0:
            del input_list[0]
    except:
        pass
    return input_list

# проходим по всей строке
while '..' in input_list:
    fined(input_list)
    print('input_list4: ', input_list)

# еще раз фильтрую пропуски
input_list = list(filter(None, input_list))
print('input_list5: ', input_list)

# приклеиваю путь к корню
output_str = '/'+"/".join([str(_) for _ in input_list])

print(output_str)

