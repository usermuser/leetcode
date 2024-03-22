"""
Палиндром — это число, которое одинаково читается в обоих направлениях. Например, 123321 — это палиндром.

Необходимо найти самый большой палиндром, равный произведению двух 3-значных чисел.
"""
def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

def find_palindrome() -> int:
    largest_palindrome = 0

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                print(f"Числа: {i} {j}")
                break

    print("Самый большой палиндром, равный произведению двух 3-значных чисел, равен:", largest_palindrome)
    return largest_palindrome


if __name__ == '__main__':
    find_palindrome()