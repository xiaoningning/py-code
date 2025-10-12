def find_two_sum(nums: list[int], target: int) -> list[int] | None:
    """Return indices of two numbers whose sum equals target, or [] if none."""
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i

    return None


# result = find_two_sum([2, 7, 11, 15], 13)
# if result != [0, 2]:
#     raise AssertionError(f"Expected indices [0, 2] but got {result}")

assert find_two_sum([2, 7, 11], 8) is None
assert find_two_sum([2, 7, 11, 15], 13) == [0, 2]
