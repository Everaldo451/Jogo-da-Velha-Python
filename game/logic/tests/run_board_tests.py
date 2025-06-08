import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(BASE_DIR)

from board.test_board_create import test_create_board
from board.test_update_cell import test_update_cell, test_is_cell_updatable

test_create_board()
test_update_cell()
test_is_cell_updatable()