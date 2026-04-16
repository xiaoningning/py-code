"""https://leetcode.com/problems/shortest-path-in-binary-matrix/"""

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:  # noqa: N802
        n = len(grid)
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        dist = 1
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
                        if (dr == 1 and dc == 1):
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
        q = deque([(0,0,1)])
        grid[0][0] = 1 # visit = set((0, 0))

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
    
    def shortestPathBinaryMatrix3(self, grid: list[list[int]]) -> int:  # noqa: N802
        if grid[0][0] == 1 or grid[-1][-1] == 1 : return -1

        N = len(grid)
        q = deque([(0, 0, 1)]) # r, c, dist
        grid[0][0] = 1 # marked as visited
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, -1], [-1, 1]] # no diagonal direction

        while q:
            r, c, dist = q.popleft()
            if r == N - 1 and c == N - 1: return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, dist + 1))
        
        return -1
    
    def shortestPathBinaryMatrix4(self, grid: list[list[int]]) -> int:  # noqa: N802
        if grid[0][0] == 1 or grid[-1][-1] == 1 : return -1

        N = len(grid)
        q = deque([(0, 0, 1)]) # r, c, dist
        visited = set((0,0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, -1], [-1, 1]] # no diagonal direction

        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()
                if r == N - 1 and c == N - 1:
                    return dist
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                        visited.add(nr, nc)
                        q.append((nr, nc, dist + 1))
        
        return -1


if __name__ == '__main__':
    m1 = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
    ]
    r = Solution().shortestPathBinaryMatrix(m1)
    
    m2 = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
    ]
    r2 = Solution().shortestPathBinaryMatrix2(m2)
    
    m3 = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
    ]
    r3 = Solution().shortestPathBinaryMatrix3(m3)

    m4 = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
    ]
    r4 = Solution().shortestPathBinaryMatrix4(m4)

    print(f"shortest path: {r}")
    print(f"shortest path: {r2}")
    print(f"shortest path: {r3}")
    print(f"shortest path: {r4}")
