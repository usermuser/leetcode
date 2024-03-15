"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution(object):
    """
    Использую словарь, в котором буду хранить числа которые встретились и их индекс (seen).
    Бегу по числам и каждый раз отнимаю от target текущее число,
    если полученный результат есть в виденных ранее числах (seen) - то это правильный ответ.

    Это быстрый результат с использованием дополнительной памяти в виде словаря.
    В словаре поиск происходит за константное время O(1) - так как это hashmap,
    поэтому условие `if difference in seen` - выполняется быстро.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = dict()  # ключ число, значение, индекс.

        for i, num in enumerate(nums):
            difference = target - num

            if difference in seen:
                return [seen[difference], i]

            seen[num] = i
        return []


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    expect = [0,1]
    output = Solution().twoSum(nums, target)
    assert output == expect, f"Ошибка {output=} != {expect=}"

    nums = [3, 2, 4]
    target = 6
    expect = [1, 2]
    output = Solution().twoSum(nums, target)
    assert output == expect, f"Ошибка {output=} != {expect=}"

    nums = [3, 2, 3]
    target = 6
    expect = [0, 2]
    output = Solution().twoSum(nums, target)
    assert output == expect, f"Ошибка {output=} != {expect=}"


