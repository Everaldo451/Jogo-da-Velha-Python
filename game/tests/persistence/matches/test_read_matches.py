from logic.persistence.matches.read import read_all_matches, read_latest_n_matches
import os
from . import path
matches_file_path = os.path.join(path,"data", "matches_to_read.csv")

def test_read_all_matches():
    all_matches = read_all_matches(matches_file_path)
    expected_output = [
        ["Everaldo", "Andrey", "0"],
        ["Andrey", "Everaldo", "1"],
        ["Jogador1", "Jogador2", "-"],
        ["Jogador3", "Jogador4", "-"]
    ]

    assert all_matches == expected_output


def test_3_latest_matches():
    three_latest_matches = read_latest_n_matches(matches_file_path, 3)
    expected_output = [
        ["Jogador3", "Jogador4", "-"],
        ["Jogador1", "Jogador2", "-"],
        ["Andrey", "Everaldo", "1"],
    ]

    assert three_latest_matches == expected_output


