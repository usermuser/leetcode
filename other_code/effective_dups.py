import json


# Функция-генератор для удаления дубликатов
def remove_duplicates(file_path):
    seen = set()
    with open(file_path, 'r') as file:
        for line in file:
            obj = json.loads(line)
            obj_tuple = tuple(sorted(obj.items()))
            if obj_tuple not in seen:
                seen.add(obj_tuple)
                yield obj

def effective(input_file_path, output_file_path):

    # Перезаписываем файл с уникальными данными
    with open(output_file_path, 'w') as file:
        for obj in remove_duplicates(input_file_path):
            json.dump(obj, file)
            file.write('\n')

    # Подсчитываем число уникальных объектов
    num_unique_objects = sum(1 for _ in remove_duplicates(input_file_path))
    print(num_unique_objects)


if __name__ == '__main__':
    # Путь к исходному файлу и новому файлу
    input_file_path = 'dicts.json'
    output_file_path = 'dicts_unique.json'

    effective(input_file_path, output_file_path)
