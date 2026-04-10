"""https://leetcode.com/problems/shortest-path-in-binary-matrix/"""

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:  # noqa: N802
        n = len(grid)
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        dist = 0
        q = deque([(0, 0)])
        grid[0][0] = 1 # mark as visited

        while q:
            for _ in range(len(q)):
                # print(q)
                row, col = q.popleft()
                if row == n - 1 and col == n - 1:
                    return dist

                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        # no diagonal move
                        if dr == 1 and dc == 1:
                            continue

                        nr, nc = row + dr, col + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            q.append((nr, nc))
            dist += 1

        return -1

    def shortestPathBinaryMatrix2(self, grid: list[list[int]]) -> int:  # noqa: N802
        if grid[0][0] == 1 or grid[-1][-1]:
            return -1
        
        n = len(grid)
        q = deque([(0,0,0)])
        grid[0][0] = 1

        while q:
            # print(q)
            x, y, d = q.popleft()
            if x == n - 1 and y == n - 1:
                return d
            
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if i == x + 1 and j == y + 1:
                        continue
                        
                    if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                        grid[i][j] = 1
                        q.append((i, j, d + 1))
        
        return -1


if __name__ == '__main__':
    m1 = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
    ]

    r = Solution().shortestPathBinaryMatrix2(m1)
    print(f"shortest path: {r}")
