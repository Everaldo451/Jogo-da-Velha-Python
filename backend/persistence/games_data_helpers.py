def load_games_data(games_file_path: str):
    games_data_file = open(games_file_path, "r")
    data = games_data_file.read()
    games_data_file.close()
    return data


def validate_game_result_identifier(game_result_identifier:str):
    valid_game_results = ["E","V"]
    for valid_result in valid_game_results:
        if game_result_identifier == valid_result:
            return True
    
    return False


def insert_game(
        games_file_path:str,
        players:list[list],
        game_result_identifier:str,
        winner_index:int|None = None
        ):
    if not validate_game_result_identifier(game_result_identifier):
        return
    
    games_data_file = open(games_file_path, "a")
    
    player1_name = players[0][0]
    player2_name = players[1][0]
    game_string=f"{player1_name};{player2_name}={game_result_identifier}{winner_index}\n"
    games_data_file.write(game_string)
    games_data_file.close()
    

