def func():
    """
     Вводим целые числа через пробел.
     Чтобы завершить программу вводим спец-символ ! (восклицательный знак).
     Если вводить буквы, ничего не будет с ними происходить. Если вводить числа, они будут складываться.
    """
    i = 0
    result = 0

    while i != '!':
        input_number = input('Введите числа, через пробел (чтобы завершить >>!<<): ')
        for i in input_number.split(" "):
            if i.isdigit():
              result = result + int(i)
        print(f'Ваш результат на данный момент: ', result)
    else:
        print(f'Программа завершилась.')
func()