class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        if ROWS == 1 and COLS == 1:
            return True if matrix[0][0] == target else False

        for row in range(ROWS):
            l = 0
            r = COLS - 1
            while l <= r:
                index = (l + r) // 2
                print(f"{index}: l: {l}, r: {r} total: {l + r // 2}")

                elem = matrix[row][index]

                if elem == target:
                    return True
                
                if elem > target:
                    r = index - 1
                elif elem < target:
                    l = index + 1
                
        return False
        
        