"""
Минимальное четное

Найти минимальное четное число в последовательности,
вывести -1, если ни одного четного нет.
"""

def solution(seq):
    ans = -1
    for now in seq:
        if (now % 2 == 0) and (ans == -1 or now < ans):
            ans = now
    return ans


if __name__ == '__main__':
    assert solution([1, 5, 7, 6, 2]) == 2
    assert solution([1, 5, 7, 6, -2]) == -2
    assert solution([1, 5, 7, -6, -2]) == -6
