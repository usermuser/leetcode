"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

from queue import LifoQueue


class Solution(object):
    """
    Если длина не четная, то сразу False.
    Если первая скобка не открывающая, то сразу False.
    Если последняя не закрывающая, то тоже сразу False.
    Если первая половина скобок все открывающие, то если скобка половина+1 не закрывающая, то False.
    """
    OPEN = '([{'
    CLOSE = ')]}'
    # положим пары скобок в словарь, чтобы при получении закрывающей скобки при помощи метода self.match
    # удобно определять что у нас валидный случай и открывающую скобку из списка можно удалить.
    PAIRS = {'[': ']', '(': ')', '{': '}'}

    def isValid(self, s) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        if any([
            len(s) % 2 != 0 or              # Если длина нечетная или
            s[0] not in self.OPEN or        # первая скобка не открывающая или
            s[-1] not in self.CLOSE         # последняя не закрывающая, то сразу False
        ]):
            return False

        stack = LifoQueue(maxsize=104)
        for p in s:
            # если встретили закрывающую скобку, а список пустой, то ошибка.
            if p in self.CLOSE and stack.empty():
                return False

            if p in self.OPEN:
                stack.put(p)
                continue

            if self._match(p, stack[-1]):
                stack.pop()
            else:
                return False
                
        if len(stack) == 0:
            return True
        return False

    def _match(self, p: str, prev: str):
        return self.PAIRS.get(prev, '') == p


if __name__ == '__main__':
    # s = "()"
    # expect = True
    # assert Solution().isValid(s) == expect
    #
    # s = "()[]{}"
    # expect = True
    # assert Solution().isValid(s) == expect
    #
    # s = "(]"
    # expect = False
    # assert Solution().isValid(s) == expect
    #
    # s = "([}}])"
    # expect = False
    # assert Solution().isValid(s) == expect
    #
    # s = "()))"
    # expect = False
    # assert Solution().isValid(s) == expect

    q = LifoQueue()
    q.put("a")
    q.put("b")
    q.put("c")

    print("Full: ", q.full())
    print("Size: ", q.qsize())

    c = q.get()
    print(c)
    print(q.qsize())
    q.get()
    print(q.qsize())