#################################################################
# FILE : nonogram.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex 2020
# DESCRIPTION: nonogram puzzle solver
# NOTE: In func get_row_variations_helper, i have chosen to use "-1" because in func solve_easy_nonogram we have both
#       the row constraints and the column constraints and so if we hadn't kept it as -1, and chosen a different value,
#       it might wouldn't fit the row constraints.
#################################################################
import math

WHITE = 0
BLACK = 1
UNKNOWN_COLOR = -1
ROW_INDEX = 0
COLUMN_INDEX = 1

def color_index(row, index, color):
    """
    This function colors an index within a row
    :param row: nonogram row
    :param index: index within row
    :param color: BLACK/WHITE/UNKNOWN_COLOR
    :return: colored index row
    """
    new_row = row[:]
    new_row[index] = color
    return new_row


def block_ok(row, blocks_list):
    """
    This function recieves a nonogram row and a blocks_list and checks if the row matches the constraints
    :param row: nonogram row
    :param blocks_list: block constraints
    :return: True if row matches constraints, else, False
    """
    i = 0
    block_index = -1
    while BLACK in row[i:]:
        i=row.index(BLACK,i)
        if WHITE in row[i:]:
            j=row.index(WHITE,i)
        else:
            j=len(row)
        block_index+=1
        if block_index > len(blocks_list) -1:
            return False
        if not j-i==blocks_list[block_index]:
            return False
        i=j
    return True

def get_row_variations_helper(row, blocks, index, block_sum,row_len,w_count,b_count,u_count):
    """
    This function is the recursive function of "get_row_variations". This function uses backtracking.
    :param row: nonogram row
    :param blocks: blocks constraints list
    :param index: current index to alter.
    :return:
    """
    if b_count > block_sum: #if the row has more black indexes than required
        return []
    if w_count > row_len - block_sum:#if the row has more white indexes than required
        return []
    if u_count>0: #if we have more indexes to discover
        index = row.index(UNKNOWN_COLOR, index) #set index to the first to discover
    else:
        index = row_len #if we have found all indexes, set index to the end of the list

    if index == row_len: #got to the end of row
        if block_ok(row, blocks): #if row matches constraints, return it.
            return [row[:]]
        return []

    coloring_lst = []
    #coloring undiscovered index white
    coloring_lst += get_row_variations_helper(color_index(row, index, WHITE), blocks, index + 1,block_sum,row_len,w_count+1,b_count,u_count-1)
    #coloring undiscovered index black
    coloring_lst += get_row_variations_helper(color_index(row, index, BLACK), blocks, index + 1,block_sum,row_len,w_count,b_count+1,u_count-1)

    return coloring_lst

def get_row_variations(row, blocks):
    """
    This function recieves a row and a list of constraints and return a list of possible variations of the row
    :param row: nonogram row
    :param blocks: list of block constraints
    :return: a list of possible variations of the row
    """
    return get_row_variations_helper(row[:], blocks, 0,sum(blocks),len(row),row.count(WHITE),row.count(BLACK),row.count(UNKNOWN_COLOR))

def get_intersection_row(rows):
    """
    This function finds the intersection of different row variations.
    :param rows:list of possible rows
    :return:intersection of the rows
    """
    if not rows:
        return []
    new_row = []
    for i in range(len(rows[0])):
        val = rows[0][i]
        for row in rows:
            if row[i] != val:
                val = UNKNOWN_COLOR
        new_row.append(val)
    return new_row


def create_board(constraints):
    """
    This function creates a nonogram board based on a list of constraints and partially fills it
    based on row constraints only.
    :param constraints: list of block  constraints
    :return:nonogram board
    """
    board = []
    def_row = [-1] * len(constraints[COLUMN_INDEX])
    for i in range(len(constraints[ROW_INDEX])):

        blocks = constraints[ROW_INDEX][i]
        new_row = get_intersection_row(get_row_variations(def_row, blocks))
        if not new_row: #if there are no row variations, the nonogram is incorrect.
            return None
        else:
            board.append(new_row)
    return board


def row_board_to_columns(board):
    """
    This function turns a list of lists of rows turns to list of lists of columns
    :param board: a list of lists of rows
    :return: list of lists of columns
    """
    columns_board = []
    for j in range(len(board[0])):
        column = []
        for i in range(len(board)):
            column.append(board[i][j])
        columns_board.append(column)
    return columns_board


def columns_to_rows(board):
    """
    This function turns a list of lists of columns turns to list of lists of rows
    :param board: a list of lists of columns
    :return: list of lists of rows
    """
    if board is None:
        return None
    new_board = []
    for i in range(len(board[0])):
        row = []
        for j in range(len(board)):
            row.append(board[j][i])
        new_board.append(row)
    return new_board


def check_rows(board, constraints, constraints_index=ROW_INDEX):
    """
    This function recvieves a nonogram board, goes through the rows that contain an Unknown color and
    tries to figure out the color using  get_intersection_row and get_row_variations
    :param board: nonogram board
    :param constraints: list of block constraints
    :param constraints_index: default - ROW_INDEX, when used in check_columns, COLUMN_INDEX
    :return: nonogram board with rows discovered as much a possible
    """
    if board is None:
        return None
    new_board = []
    for row_index, row in enumerate(board):
        blocks = constraints[constraints_index][row_index]
        if UNKNOWN_COLOR in row:
            new_row = get_intersection_row(get_row_variations(row, blocks))
            if not new_row:
                return None
        else:
            new_row = row #no need to check rows without UNKNOWN_COLOR
        new_board.append(new_row)
    return new_board


