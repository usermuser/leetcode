import re

with open("rezult.txt", "r") as f:
    content = f.read()

numbers = re.findall(r'Сумма..(\d+.\d+)', content)

total_sum = sum(float(num) for num in numbers)
print(total_sum)
