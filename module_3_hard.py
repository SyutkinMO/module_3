# -------Функция подсчета суммы целых чисел и символов в сложном списке через рекурсию-------

def counter(*objects):
    sum_ = 0
    for i in list(*objects):
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            sum_ = sum_ + (counter(i))
        elif isinstance(i, dict):
            sum_ = sum_ + counter(list(i.items()))
        else:
            if isinstance(i, int):
                sum_ += i
            else:
                sum_ += len(i)
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(counter(data_structure))
