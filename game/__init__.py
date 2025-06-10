from helpers import add_game_path_to_sys, select_option
from helpers.messagers import game_start, game_end
from helpers.matches import n_matches, show_latest_n_matches
from helpers.players import create_players
from helpers.board import make_move
from logic.board.create_board import create_board
import configs
import random
import os

def run():
    add_game_path_to_sys()
    game_start()
    while True:
        opcao_selecionada = select_option()

        #Opção 1: novo jogo
        #Opção 2: ver histórico de últimas partidas
        #Opção 3: finalizar jogo
        if opcao_selecionada==1:
            players = []
            symbols = ["X", "O"]
            create_players(players, symbols)
            symbols = None
            print(players)
            board = create_board()
            player_index = random.randint(0, 1)
            while True:
                make_move(board, players[player_index])
                player_index = (player_index-1)*-1
            continue
        elif opcao_selecionada==2:
            quantidade_partidas = n_matches()
            arquivo_partidas_caminho = os.path.join(configs.BASE_DIR, "data", "matches.csv")
            show_latest_n_matches(arquivo_partidas_caminho, quantidade_partidas)
            continue
        elif opcao_selecionada==3:
            game_end()
            break