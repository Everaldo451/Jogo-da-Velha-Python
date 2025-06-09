from .board_helpers import calculate_cell_column, calculate_cell_line

def is_cell_updatable(board:list[list], line:int, column:int):
    if board[line][column] is not None:
        return False
    return True


def update_cell(board: list[list], line:int, column:int, value:str):
    board[line][column] = value
