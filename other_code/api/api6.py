def read_file_character_by_character(filename):
    # Открываем файл для чтения
    with open(filename, 'r') as file:
        # Итерируемся по символам в файле
        for line in file.readline():
            yield line  # Возвращаем символ генератором

# Функция для суммирования чисел после ключевого слова 'Сумма:'
def sum_numbers_after_keyword(filename, keyword):
    total_sum = 0.0  # Инициализируем общую сумму

    # Флаг, указывающий, что ключевое слово было найдено
    keyword_found = False
    # Буфер для хранения числа
    number_buffer = ""

    # Итерируемся по символам, возвращаемым генератором
    for char in read_file_character_by_character(filename):
            if char.isdigit() or char == '.':
                number_buffer += char
            # Если текущий символ - пробел, то преобразуем буфер числа в число и добавляем его к общей сумме
            elif char == ' ':
                total_sum += float(number_buffer)
                # Очищаем буфер числа
                number_buffer = ""
                # Сбрасываем флаг
                keyword_found = False
        # Если нашли ключевое слово
        elif char == keyword[0]:
            keyword_found = True

    return total_sum

# Вызываем функцию для суммирования чисел после ключевого слова 'Сумма:'
total_sum = sum_numbers_after_keyword('summa.txt', 'Сумма:')
print("Общая сумма:", total_sum)
