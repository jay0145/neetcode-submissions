class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        NEIGHBOURS = [[1,0], [-1,0], [0,1], [0,-1]]

        fresh = 0
        minutesElapsed = 0
        queue = collections.deque()

        # pre-process all fruits and rotten oranges into queue
        # because of multi-source BFS - if two rotten oranges in same cluster
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        #BFS over DFS - DFS follows deepest route - want to expand frontiers simultaneously so BFS
        #if fresh runs out while rotten in queue, exit loop
        while queue:

            for i in range(len(queue)):
                row, col = queue.popleft()

                for rowDiff, colDiff in NEIGHBOURS:
                    newRow = row + rowDiff
                    newCol = col + colDiff
                    
                    if (newRow in range(ROWS) and 
                    newCol in range(COLS) and 
                    grid[newRow][newCol] == 1):
                        queue.append((newRow, newCol))
                        grid[newRow][newCol] = 2
                        fresh -= 1

            minutesElapsed += 1
        
        
        return -1 if fresh > 0 else max(0, minutesElapsed-1)