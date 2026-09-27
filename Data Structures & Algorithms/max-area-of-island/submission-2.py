class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        #### DFS RECURSIVE version
        #### using Visited hashset 

        maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])
        #DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()

        def dfs(row, col):
            if (row not in range(ROWS) or col not in range(COLS) or
                grid[row][col] == 0 or (row, col) in visited):
                return 0
            
            visited.add((row, col))

            return (1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col + 1) + dfs(row, col -1))


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = dfs(row, col)
                    maxArea = max(area, maxArea)

        return maxArea