from .order import order_matches_by_latest
import csv

def read_all_matches(matches_file_path: str):
    with open(matches_file_path, newline="") as matches_data_file:
        match_reader = csv.reader(matches_data_file, delimiter=" ",quotechar="|")
        return [match_row for match_row in match_reader]
    

def read_latest_n_matches(matches_file_path:str, n:int):
    all_matches = read_all_matches(matches_file_path)
    latest_n_matches = all_matches[-n:]
    order_matches_by_latest(latest_n_matches)
    return latest_n_matches
    