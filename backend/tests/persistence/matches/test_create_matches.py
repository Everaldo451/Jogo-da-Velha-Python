from src.persistence.matches.create import create_match
import os
from . import path
matches_file_path = os.path.join(path,"data", "matches_to_create.csv")

def test_create_match():
    players = [
        ["Everaldo","X"],
        ["Andrey","O"]
    ]
    winner_index=0
    create_match(matches_file_path, players, winner_index)

    assert os.path.exists(matches_file_path)

    first_line = None
    with open(matches_file_path, "r") as matches_file:
        first_line = matches_file.readline().replace("\n","")

    os.remove(matches_file_path)
    assert first_line == f"{players[0][0]} {players[1][0]} {winner_index}"