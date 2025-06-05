from src.persistence.matches.read import read_all_matches, read_latest_n_matches
import os
from . import path
matches_file_path = os.path.join(path,"data", "matches_to_read.csv")

def test_read_all_matches():
    all_matches = read_all_matches(matches_file_path)
    expected_output = [
        ["Everaldo", "Andrey", "V", "0"],
        ["Andrey", "Everaldo", "V", "1"],
        ["Jogador1", "Jogador2", "E", "0"],
        ["Jogador3", "Jogador4", "E", "0"]
    ]

    assert all_matches == expected_output


def test_3_latest_matches():
    three_latest_matches = read_latest_n_matches(matches_file_path, 3)
    expected_output = [
        ["Jogador3", "Jogador4", "E", "0"],
        ["Jogador1", "Jogador2", "E", "0"],
        ["Andrey", "Everaldo", "V", "1"],
    ]
    print(three_latest_matches)

    assert three_latest_matches == expected_output


