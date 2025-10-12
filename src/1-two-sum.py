def find_two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers whose sum equals target, or [] if none."""
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
    seen[n] = i

    return []


assert find_two_sum([2, 7, 11, 15], 13) == [0, 2]
assert find_two_sum([2, 7, 11], 8) == []
