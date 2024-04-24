"""
Дана строка, содержащая буквы //A-Z//:
"AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
Нужно написать функцию RLE, которая выведет строку вида:
"A4B3C2XYZD4E3F3A6B28"
Еще надо выдавать ошибку, если на ввод приходит недопустимая строка.

Примечания:
1. Если символ встречается один раз, он остается неизменным
2. Если символ встречается более одного раза, к нему добавляется число повторений
"""


def rle(s):
    lst = []
    ans = ''
    idx = 0

    for i in len(s):

        if ans != s[i]:
            if i - idx > 1:
                lst.append(f"{i - idx}{s[i]}")
            else:
                lst.append[s[i]]

            idx = i
            ans = s[i]

        if i == len(s) - 1:
            if i + 1 - idx > 1:
                lst.append(f"{i + 1 - idx}")

    return "".join(lst)


if __name__ == '__main__':
    s = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    assert rle(s) == "A4B3C2XYZD4E3F3A6B28"
