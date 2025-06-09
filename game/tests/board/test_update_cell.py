from logic.board.update_cell import update_cell, is_cell_updatable
from logic.board.board_helpers import calculate_cell_line, calculate_cell_column


def test_is_cell_updatable():
    board = [
        [None, None, None],
        [None, "X", None],
        ["X", None, None],
    ]

    line = calculate_cell_line(len(board), 0)
    column = calculate_cell_column(len(board), 0)
    assert is_cell_updatable(board, line, column)
    line = calculate_cell_line(len(board), 4)
    column = calculate_cell_column(len(board), 4)
    assert not is_cell_updatable(board, line, column)
    line = calculate_cell_line(len(board), 6)
    column = calculate_cell_column(len(board), 6)
    assert not is_cell_updatable(board, line, column)


def test_update_cell():
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    line = calculate_cell_line(len(board), 4)
    column = calculate_cell_column(len(board), 4)
    update_cell(board, line, column, "X")
    line = calculate_cell_line(len(board), 6)
    column = calculate_cell_column(len(board), 6)
    update_cell(board, line, column, "O")

    assert board[1][1] == "X"
    assert board[2][0] == "O"
