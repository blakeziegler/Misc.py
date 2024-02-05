import random

# Class representing the game board
class Board:
    def __init__(self, n, m, alphabet, empty):
        # Initialize the board with dimensions, allowed alphabet, empty symbol, and moves counter
        self.__n = n
        self.__m = m
        self.__alphabet = alphabet
        self.__empty = empty
        self.__moves = 0
        # Create a 2D grid with the empty symbol
        self.grid = [[self.__empty for _ in range(m)] for _ in range(n)]

    def set(self, x, y, v):
        # Set a value in a specific cell on the board if conditions are met
        if self.is_onboard(x, y) and self.is_coordinate(x, y) \
                and (self.is_alphabet(v) or v == self.__empty) \
                and self.is_available(x, y):
            self.grid[x][y] = v
            self.__moves += 1

    def wipe(self):
        # Clear the board by setting all cells to the empty symbol
        for i in range(self.__n):
            for j in range(self.__m):
                self.set(i, j, self.__empty)
                
    def is_onboard(self,x,y):
        onboard=False
        if x in range(self.__n) and y in range(self.__m):
            onboard=True
            return onboard

    def is_coordinate(self,x,y):
        coordinate=False
        if type(x) == int and type(y) == int:
            coordinate = True
            return coordinate

    def is_alphabet(self,v):
        in_alphabet = False
        if v in self.__alphabet:
            in_alphabet = True
            return in_alphabet
        
    def is_available(self,x,y):
        available = False
        if self.grid[x][y] not in self.__alphabet:
            available = True
            return available
        
    def get(self, x, y):
    # function to get an x,y cell's value
        return self.grid[x][y]
    
    def get_dimension(self,axis="X"):
        if axis=="X":
            return(self.__n)
        else:
            return(self.__m)
        
    def get_alphabet(self):
        return self.__alphabet
    
    def __str__(self):
    # create a nice visualization of the board
        s = "Board (" + str(self.__moves) +")\n" +\
            "\n".join([" ".join([self.grid[i][j] for i in range(self.__m)]) for j in range(self.__n)]) + "\n"
        return s



# Class representing a player
class Player:
    def __init__(self, mark):
        # Initialize a player with a mark ("X" or "O") and win indicator
        self.mark = mark
        self.won = False

    def move(self, board):
        # Movement Rules:
        winning_move = self.find_winning_move(board)
        # Choose winning move if one is available
        if winning_move:
            x, y = winning_move
        # If no winning move available, choose a random legal move
        else:
            x, y = self.make_random_move(board)
        board.set(x, y, self.mark)

    def find_winning_move(self, board):
        # find a winning move on the board
        for i in range(board.get_dimension("X")):
            for j in range(board.get_dimension("Y")):
                if board.is_available(i, j):
                    # Create simulated board to recognize if winning move is possible
                    # Only way I could think of testing for winning move, definitly a more optimized solution out there
                    # get the current state of the board
                    sim_board = Board(board.get_dimension("X"), board.get_dimension("Y"), board.get_alphabet(), "")
                    # match the grids
                    sim_board.grid = [j[:] for j in board.grid]
                    # fill in the board with all possible moves
                    sim_board.set(i, j, self.mark)
                    # check if there is a winning outcome using the check_win def
                    if self.check_win(sim_board):
                        return i, j
        return False

    def check_win(self, board):
        # Check if the player has won on the given board
        # Use a for loop w/ conditional to check all possible win combinations
        # Horizontal win: if 3 X's or O's Y value is the same
        for i in range(board.get_dimension("X")):
            if all(board.get(i, j) == self.mark for j in range(3)):
                return True  # Horizontal win
        # Vertical win: if 3 X's or O's X value is the same
        for j in range(board.get_dimension("Y")):
            if all(board.get(i, j) == self.mark for i in range(3)):
                return True  # Vertical win
        # Diagonal win: if 3 X's or O's X value and Y value proportionaly increase/decrease  
        if all(board.get(i, i) == self.mark for i in range(board.get_dimension("X"))):
            return True  # Diagonal win (top-left to bottom-right)
        if all(board.get(i, board.get_dimension("Y") - 1 - i) == self.mark for i in range(board.get_dimension("X"))):
            return True  # Diagonal win (top-right to bottom-left)
        return False

    def make_random_move(self, board):
        # Make a random move on the board
        available_moves = [(i, j) for i in range(board.get_dimension("X")) for j in range(board.get_dimension("Y")) if
                           board.is_available(i, j)]
        return random.choice(available_moves)

# simulate the game
def play_game():
    # Initialize the board and players
    board = Board(3, 3, ["X", "O"], " ")
    count = 0
    # Create players
    player_X = Player("X")
    player_O = Player("O")

    # Cycle between player 1 and player 2 moves until there is a winner or tie
    while not player_X.won and not player_O.won:
        # end game if it is a tie (no available moves left)
        count += 1
        print("Player 1's move:")
        player_X.move(board)
        print(board)
        # end game if player 1 wins
        if player_X.check_win(board):
            player_X.won = True
            print("Player 1 wins!")
            break
        
        # if neither player wins on the 9th move, its a tie
        # this is placed here because player 1 always moves last
        if count == 9 and not (player_X.won or player_O.won):
            print("It's a tie!")
            break
        
        count += 1
        print("Player 2's move:")
        player_O.move(board)
        print(board)
        # end game if player 2 wins
        if player_O.check_win(board):
            player_O.won = True
            print("Player 2 wins!")
            break
        



# Run the game
play_game()


