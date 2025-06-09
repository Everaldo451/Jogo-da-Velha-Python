from logic.players.game_helpers import change_player_index

def test_change_player_index():
    players = [
        ["Everaldo", "X"],
        ["Andrey", "O"]
    ]

    player_index = 0
    player_index = change_player_index(player_index)
    player_index = change_player_index(player_index)
    
    assert players[player_index] == ["Everaldo", "X"]
