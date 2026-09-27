class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []

        ## OPTIMAL SOLUTION - dfs from borders of pacific/atlantic
        ## Time Complexity - O((m * n)^2)
        ## Space Complexity - O(m * n)
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # RECURSIVE DFS

        def dfs(row, col, visit, prevHeight):
            if (row not in range(ROWS) or col not in range(COLS) or
                (row, col) in visit or heights[row][col] < prevHeight):
                return
            visit.add((row, col))

            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])



        # all pacific and atlantic top and bottom cells
        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])

        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])

        bridges = pac.intersection(atl)
        for r, c in bridges:
            result.append([r, c])

        return result
