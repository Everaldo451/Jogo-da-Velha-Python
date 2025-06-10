import sys
import os

GAME_DIR = os.path.join(os.path.dirname(__file__), "game")
sys.path.append(GAME_DIR)

from game import run

run()