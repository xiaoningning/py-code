from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, num in enumerate(nums):
        if num in d:
            return [d[num], i]
        d[target - num] = i
    return []

if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 13) == [0, 2]