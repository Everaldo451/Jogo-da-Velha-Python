def add_game_path_to_sys():
    import sys
    import os
    path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    sys.path.append(path)


def select_option():
    while True:
        print("Selecione uma opção:")
        print("1 - Novo jogo")
        print("2 - Ver histórico de últimas partidas")
        print("3 - Finalizar jogo")

        opcao_selecionada = input("""""
        Selecione uma opção:
        1 - Novo jogo
        2 - Ver histórico de últimas partidas
        3 - Finalizar jogo
        """).replace(" ", "")  # Corrigido para tirar espaços corretamente

        if not opcao_selecionada.isdigit():
            print("Por favor, digite apenas dígitos.")
            continue
        
        opcao_num = int(opcao_selecionada)
        if opcao_num < 1 or opcao_num > 3:
            print("Valor inválido. Escolha uma opção entre 1 e 3.")
            continue
        
        return opcao_num
