def print_params(a=1, b='String', c=True):
    print(a, b, c)


print_params(89, 'good', False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1028, 'Orange', False]
values_dict = {'a': True, 'b': 2048, 'c': 'Potato'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
