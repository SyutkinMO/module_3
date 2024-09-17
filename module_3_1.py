calls = 0


def count_cals():
    global calls
    calls += 1


def string_info(a):
    count_cals()
    tuple_ = len(a), a.upper(), a.lower()
    return tuple_


def is_contains(b, c):
    count_cals()
    if b.upper() in str(c).upper():
        bool_ = True
    else:
        bool_ = False
    return bool_


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
