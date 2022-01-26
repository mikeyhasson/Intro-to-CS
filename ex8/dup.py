WHITE = 0
BLACK = 1
UNKNOWN_COLOR = -1
ROW_INDEX = 0
COLUMN_INDEX = 1


def get_row_variations(row, blocks):
    return get_row_variations_helper(row[:], blocks, 0)


def color_index(temp, index, color):
    new_lst = temp[:]
    if temp[index] == UNKNOWN_COLOR:
        new_lst[index] = color
    return new_lst


def block_ok(temp, req_blocks_list):
    lst = temp[:]
    cur_blocks_list = req_blocks_list[:]
    count = 0
    i = 0
    while i < len(lst) and BLACK in lst:
        i = lst.index(BLACK)
        while i < len(lst) and lst[i] == BLACK:
            count += 1
            i += 1
        if count not in cur_blocks_list:
            return False
        elif count !=cur_blocks_list[0]:
            return False
        else:
            cur_blocks_list.pop(0)
        lst = lst[i:]
        i, count = 0, 0
    if cur_blocks_list == []:
        return True
    return False


def get_row_variations_helper(temp, blocks, index):
    index = temp.index(UNKNOWN_COLOR, index) if UNKNOWN_COLOR in temp[index:] else len(temp)
    if index == len(temp):
        if block_ok(temp, blocks):
            return [temp[:]]
        return []

    coloring_lst = []
    coloring_lst += get_row_variations_helper(color_index(temp, index, WHITE), blocks, index + 1)

    coloring_lst += get_row_variations_helper(color_index(temp, index, BLACK), blocks, index + 1)

    return coloring_lst


def get_intersection_row(rows):
    if rows == []:
        return []
    new_row = []
    for i in range(len(rows[0])):
        val = rows[0][i]
        for row in rows:
            if row[i] != val:
                val = UNKNOWN_COLOR
        new_row.append(val)
    return new_row

def create_board (constraints):
    board = []
    def_row = [-1] * len(constraints[COLUMN_INDEX])
    for i in range(len(constraints[ROW_INDEX])):

        blocks = constraints[ROW_INDEX][i]
        new_row = get_intersection_row(get_row_variations(def_row, blocks))
        if new_row != None:
            board.append(new_row)
        else:
            return None
    return board

def row_board_to_columns (board,constraints):
        columns_board = []
        for j in range(len(board[0])):
            column = []
            for i in range(len(board)):
                column.append(board[i][j])

            block = constraints[COLUMN_INDEX][j]
            column = get_intersection_row(get_row_variations(column, block))
            if column != None:
                columns_board.append(column)
            else:
                return None
        return columns_board

def columns_to_rows (board):
    new_board=[]
    for i in range(len(board[0])):
        row=[]
        for j in range(len(board)):
            row.append(board[j][i])
        new_board.append(row)
    return new_board

def check_rows(board,constraints):
    new_board=[]
    for index,row in enumerate(board):
        blocks = constraints[ROW_INDEX][index]
        new_row = get_intersection_row(get_row_variations(row, blocks))
        new_board.append(new_row)
    return new_board

def solve_easy_nonogram(constraints):
    board=create_board(constraints)
    solution=columns_to_rows(row_board_to_columns(board,constraints))
    while board != solution:
        board=check_rows(solution,constraints)
        solution=columns_to_rows(row_board_to_columns(board,constraints))
    return solution

def solve_nonogram(constraints):
    board=solve_easy_nonogram(constraints)
    return solve_nonogram_helper(board,constraints,0,[])

def nonogram_ok (board,constraints):
    rows=check_rows(board,constraints)
    columns=row_board_to_columns(board,constraints)
    if rows and columns:#if both are not "None"
        return True
    return False

def solve_nonogram_helper(board,constraints,row,sol_lst):
    if row==len(board):
        if nonogram_ok(board,constraints):
         sol_lst.append(board)
        return

    blocks=constraints[ROW_INDEX][row]
    row_variations=get_row_variations(board[row], blocks)
    for variation in row_variations:
        temp=board[:]
        temp[row]=variation
        solve_nonogram_helper(temp,constraints,row+1,sol_lst)
    return sol_lst


def count_row_variations(length, blocks):
    pass


if __name__ == "__main__":
    const= [[[2], [2, 1], [1, 3], [1, 1, 1, 1], [1, 1, 5],
                              [1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1],
                              [1, 1, 1, 1],
                              [1, 1, 4, 3], [4, 3, 2], [1, 1, 1, 1, 1],
                              [7, 2, 1],
                              [1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 1],
                              [1, 1, 5, 3],
                              [1, 1, 5, 1, 1], [1, 1, 2, 2, 1, 1],
                              [1, 1, 2, 2, 1, 1], [1, 1, 1, 1, 5],
                              [1, 1, 2, 2, 1, 1]],
                             [[1, 2], [6, 9], [1, 1], [16], [1, 1, 1],
                              [1, 7, 1],
                              [2, 1, 2, 6], [2, 2, 2], [1, 2, 2, 6],
                              [1, 1, 1, 1, 6, 1], [2, 3, 2, 1, 1],
                              [1, 1, 1, 2, 10], [4, 2, 2, 1, 1, 1], [11],
                              [1]]]
    print (solve_easy_nonogram(const))


