# Летние школы Академии Яндекса 2022. Занятие 1 (Разбор случаев, линейный поиск)
# E. Сломай палиндром

"""
Палиндромом называется строка, которая читается одинаково слева-направо и справа-налево.
В заданной строке-палиндроме необходимо заменить один символ, чтобы она перестала быть палиндромом.
При этом полученная строка должна быть лексикографически минимальной.
Строка A лексикографически меньше строки B (той же длины), если на первой различающейся позиции в строке A
стоит меньший символ, чем в B. Например, строка adbc меньше строки adca, т.к. первые два символа в строках
совпадают, а на третьем месте в строке adbc стоит символ b, который меньше символа c, стоящего на третьей
позиции в строке adca.
"""
def polindrom(seq):
    # print(chr(97))
    # print(ord('a'))

    #seq = input()

    # seq = 'aba'

    seq = list(seq)
    # print(seq)

    seq = [ord(seq[i]) for i in range(len(seq))]
    # print(seq)

    # если set от строки a - то ответа нет

    # print(len(seq))

    if set(seq) != {97}:
        # for i in range((int(len(seq)/2))):
        for i in range((int(len(seq) / 2))+1):
            # print(seq[i])
            if seq[i] > 97 and i != (int(len(seq) / 2)):
                # print('ok')
                # print('Элемент', seq[i])
                seq[i] = 97
                # print('Новый элемент', seq[i])
                break
            if set(seq) == {97} and seq[-1] == 97:
                seq[-1] = 98

    elif set(seq) == {97} and len(seq) > 1:
        seq[-1] = 98

    else:
        seq = ''

    if len(set(seq)) == 1:
        seq = ''

    if len(seq) % 2 != 0:
        if seq[-1] == 97:
            seq[-1] = 98

    #print(seq)

    seq = [chr(seq[i]) for i in range(len(seq))]
    return ''.join(seq)


# Разбор домашнего задания

def sol(s):
    if len(s) == 1:
        return ''
    middle = len(s) // 2
    flag = False
    for i in range(middle):
        if s[i] != 'a':
            ans = s[:i] + 'a' + s[i+1:]
            flag = True
            break
    if flag:
        return ans
    else:
        return s[:-1] + 'b'

s = input()
# answer = sol(s)
# print('', answer)
my_answer = polindrom(s)
print(my_answer)
