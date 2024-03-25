import json

# Открываем файл и считываем данные
with open('dicts.json', 'r') as file:
    data = [json.loads(line) for line in file]

# Удаляем дубликаты
unique_data = []
for item in data:
    if item not in unique_data:
        unique_data.append(item)

# Перезаписываем файл с уникальными данными
with open('unique_data.json', 'w') as file:
    for item in unique_data:
        json.dump(item, file)
        file.write('\n')

# Выводим число уникальных объектов
print(len(unique_data))

if __name__ == '__main__':

