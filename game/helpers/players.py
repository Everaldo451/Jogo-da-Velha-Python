from logic.src.validators import symbol_is_valid, symbol_is_already_used
from logic.src.players.create import create_player

def create_players(players:list, symbols:list):
    while len(players) < 2:
        #adicionar mensagem para solicitar nome
        name = input()
        while True:
            #adicionar mensagem para solicitar simbolo
            symbol = input()
            if not symbol_is_valid(symbol):
                #adicionar mensagem de simbolo invalido
                continue
            elif symbol_is_already_used(symbol, symbols):
                #adicionar mensagem de simbolo ja utilizado
                continue
            symbols.remove(symbol)
            break

        create_player(players, name, symbol)