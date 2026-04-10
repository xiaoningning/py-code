from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = deque()

        for i, v in enumerate(nums):
            if q and i - q[0] >= k: q.popleft() 
            while q and v >= nums[q[-1]]: q.pop()
            q.append(i)
            if i >= k - 1: res.append(nums[q[0]])

        return res

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    r = Solution().maxSlidingWindow(nums, k)
    assert r == [3, 3, 5, 5, 6, 7], "failed"