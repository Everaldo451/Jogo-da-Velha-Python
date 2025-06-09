def add_game_path_to_sys():
    import sys
    import os
    path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    sys.path.append(path)


def select_option():
    while True:
        #adicionar parte para solicitar as opções a opcao_selecionada:
        #Opção 1: novo jogo
        #Opção 2: ver histórico de últimas partidas
        #Opção 3: finalizar jogo
        opcao_selecionada = input().replace("\s","")

        if not opcao_selecionada.isdigit():
            #mostrar mensagem de que deve conter apenas dígitos.
            continue
        if 3>int(opcao_selecionada)<1:
            #mostrar mensagem de valor errado.
            continue
        return int(opcao_selecionada)
