def single_root_words(root_word, *other_words):
    same_words = []
    up_other = list(s.upper() for s in other_words)
    up_root = root_word.upper()

    for i in range(0, len(up_other)):
        if up_other[i].count(up_root) > 0:
            same_words.append(up_other[i])
    for j in range(0, len(up_other)):
        if up_root.count(up_other[j]) > 0:
            same_words.append(up_other[j])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
