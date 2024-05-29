from random import randint, random

team1_num = randint(1, 10)
team2_num = randint(1, 10)
score1 = randint(1, 100)
score2 = randint(1, 100)
team1_time = random()*5000
team2_time = random()*5000
tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / tasks_total

# Использование %
print("В команде Мастера кода участников: %d !" % team1_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Использование format()
print("Команда Волшебники данных решила задач: {} !".format(score2))
print("Волшебники данных решили задачи за {0:7.2f} с !".format(team2_time))

# Использование f-строк
print(f'Команды решили {score1} и {score2} задач.')

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"
print(result)

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:6.2f} секунды на задачу!.')
