class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()

        def bfs(row, col):
            nodesToExpand = collections.deque()
            area = 0

            nodesToExpand.append((row, col))
            visited.add((row, col))

            while nodesToExpand:
                row, col = nodesToExpand.popleft()
                area += 1

                for rowDiff, colDiff in DIRECTIONS:
                    newRow = rowDiff + row
                    newCol = colDiff + col

                    if (newRow in range(ROWS) and newCol in range(COLS) and
                    grid[newRow][newCol] == 1 and (newRow, newCol) not in visited):
                        nodesToExpand.append((newRow, newCol))
                        visited.add((newRow, newCol))

            return area


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = bfs(row, col)
                    maxArea = max(area, maxArea)

        return maxArea