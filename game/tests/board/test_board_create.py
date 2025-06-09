from logic.board.create_board import create_board

def test_create_board():
    
    board = create_board()

    assert board == [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]