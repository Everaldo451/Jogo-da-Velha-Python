from logic.board.update_cell import update_cell, is_cell_updatable
from logic.board.board_helpers import calculate_cell_line, calculate_cell_column

def make_move(board: list[list], player: list[list]):
    while True:
        move_index = input(f"{player[0]}, digite o número da célula para fazer sua jogada: ")
        if not move_index.isdigit():
            print("Entrada inválida! Por favor, digite apenas dígitos numéricos.")
            continue
        elif (len(board)**2)<int(move_index)<1:
            print(f"Índice inválido! Digite um número entre 1 e {len(board)**2}.")
            continue

        move_index = int(move_index) - 1
        line = calculate_cell_line(len(board), move_index)
        column = calculate_cell_column(len(board), move_index)

        if not is_cell_updatable(board, line, column):
            print("Célula já ocupada! Por favor, escolha outra célula.")
            continue

        update_cell(board, line, column, player[1])
        break

def show_board(board: list[list]):
    print("\n--- Tabuleiro Atual ---")
    board_size = len(board)
    for r_idx, row in enumerate(board):
        row_display = []
        for c_idx, cell in enumerate(row):
            # Adiciona o valor da célula ou o número da célula se estiver vazia
            if cell == None:
                # Calcula o número da célula (começando de 1)
                cell_number = r_idx * board_size + c_idx + 1
                row_display.append(f" {cell_number:2d} ") # Formata para ter 2 dígitos, alinhado à direita
            else:
                row_display.append(f"  {cell}  ") # Adiciona espaços para alinhamento

        print("|".join(row_display))
        if r_idx < board_size - 1:
            print("-" * (len(row_display) * 5 - 1)) # Linha divisória entre as linhas do tabuleiro
    print("---------------------\n")


board = [[None for _ in range(3)] for i in range(3)]

show_board(board)