#Летние школы Академии Яндекса 2022. Занятие 1 (Разбор случаев, линейный поиск)
#B. Канонический путь

'''
По заданной строке, являющейся абсолютным адресом в Unix-системе, вам необходимо получить канонический адрес.
В Unix-системе "." соответсвутет текущей директории, ".." — родительской директории, при этом будем считать,
что любое количество точек подряд, большее двух, соответствует директории с таким названием (состоящем из точек).
"/" является разделителем вложенных директорий, причем несколько "/" подряд должны интерпретироваться как один "/".
Канонический путь должен обладать следующими свойствами:
1) всегда начинаться с одного "/"
2) любые две вложенные директории разделяются ровно одним знаком "/"
3) путь не заканчивается "/" (за исключением корневой директории, состоящего только из символа "/")
4) в каноническом пути есть только директории, т.е. нет ни одного вхождения "." или ".." как соответствия текущей
или родительской директории
'''

#на тест /a/../b ответ /b
#на тест /a/b/../c ответ /a/c
#на тест /1/../2/3/4/5/../3 ответ /2/3/4/3

input_str = input()

input_list = input_str.split('/')   # делим по /
print('input_list1: ', input_list)

while '.' in input_list:
    input_list.remove('.')  # yдаляем, т.к. это та же директория

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

# Разбор домашнего задания

def simplifyPath(path: str) -> str:
    flag = True
    path += '/'
    while flag:
        # /./ это остаться в той же директории
        if '/./' in path:
            path = path.replace('/./', '/')
            flag = True
        elif '//' in path:
            # replace - заменяет все вхождения
            path = path.replace('//', '/')
        # /../ подъем на одну директорию выше
        elif '/../' in path:
            pos = path.find('/../')
            # чтобы не подняться выше коневой директории
            if pos == 0:
                path = path[3:]
            else:
                # rfind - ищем самое правое вхождение / в интервале 0, pos-1
                prevslashpos = path.rfind('/', 0, pos - 1)
                path = path[:prevslashpos] + path[pos + 3:]
        else:
            flag = False
    if path.endswith('/') and path != '/':
        # отрезаем последний символ, если единственный, то ничего не делаем
        path = path[:-1]
    if path.endswith('/.'):
        path = path[:-2]
    # если путь получился пустым, то устанавливаем /
    if path == '':
        path = '/'
    return path

# упрощаем решение

def simplifyPath(path: str) -> str:
    flag = True
    path += '/'
    while flag:
        # /./ это остаться в той же директории
        if '/./' in path:
            path = path.replace('/./', '/')
            #flag = True
        elif '//' in path:
            # replace - заменяет все вхождения
            path = path.replace('//', '/')
        # /../ подъем на одну директорию выше
        elif '/../' in path:
            pos = path.find('/../')
            # чтобы не подняться выше коневой директории
            if pos == 0:
                path = path[3:]
            else:
                # rfind - ищем самое правое вхождение / в интервале 0, pos-1
                prevslashpos = path.rfind('/', 0, pos - 1)
                path = path[:prevslashpos] + path[pos + 3:]
        else:
            flag = False
    if path.endswith('/') and path != '/':
        # отрезаем последний символ, если единственный, то ничего не делаем
        path = path[:-1]
    # if path.endswith('/.'):
    #     path = path[:-2]
    # # если путь получился пустым, то устанавливаем /
    # if path == '':
    #     path = '/'
    return path

