from src.board.update_cell import update_cell, is_cell_updatable


def test_is_cell_updatable():
    board = [
        [None, None, None],
        [None, "X", None],
        ["X", None, None],
    ]

    assert is_cell_updatable(board, 0)
    assert not is_cell_updatable(board, 4)
    assert not is_cell_updatable(board, 6)


def test_update_cell():
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    update_cell(board, 4, "X")
    update_cell(board, 6, "O")

    assert board[1][1] == "X"
    assert board[2][0] == "O"
