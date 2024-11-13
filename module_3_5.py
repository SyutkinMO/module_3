# ---------------Рекурсия---------------


"""Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и
подсчитывает произведение цифр этого числа."""


def get_multiplied_digits(number):
    str_number = str(number)  # строковое представление(str) числа number
    first = int(str_number[0])  # первый символ из str_number в числовом представлении(int).
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
