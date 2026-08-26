class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = False
        
        for row in range(9):
            counter = set()
            for col in range(9):
                item = board[row][col]
                #print(f'row:{row} col:{col} = {item}')
                if item == ".":
                    continue
                if item not in counter:
                    counter.add(item)
                else:
                    return False

        for col in range(9):
            counter = set()
            for row in range(9):
                item = board[row][col]
                #print(f'col:{col} row:{row} = {item}')
                if item == ".":
                    continue
                if item not in counter:
                    counter.add(item)
                else:
                    return False
            #print(counter)

        subgrids = [(0,0), (3,0), (6,0), (0,3), (3, 3), (6,3), (0, 6), (3, 0), (6, 6)]

        for i,j in subgrids:
            counter = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    print(f'row{row} col:{col} = {item}')
                    if item == ".":
                        continue
                    if item not in counter:
                        counter.add(item)
                    else:
                        return False
        
        return True
        
                
