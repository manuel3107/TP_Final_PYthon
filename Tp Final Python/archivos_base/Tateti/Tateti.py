import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Comprobar filas, columnas y diagonales
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    machine = "O"
    
    while True:
        print_board(board)
        
        # Turno del jugador
        while True:
            try:
                row = int(input("Elige la fila (0, 1, 2): "))
                col = int(input("Elige la columna (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Esa posición ya está ocupada. Intenta de nuevo.")
            except (ValueError, IndexError):
                print("Entrada no válida. Por favor, elige números entre 0 y 2.")
        
        if check_winner(board) == player:
            print_board(board)
            print("¡Felicidades! Has ganado.")
            break
        
        if is_board_full(board):
            print_board(board)
            print("¡Es un empate!")
            break
        
        # Turno de la máquina
        while True:
            row = random.randrange(3)
            col = random.randrange(3)
            if board[row][col] == " ":
                board[row][col] = machine
                break
        
        if check_winner(board) == machine:
            print_board(board)
            print("La máquina ha ganado. ¡Intenta de nuevo!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("¡Es un empate!")
            break

if __name__ == "__main__":
    main()