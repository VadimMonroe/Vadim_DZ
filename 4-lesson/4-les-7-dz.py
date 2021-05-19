from math import factorial


# Классический факториал
# -------------------------------------------------------
def classic_fact(number):
    for i in range(number):
        yield factorial(i + 1)


print('*' * 1, '\n'f'Значение встроенной функции факториала: {classic_fact(5)}', '\n' '*' * 1)

new_fact = classic_fact(5)

print('Шаг классического генератора 1 -', next(new_fact))
print('Шаг классического генератора 2 -', next(new_fact))
print('Шаг классического генератора 3 -', next(new_fact))
print('Шаг классического генератора 4 -', next(new_fact))
print('Шаг классического генератора 5 -', next(new_fact))


# Функция - генератор, вычесляющая факториял последовательно
# -------------------------------------------------------
def fact_func(number):
    fact = 1
    for i in range(number):
        fact = fact * (i + 1)
        yield fact


# Показываем что наша функция это генератор
# -------------------------------------------------------
print('*' * 1, '\n'f'Показываем что генератор - {fact_func(5)}', '\n' '*' * 1)

x = fact_func(5)

print('Шаг генератора 1 -', next(x))
print('Шаг генератора 2 -', next(x))
print('Шаг генератора 3 -', next(x))
print('Шаг генератора 4 -', next(x))
print('Шаг генератора 5 -', next(x), '\n' '*' * 1)

# Показываем все значения генератора факториала
# -------------------------------------------------------
for el in fact_func(5):
    print(f'Вывод всех значений факториала сразу: {el}')
