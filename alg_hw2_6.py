#  6. В программе генерируется случайное целое число от 0 до 100.
#  Пользователь должен его отгадать не более чем за 10 попыток.
#  После каждой неудачной попытки должно сообщаться больше или меньше
#  введенное пользователем число, чем то, что загадано.
#  Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

n = random.randint(0, 100)
print(n)
print('Угадайте число от 0 до 100 за 10 попыток!')

for i in range(10):
    attempt = int(input(f'Попытка № {i+1} -->'))
    if attempt == n:
        print(f'Бинго! Угадали с {i + 1}-й попытки! Поздравляю!')
        break
    elif attempt > n:
        print(f'{attempt} больше чем загаданное число!')
    else:
        print(f'{attempt} меньше чем загаданное число!')
if attempt != n:
    print(f'Не угадали! правильный ответ = {n} !')