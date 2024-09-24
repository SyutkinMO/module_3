def counter(*objects):
    sum_ = 0
    for i in list(*objects):
        if isinstance(i, list):
            sum_ = sum_ + (counter(i))
        elif isinstance(i, dict):
            sum_ = sum_ + counter(i.items())
        elif isinstance(i, tuple):
            sum_ = sum_ + counter(list(i))
        elif isinstance(i, set):
            sum_ = sum_ + counter(list(i))
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
