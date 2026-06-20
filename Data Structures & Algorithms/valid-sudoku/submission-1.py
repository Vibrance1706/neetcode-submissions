class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col=0,0
        valid_list = []
        board_int = []
        for i in range(len(board)):
            board_int_row = []
            for j in range(len(board[i])):
                if board[i][j]!='.':
                    board_int_row.append(int(board[i][j]))
                else:
                    board_int_row.append(0)

            board_int.append(board_int_row)

        row = 0
        while row < 9:
            seen_list_row = []
            col = 0
            while col < 9:
                val = board_int[row][col]
                if val != 0:
                    if val in seen_list_row:
                        return False
                    seen_list_row.append(val)
                col += 1
            row += 1

        col = 0
        while col < 9:
            seen_list_col = []
            row = 0
            while row < 9:
                val = board_int[row][col]
                if val != 0:
                    if val in seen_list_col:
                        return False
                    seen_list_col.append(val)
                row += 1
            col += 1

        box_row = 0
        while box_row < 9:
            box_col = 0
            while box_col < 9:
                seen_list_box = []
                i = box_row
                while i < box_row + 3:
                    j = box_col
                    while j < box_col + 3:
                        val = board_int[i][j]
                        if val != 0:
                            if val in seen_list_box:
                                return False
                            seen_list_box.append(val)
                        j += 1
                    i += 1
                box_col += 3
            box_row += 3

        return True



