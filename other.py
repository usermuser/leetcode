"""
original list: [-1, -1, -1, 160, 170, -1, -1, 190, 180, -1, 140,]
"""

def solution(lst: list) -> list:
    positive_nums = [i for i in lst if i > 0]
    sorted(lst, key=lambda x: x > 0)
    return lst

if __name__ == '__main__':
    payload = [-1, -1, -1, 160, 170, -1, -1, 190, 180, -1, 140,]
    sol =
    assert  == [-1, -1, -1, 140, 160, -1, -1, 170, 180, -1, 190]