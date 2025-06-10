from logic.validators import symbol_is_valid, symbol_is_already_used
from logic.players.create import create_player

def create_players(players: list, symbols: list):
    # Damos boas-vindas aos jogadores
    print("Vamos configurar os jogadores para o Jogo da Velha!")

    while len(players) < 2:
        player_number = len(players) + 1
        # Adicionar mensagem para solicitar nome
        print(f"\nJogador {player_number}, por favor, digite seu nome:")
        name = input()

        while True:
            # Adicionar mensagem para solicitar simbolo
            print(f"{name}, escolha um símbolo para jogar (ex: X, O, #):")
            symbol = input().strip() # .strip() remove espaços em branco extras

            if not symbol_is_valid(symbol):
                # Adicionar mensagem de simbolo invalido
                print("Símbolo inválido! Por favor, escolha um único caractere que não seja um número ou espaço.")
                continue
            elif symbol_is_already_used(symbol, symbols):
                # Adicionar mensagem de simbolo ja utilizado
                print("Símbolo já em uso! Por favor, escolha outro.")
                continue
            
            # Se o símbolo for válido e não estiver em uso, removemos ele da lista de símbolos disponíveis
            # para evitar que seja escolhido novamente.
            if symbol in symbols: # Verificamos se o símbolo ainda está na lista para evitar KeyError
                symbols.remove(symbol)
            else:
                # Caso o símbolo não estivesse na lista original 'symbols' (por exemplo, se 'symbols'
                # contiver apenas 'X' e 'O' e o usuário digitar '#'), não há problema.
                # A ideia é que 'symbols' seja uma lista dos *símbolos permitidos*,
                # e a remoção garante que não sejam reutilizados.
                pass 
            break

        create_player(players, name, symbol)
        print(f"Ótimo! Jogador {name} ({symbol}) configurado.")

    print("\nTodos os jogadores estão prontos! Vamos começar a jogar!")