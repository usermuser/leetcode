"""
Второй по величине элемент.

Найти второе по величине число,
такое, которое будет максимальным,
если вычеркнуть из последовательности одно максимальное число
"""


def solution(nums: list) -> list:
    max1 = nums[0]
    max2 = nums[1]  # второе по величине максимальное число.
    if max1 < max2:
        max1, max2 = max2, max1

    for now in nums:
        # если число больше макс1
        if now > max1:
            max2 = max1
            max1 = now
        # если число меньше максимального, но больше макс2
        elif now > max2 and now < max1:
            max2 = now

    return max2


if __name__ == '__main__':
    assert solution([1, 6, 20]) == 6
    assert solution([20, 1, 20, 6, 20]) == 6
    assert solution([1, 6]) == 1
    assert solution([-1, -6, -20]) == -6
    assert solution([1, -6, 20]) == 1
    assert solution([20, 6, 1]) == 6
    assert solution([20, 1, 6]) == 6

