#  2. Посчитать четные и нечетные цифры введенного натурального числа.
#  Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input('Введите натуральное число-->'))

even = 0
odd = 0

while n != 0:
    if (n % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print(f'В числе {even} четных и {odd} нечетнх цифр')
