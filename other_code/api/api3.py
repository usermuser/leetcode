def find_sum(filename):
    total_sum = 0.0
    sum_started = False

    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for i, word in enumerate(words):
                if word == 'Сумма':
                    sum_started = True
                    try:
                        total_sum += float(words[i + 1])
                    except IndexError:
                        # Если слово "Сумма" в конце строки без числа
                        pass
                elif sum_started:
                    try:
                        total_sum += float(word)
                    except ValueError:
                        # Если не удалось преобразовать слово в число
                        sum_started = False
                        break

    return total_sum

filename = 'summa.txt'  # Укажите имя вашего файла
total = find_sum(filename)
print("Общая сумма чисел после слова 'Сумма':", total)
