import random

def display_board(board):
    """
    The function accepts one parameter containing the board's current status
    and prints it out to the console.
    """
    print("+-------" * 3 + "+")
    for row in board:
        print("|       " * 3 + "|")
        print("|  " + "    |  ".join(str(cell) for cell in row) + "    |")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def enter_move(board):
    """
    The function accepts the board's current status, asks the user about their move, 
    checks the input, and updates the board according to the user's decision.
    """
    free_fields = make_list_of_free_fields(board)
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Choose a number between 1 and 9.")
                continue
            
            row, col = divmod(move - 1, 3)
            if (row, col) in free_fields:
                board[row][col] = 'O'
                break
            else:
                print("This field is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def make_list_of_free_fields(board):
    """
    The function browses the board and builds a list of all the free squares; 
    the list consists of tuples, while each tuple is a pair of row and column numbers.
    """
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ('O', 'X')]


def victory_for(board, sign):
    """
    The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game.
    """
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    """
    The function draws the computer's move and updates the board.
    """
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'
        
def main():
    board = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]  # Initialize board
    display_board(board)
    
    while True:
        # Player's turn
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You win!")
            break
        if not make_list_of_free_fields(board):
            print("It's a draw!")
            break
        
        # Computer's turn
        print("Computer's move:")
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer wins!")
            break
        if not make_list_of_free_fields(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()

