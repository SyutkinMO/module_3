# -------------Пространство имён-------------

"""Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
В Python не предусмотрен подсчёт вызовов автоматически.
И вот реализация"""

calls = 0

"""Вам необходимо написать 3 функции:"""


def count_cals():
    """Функция count_calls подсчитывающая вызовы остальных функций."""
    global calls
    calls += 1


def string_info(a) -> tuple:
    """Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки,
        строку в верхнем регистре, строку в нижнем регистре."""
    count_cals()
    tuple_ = len(a), a.upper(), a.lower()
    return tuple_


def is_contains(b, c) -> bool:
    """Функция is_contains принимает два аргумента: строку и список, и возвращает True,
    если строка находится в этом списке,
    False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN."""
    count_cals()
    BIG_ = [s.upper() for s in c]
    for i in BIG_:
        if i == b.upper():
            bool_ = True
            break
        else:
            bool_ = False
    return bool_


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
