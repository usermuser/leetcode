"""
В сортировке пузырьком элементы сравниваются попарно.
Если нужно отсортировать в порадке возрастания,
то мы будем перемещать каждый раз тот элемент, который больше.
таким образом бОльшие числа как бы всплывают как пузырьки в конец последовательности.
"""
def bubble_sort(nums: list) -> list:
    if len(nums) == 1:
        return nums

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True

    return nums


if __name__ == '__main__':
    assert bubble_sort([5, 2, 1, 8, 4]) == [1, 2, 4, 5, 8]

    assert bubble_sort([5, 2]) == [2, 5]

    assert bubble_sort([1]) == [1]

    assert bubble_sort([-1, -6]) == [-6, -1]



