class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # check the row
        for r in range(9):
            for c in range(9):
                current = board[r][c]
                if current == '.':
                    continue

                # check the entire row
                if current in rows[r]:
                    return False

                # check the entire col
                if current in cols[c]:
                    return False

                # check all the squares
                if current in squares[(r//3,c//3)]:
                    return False
                
                # add current to each 
                rows[r].add(current)
                cols[c].add(current)
                squares[(r//3, c//3)].add(current)
        return True
                
