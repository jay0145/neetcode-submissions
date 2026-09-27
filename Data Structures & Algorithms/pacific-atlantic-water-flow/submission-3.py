class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []

        ## NAIVE SOLUTION - dfs every cell 
        ## Time Complexity - O((m * n)^2)
        ## Space Complexity - O(m * n)
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]


        def dfs(row, col):
            nodesToExpand = collections.deque()
            visited = set()
            inPacific = False
            inAtlantic = False

            nodesToExpand.append((row, col))
            visited.add((row, col))

            while nodesToExpand and (not inPacific or not inAtlantic):
                r, c = nodesToExpand.pop()

                if r == 0 or c == 0:
                    inPacific = True
                if r == ROWS-1 or c == COLS-1:
                    inAtlantic = True

                for rowDiff, colDiff in DIRECTIONS:
                    newRow, newCol = r + rowDiff, c + colDiff

                    if (newRow in range(ROWS) and newCol in range(COLS) and
                    heights[r][c] >= heights[newRow][newCol] and (newRow, newCol) not in visited):
                        nodesToExpand.append((newRow, newCol))
                        visited.add((newRow, newCol))
                
            if inPacific and inAtlantic:
                result.append([row, col])


        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col)
        
        return result
                