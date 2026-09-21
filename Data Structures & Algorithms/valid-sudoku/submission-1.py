class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isValidGroup(cells):
            unique = set()

            for cell in cells:
                if cell != ".":
                    if cell in unique:
                        return False
                    unique.add(cell)

            return True


        # Check rows
        for row in board:
            if not isValidGroup(row):
                return False


        # Check columns
        for c in range(9):
            col = []

            for r in range(9):
                col.append(board[r][c])

            if not isValidGroup(col):
                return False


        # Check 3x3 boxes
        for rowStart in range(0, 9, 3):
            for colStart in range(0, 9, 3):
                box = []

                for r in range(rowStart, rowStart + 3):
                    for c in range(colStart, colStart + 3):
                        box.append(board[r][c])

                if not isValidGroup(box):
                    return False


        return True