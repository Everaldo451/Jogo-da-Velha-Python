import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(BASE_DIR)

from players.test_create_player import test_create_player
from players.test_delete_players import test_delete_players
from players.test_change_player_index import test_change_player_index


test_create_player()
test_delete_players()
test_change_player_index()