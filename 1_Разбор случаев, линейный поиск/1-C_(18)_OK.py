# # Летние школы Академии Яндекса 2022. Занятие 1 (Разбор случаев, линейный поиск)
# # C. Купить и продать

'''
У вас есть 1000$, которую вы планируете эффективно вложить. Вам даны цены за 1000 кубометров газа за n дней. Можно один раз купить газ на все деньги в день i и продать его в один из последующих дней j, i < j.

Определите номера дней для покупки и продажи газа для получения максимальной прибыли.
'''

# n_days = int(input())
# prices = tuple(map(int, input().split()))

# input_days = '6'
# input_prices = '10 3 5 3 11 9'
#
# # input_days = '4'
# # input_prices = '5 5 5 5'

input_days = '6'
input_prices = '89 89 89 48 34 13'

'''
print((1000 / 89) * 89 - 1000)
дает ответ 1.1368683772161603e-13
'''

n_days = int(input_days)
prices = list(map(int, input_prices.split()))

# Рассчитаем все для первого дня

def my_find_days(n_days, prices):
    ind_day_buy = 0
    price_day_buy = prices[0]
    index_day_min_price = 0
    profit = 0
    ans = (0, 0)

    for i in range(1, n_days):

        # здесь нужно считать профит (как будто зная день с минимальной ценой)
        # сначала инициализируем ее ценой дня с индексом 0
        ind_day_sell = i
        price_day_sell = prices[i]
        new_profit = (256 / prices[index_day_min_price]) * prices[i] - 256
        if new_profit > profit:
            profit = new_profit
            # потом добавить +1 для переходя к дням от индексов
            ans = (index_day_min_price+1, i+1)

        # теперь мне нужно найти это день с минимальной ценой
        if price_day_buy > prices[i]:
            index_day_min_price = i
            price_day_buy = prices[i]

    return print(*ans)

my_find_days(n_days, prices)

# Разбор домашнего задания для стресс-тестирования

def find_days(n_days, prices):
    money = 1

    index_day_min_price = 0
    value_gas = money / prices[0]
    profit = 0

    ans = (0, 0)

    for i in range(1, n_days):
        if value_gas * prices[i] - money > profit:
            profit = value_gas * prices[i] - money
            ans = (index_day_min_price + 1, i + 1)
        if money / prices[i] > value_gas:
            index_day_min_price = i
            value_gas = 1 / prices[i]

    return ans

# проведем тестирование (тест 10 заваливался)
# нашел ошибку
'''
89 89 89 48 34 13
(1, 2) (0, 0)
'''

from random import randint

while True:
    n_days = 6
    prices = []
    for i in range(n_days):
        prices.append(randint(1, 100))
    print(*prices)
    my_ans = my_find_days(n_days, prices)
    right_ans = find_days(n_days, prices)
    print(my_ans, right_ans)
    if my_ans != right_ans:
        break

my_ans = my_find_days(n_days, prices)
right_ans = find_days(n_days, prices)
print(my_ans, right_ans)

# Разбор домашнего задания

n = int(input())
cost = list(map(int, input().split()))
minIndex = 0
maxGas = 1 / cost[0]
maxRevenue = 0
ans = (0, 0)

for i in range(1, n):
    if maxGas * cost[i] - 1 > maxRevenue:
        maxRevenue = maxGas * cost[i] - 1
        ans = (minIndex + 1, i + 1)
    if 1 / cost[i] > maxGas:
        minIndex = i
        maxGas = 1 / cost[i]
print(*ans)

# если заменить 1 на 1000 решение дает WA 1 тесте
# Проблема в точности вычисления.

'''
Сравниваем два случая, например, a - цена покупки, b - цена продажи и второй случай с - цена покупки,
d - цена продажи. Проверяем условие b/a < d/c, чтобы понять, что выручка во втором случае больше. 
Домножаем дроби нa (a*c) и получаем условие b*c < a*d. При таком сравнении все целые числа, нет деления.
'''

n = int(input())
cost = list(map(int, input().split()))
bestBuyDay = 0
bestSellDay = 0
minCostDay = 0

for i in range(1, n):
    if cost[bestSellDay] * cost[minCostDay] < cost[bestBuyDay] * cost[i]:
        bestBuyDay = minCostDay
        bestSellDay = i
    if cost[i] < cost[minCostDay]:
        minCostDay = i
if bestSellDay == 0 and bestBuyDay == 0:
    print(0, 0)
else:
    print(bestBuyDay + 1, bestSellDay + 1)

print(*ans)