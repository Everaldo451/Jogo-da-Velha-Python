from .. import configs

def validate_matches_file_path(matches_file_path: str):
    for valid_extension in configs.VALID_FILE_EXTENSIONS:
        if matches_file_path.endswith(valid_extension):
            return True

    return False


def validate_match_result_identifier(game_result_identifier:str):
    for valid_result in configs.VALID_GAME_RESULTS:
        if game_result_identifier == valid_result:
            return True
    
    return False