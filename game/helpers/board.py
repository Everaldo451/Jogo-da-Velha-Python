from logic.board.update_cell import update_cell, is_cell_updatable
from logic.board.board_helpers import calculate_cell_line, calculate_cell_column

def make_move(board:list[list], player:list[list]):
    while True:
        move_index = input()
        if not move_index.isdigit():
            #adicionar mensagem de deve ser apenas digitos
            continue
        elif (len(board)**2)<int(move_index)<1:
            #adicionar mensagem de index invalido
            continue

        move_index = int(move_index)-1
        line = calculate_cell_line(len(board), move_index)
        column = calculate_cell_column(len(board), move_index)

        if not is_cell_updatable(board, line, column):
            #adicionar mensagem de celula ja ocupada
            continue

        update_cell(board, line, column, player[1])
        break
    