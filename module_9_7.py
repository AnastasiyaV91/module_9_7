def is_prime(func):
    def wrapper(*args):
        res2 = func(*args)
        is_prime = True                        # Присваиваем переменной is_prime значение True
        for i in range(2, res2):               # Цикл проверки числа начиная с двойки (пропускаем единицу)
            if res2 % i == 0 and res2 != i:    # Условие проверки составного числа
                is_prime = False               # Если число составное, то
                break                          # выходим из цикла
        if is_prime == True:                   # Если число простое, то
            print("Простое")                   # выводим в консоль сообщение
        if is_prime == False:                  # Если число составное, то
            print("Составное")                 # выводим в консоль сообщение
        return res2                            # Функция wrapper возвращает результат принимаемой функции
    return wrapper                             # Функция is_prime (декоратор) возвращает внутренюю функцию

@is_prime                  # Указание, что функция is_prime является декоратором для функции sum_three
def sum_three(*args):      # Функция посчитывает сумму чисел списка args
    res = sum(args)        # В переменную res записываем сумму чисел списка args
    return res             # Возвращаем результат


result = sum_three(2, 3, 6)
print(result)