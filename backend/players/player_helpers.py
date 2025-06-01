def change_player(player_index:int):
    return (player_index-1)*-1


def reset_players():
    return []


def create_player(players:list, player_name:str):
    player = [player_name]
    players.append(player)


def add_player_symbol(player:list, symbol:str):
    player[1]=symbol
