from .board_helpers import calculate_cell_column, calculate_cell_line

def is_cell_updatable(board:list[list], index:int):
    line_count = len(board)
    line = calculate_cell_line(line_count, index)
    column = calculate_cell_column(line_count, index)

    if board[line][column] is not None:
        return False
    return True


def update_cell(board: list[list], index:int, value:str):
    line_count = len(board)
    line = calculate_cell_line(line_count, index)
    column = calculate_cell_column(line_count, index)

    board[line][column] = value
