# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите число, у которого нужно посчитать сумму по формуле n + nn + nnn: ')
result = int(n) + int(n + n) + int(n + n + n)
print('Ваш результат равен: ', result)