def check_columns(board, constraints):
    """
    This function recieves a nonogram board and tries to discover unknown colors in columns.
    :param board: nonogram board
    :param constraints: list of block constraints
    :return: nonogram board with coumns discovered as much a possible
    """
    if board is None:
        return None
    new_board = row_board_to_columns(board) #turn to a list of lists of columns
    new_board = check_rows(new_board, constraints, COLUMN_INDEX) #discover colors
    new_board = columns_to_rows(new_board)# turn back to a list of lists of rows
    return new_board


def solve_easy_nonogram(constraints):
    """
    This function recieves a list of an easy nonogram puzzle constraints and solves the nonogram puzzle.
    An easy nonogram puzzle is one for which there is no need to guess any color.
    :param constraints: a list of block constraints
    :return: solved nonogram puzzle.
    """
    board = create_board(constraints)
    solution = check_columns(board, constraints)
    while board != solution:
        board = check_rows(solution, constraints)
        solution = check_columns(board, constraints)
    return solution


def solve_nonogram(constraints):
    """
    This function solves any nonogram puzzle, including complex ones.
    :param constraints: a list of block constraints
    :return: List of possible nonogram puzzle solutions
    """
    board = solve_easy_nonogram(constraints)
    return solve_nonogram_helper(board[:], constraints, 0, [])


def nonogram_ok(board, constraints):
    """
    This function check if a filled nonogram puzzle matches the constraints
    :param board: nonogram puzzle
    :param constraints: a list of block constraints
    :return: True if board matches constraints, else, False
    """
    rows = check_rows_bool(board, constraints, ROW_INDEX)
    column_board = row_board_to_columns(board)
    columns = check_rows_bool(column_board, constraints, COLUMN_INDEX)
    return rows and columns


def check_rows_bool(board, constraints, constraints_index):
    """
    This function recieves filled nonogram board, and checks if its rows match the constraints
    :param board: nonogram puzzle
    :param constraints: a list of block constraints
    :param constraints_index: ROW_INDEX for rows, COLUMN_INDEX for columns
    :return: True if rows match constraints
    """
    for row_index, row in enumerate(board):
        blocks = constraints[constraints_index][row_index]
        if not block_ok(row, blocks):
            return False
    return True


def solve_nonogram_helper(board, constraints, row, sol_lst):
    """
    This function solves nonogram puzzles using backtracking. It tries every variation of a row and checks the final
    result.
    :param board: a board, partially filled using solve_easy_nonogram
    :param constraints: a list of block constraints
    :param row: current row we are altering
    :param sol_lst: a list of solutions.
    :return:
    """
    if row == len(board):
        if nonogram_ok(board, constraints):
            sol_lst.append(board)
        return

    blocks = constraints[ROW_INDEX][row]
    if UNKNOWN_COLOR in board[row]:
        row_variations = get_row_variations(board[row], blocks)
    else:
        row_variations = [board[row]]

    for variation in row_variations:
        temp = board[:]
        temp[row] = variation
        solve_nonogram_helper(temp, constraints, row + 1, sol_lst)
    return sol_lst


def formula_for_variations(a,b):
    """
    This function calculates the formula (a+b) choose a.
    :param a: number of blocks
    :param b: number of whites
    :return: formula value
    """
    return math.factorial(a+b) / (math.factorial(b) * math.factorial(a))

def variations_for_two (length, blocks):
    """
    This function finds the amount of variations for 2 or less blocks.
    Logic - if we mark each block as "|" and every 0 as *.
    For one block (ex. *|*) the amount of options is number of objects (in ex. = 3) choose number of "|".
    If we have 2 blocks, we can't have variations like ||*. however the amount of these is equivlent to the amount
    of these |*. So we do s+t choose s - s-1+t chose s-1.
    :param length: length of the row
    :param blocks: list of blocks.
    :return:
    """
    sum_of_blocks = sum(blocks)
    number_of_blocks = len(blocks)
    number_of_whites = length - sum_of_blocks
    if number_of_whites == 0 and number_of_blocks > 1:
        return 0
    formula=formula_for_variations(number_of_blocks,number_of_whites)
    if number_of_blocks==2:
        formula-=formula_for_variations(number_of_blocks-1,number_of_whites)
    return formula

def count_row_variations(length, blocks):
    """
    This function calculates the amount of row variations for an unknown row size "length", and has
    a constraint  "blocks".
    LOGIC: dividing the blocks list into 2 smaller lists, for each we can calculate how many options there are,
    then multiply.
    :param length: length of the row
    :param blocks: list of block constraints.
    :return:amount of row variations
    """
    count=0
    n=len(blocks)
    if n<=2:
        return variations_for_two(length, blocks)
    if sum(blocks)+len(blocks)-1 == length:
        return 1
    index=(n // 2 ) if n%2==0 else n//2 +1
    list_a=blocks[:index]
    list_b=blocks[index:]
    sub_len=sum(list_a)+len(list_a)-1
    count+=count_row_variations(sub_len,list_a)*count_row_variations(length-sub_len-1,list_b)
    index=(n // 2 - 1) if n%2==0 else n//2
    list_a=blocks[:index]
    list_b=blocks[index:]
    sub_len=sum(list_b)+len(list_b)-1
    count+=count_row_variations(length-sub_len-1,list_a)*count_row_variations(sub_len,list_b)
    return count

if __name__=="__main__":
    print(get_row_variations([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],[50]))
