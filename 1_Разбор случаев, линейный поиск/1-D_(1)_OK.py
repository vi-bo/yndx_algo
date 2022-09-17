# # Летние школы Академии Яндекса 2022. Занятие 1 (Разбор случаев, линейный поиск)
# # D. Разница во времени

# n = int(input())
# arrival = list(input().split())


n = '4'
arrival = '01:00 14:00 16:00 23:00'

n = int(n)
arrival = list(arrival.split())
print('arrival', arrival)

if n > 1:

    # преобразуем все в минуты
    seq = []
    for i in range(n):
        n_arrival = list(map(int, arrival[i].split(':')))
        if n_arrival[0] == 0 and n_arrival[1] == 0:
            n_arrival[0], n_arrival[1] = 23, 60
        seq.append((n_arrival[0] * 60 + n_arrival[1]))
    #print('seq', seq)

    sort_seq = sorted(seq)
    #print('sort_seq', sort_seq)

    # была ошибка в инициализации
    # т.к. это расписание нужно было учитывать интервал
    # между первой и последней электричкой
    min_interval = 24 * 60 + sort_seq[0] - sort_seq[-1]
    for i in range(1, n):
        #print('sort_seq', sort_seq[i])
        new_min_interval = abs(sort_seq[i] - sort_seq[i-1])
        #print('new_min_interval:', new_min_interval)
        if new_min_interval < min_interval:
            min_interval = new_min_interval

    print(min_interval)

else:
    pass

'''
date_time_str = '07:40'
date_time_obj = datetime.datetime.strptime(date_time_str, '%H:%M')
print('Время:', date_time_obj.time())

time_1 = datetime.datetime.strptime('05:00:00',"%H:%M:%S")
time_2 = datetime.datetime.strptime('10:00:00',"%H:%M:%S")

time_interval = time_2 - time_1
print(time_interval)

#arrival = [datetime.datetime.strptime(time, '%H:%M') for time in arrival]

# for i in range(n):
#     print(arrival[i].time())
'''

'''
n = int(input())

timePoints = input().split()
minutePoints = []
for nowTime in timePoints:
    h, m = map(int, nowTime.split(':'))
    minutePoints.append(h * 60 + m)
minutePoints.sort()
minDist = 1440 + minutePoints[0] - minutePoints[-1]
for i in range(1, len(minutePoints)):
    minDist = min(minDist, minutePoints[i] - minutePoints[i - 1])
print(minDist)
'''