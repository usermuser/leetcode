def sum_numbers_after_keyword(filename, keyword):
    total_sum = 0.0  # Инициализируем общую сумму

    # Открываем файл для чтения
    with open(filename, 'r') as file:
        # Итерируем по файлу построчно
        for line in file:
            # Находим индекс вхождения ключевого слова
            index = line.find(keyword)
            while index != -1:
                # Находим начало числа после ключевого слова
                number_start = index + len(keyword) + 1
                # Находим конец числа
                number_end = line.find(' ', number_start)
                if number_end == -1:
                    number_end = len(line)
                # Извлекаем число и прибавляем его к общей сумме
                number = float(line[number_start:number_end])
                total_sum += number
                # Ищем следующее вхождение ключевого слова
                index = line.find(keyword, number_end)

    return total_sum


# Вызываем функцию для суммирования чисел после ключевого слова 'Сумма:'
total_sum = sum_numbers_after_keyword('summa.txt', 'Сумма:')
print("Общая сумма:", total_sum)
