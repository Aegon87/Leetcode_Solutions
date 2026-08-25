class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # # Rough intuition:
        # for row in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[row][i] == ".":
        #             continue
        #         if board[row][i] in seen:
        #             return False
        #         seen.add(board[row][i])
                
        # for col in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[i][col] == ".":
        #             continue
        #         if board[i][col] in seen:
        #             return False
        #         seen.add(board[i][col])
        # return True

        row = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in row[r] or
                   board[r][c] in col[c] or 
                   board[r][c] in squares[(r//3, c//3)]):
                   return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True