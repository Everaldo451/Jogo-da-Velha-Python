import csv
"""
Quando o winner_index é igual a '-', significa empate.
"""
def create_match(
        matches_file_path:str,
        players:list[list],
        winner_index:int|str = "-"
        ):
    with open(matches_file_path, "a", newline="") as matches_data_file:
        match_writer = csv.writer(
            matches_data_file, 
            delimiter=" ", 
            quotechar="|", 
            quoting=csv.QUOTE_MINIMAL
            )

        player1_name = players[0][0]
        player2_name = players[1][0]
        match_writer.writerow([player1_name, player2_name, winner_index])