"""O index, nesta função, é um valor de 0 a 8. A coluna e a linha são calculados automaticamente"""

def calculate_cell_line(line_count:int, index:int):
    return index//line_count


def calculate_cell_column(line_count:int, index:int):
    return index%line_count