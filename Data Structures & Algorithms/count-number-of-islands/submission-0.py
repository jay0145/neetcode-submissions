class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # empty grid input sanitise
        if not grid:
            return 0

        # grab dimensions
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # iterative bfs
        # NOTE: DFS would only change popleft() to pop() - explore most recent child
        def bfs(row, col):
            queue = collections.deque()
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()

                neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for diffRow, diffCol in neighbours:
                    newRow, newCol = row + diffRow, col + diffCol

                    if newRow in range(rows) and newCol in range(cols) and grid[newRow][newCol] == "1" and (newRow, newCol) not in visited:
                        queue.append((newRow, newCol))
                        visited.add((newRow, newCol))

        
        for row in range(rows):
            for col in range(cols):
                item = grid[row][col]
                if item == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands



