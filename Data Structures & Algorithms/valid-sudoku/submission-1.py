class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item == ".":
                    continue
                if item in rows[row]:
                    return False
                if item in cols[col]:
                    return False
                if item in squares[(row // 3, col // 3)]:
                    return False
                rows[row].add(item)
                cols[col].add(item)
                squares[(row // 3, col // 3)].add(item)
        
        return True
        
                
