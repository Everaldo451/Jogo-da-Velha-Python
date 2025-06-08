from . import constants

def validate_matches_file_path(matches_file_path: str):
    for valid_extension in constants.VALID_FILE_EXTENSIONS:
        if matches_file_path.endswith(valid_extension):
            return True
    return False


def symbol_is_valid(symbol:str):
    return symbol in constants.VALID_SYMBOLS


def symbol_is_already_used(valid_symbol:str, remaining_symbols:list[str]):
    return valid_symbol not in remaining_symbols