from src.players.create import create_player


def test_create_player():
    players = []

    create_player(players, "Everaldo", "X")
    assert players == [["Everaldo", "X"]]