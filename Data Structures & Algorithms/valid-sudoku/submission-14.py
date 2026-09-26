class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)        
        col = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                
                currentBox = (r//3 , c//3)

                if board[r][c] in row[r]:
                    return False
                elif board[r][c] in col[c]:
                    return False
                elif board[r][c] in boxes[currentBox]:
                    return False

                row[r].add(board[r][c])
                col[c].add(board[r][c])
                boxes[currentBox].add(board[r][c])             

        return True