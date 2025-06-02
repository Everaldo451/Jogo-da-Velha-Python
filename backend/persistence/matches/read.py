import csv

def read_matches(matches_file_path: str):
    with open(matches_file_path, newline="") as matches_data_file:
        match_reader = csv.reader(matches_data_file, delimiter=" ",quotechar="|")
        return [match_row for match_row in match_reader]