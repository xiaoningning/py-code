"""https://leetcode.com/problems/shortest-path-in-binary-matrix/"""

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        dist = 0
        q = deque([(0, 0)])
        grid[0][0] = 1

        while q:
            for _ in range(len(q)):
                row, col = q.pop()
                if row == n - 1 and col == n - 1:
                    return dist

                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == 0 and dc == 0:
                            continue

                        nr, nc = row + dr, col + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            q.append((nr, nc))
            dist += 1
        return -1


if __name__ == '__main__':
    m1 = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
    ]

    r = Solution().shortestPathBinaryMatrix(m1)
    print(f"shortest path: {r}")
