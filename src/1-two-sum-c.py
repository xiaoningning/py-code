from dataclasses import dataclass


@dataclass
class TwoSum:
    nums: list[int]
    target: int

    def find_two_sum(self) -> list[int] | None:
        seen = {}
        for i, n in enumerate(self.nums):
            if (m := self.target - n) in seen:
                return [seen[m], i]
            seen[n] = i
        return None

    def __str__(self) -> str:
        return f"TwoSum(nums={self.nums}, target={self.target})"


if __name__ == "__main__":
    # Example 1: has solution
    solver1 = TwoSum([2, 7, 11, 15], 9)
    print(solver1)
    print("Result:", solver1.find_two_sum())

    # Example 2: no solution
    solver2 = TwoSum([1, 2, 3], 10)
    print(solver2)
    try:
        print("Result:", solver2.find_two_sum())
    except ValueError as e:
        print("Error:", e)
