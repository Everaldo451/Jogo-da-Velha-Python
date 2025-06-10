def verify_victory(board:list[list]):
    left_diagonal = [board[x][x] for x in range(len(board))]
    if all(cell == left_diagonal[0] for cell in left_diagonal) and left_diagonal[0] is not None:
        return True
    
    right_diagonal = [board[x][len(board)-(x+1)] for x in range(len(board))]
    if all(cell == right_diagonal[0] for cell in right_diagonal) and right_diagonal[0] is not None:
        return True
    
    columns = [[board[column][line] for column in range(len(board))] for line in range(len(board[0]))]
    for column in columns:
        if column[0] is not None and all(cell == column[0] for cell in column):
            return True

    for line in board:
        if line[0] is not None and all(cell == line[0] for cell in line):
            return True
        
    return False


def verify_empate(board:list[list]):
    return all(cell is not None for row in board for cell in row)


