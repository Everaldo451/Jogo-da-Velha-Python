from logic.persistence.matches.read import read_latest_n_matches

def n_matches():
    #Inserir mensagem para adquirir quantidade de partidas
    quantidade_partidas = input()
    while not quantidade_partidas.isdigit():
        #Inserir mensagem deve ser numero
        quantidade_partidas = input()
    
    return int(quantidade_partidas)


def match_interpreter(match:list):
    winner_index:str = str(match[2])
    if not winner_index.isdigit():
        return [match[0], match[1], "Empate", match[2]]
    return [match[0], match[1], "Vitória", match[int(match[2])]]


def show_latest_n_matches(matches_file_path,n:int):
    print(" ".join(["Jogador1", "Jogador2", "Resultado", "Vencedor"]))
    latest_matches = read_latest_n_matches(matches_file_path, n)
    latest_matches = [
        match_interpreter(match) for match in latest_matches
    ]

    for interpreted_match in latest_matches:
        print(" ".join(interpreted_match))
