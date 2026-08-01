class Board:
    """
        Where the game takes place
        Maintains everything related to the board, such as player moves, marker placement and grid management
    """
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]


    def displayBoard(self):
        """ To display the board with the correct spaces and layout """
        for i in range(3):
            print(" " + " | ".join(self.grid[i]) + " ")
            if i < 2:
                print("--- --- ---")


    def isValidMove(self, row, col):
        """ Checks if the move is within bounds of the board and that it is an empty space """
        if row > 2 or row < 0 or col < 0 or col > 2:
            print("Invalid move")
            return False

        if self.grid[row][col] != " ":
            print("Already a marker at this position")
            return False

        return True
    

    def placeMarker(self, row, col, marker):
        """ Placing the marker on the board """
        if self.isValidMove(row, col):
            self.grid[row][col] = marker
            return True
        return False
        

    def isFull(self):
        """ Checking if the board has no more empty spaces left """
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == " ":
                    return False
        return True


    def reset(self):
        """ Emptying all the blocks for a new game """
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
        return True





class GameEngine:
    def __init__(self):
        self.board = Board()
        self.scores = {"X": 0, "O": 0, "Ties": 0}
        self.curr_player = "X"


    def switchTurn(self):
        """ Hands over turn from one player to another """
        if self.curr_player == "X":
            self.curr_player = "O"
        else:
            self.curr_player = "X"


    def checkWinner(self):
        """ Checks if there is a winner at this moment in the game """
        for i in range(3):
            if self.board.grid[0][i] == self.board.grid[1][i] == self.board.grid[2][i] != " ":
                return self.board.grid[0][i]

            if self.board.grid[i][0] == self.board.grid[i][1] == self.board.grid[i][2] != " ":
                return self.board.grid[i][0]

        if self.board.grid[0][0] == self.board.grid[1][1] == self.board.grid[2][2] != " ":
            return self.board.grid[0][0]

        if self.board.grid[0][2] == self.board.grid[1][1] == self.board.grid[2][0] != " ":
            return self.board.grid[0][2]

        return None
        

    def checkTie(self):
        """ Checks for a tie """
        if self.board.isFull and self.checkWinner() is None:
            return True
        return False 





class CLIHandler:
    def __init__(self):
        self.game = GameEngine()


    def getPlayerInput(self):
        while True:
            raw_input = input(f"Player {self.game.curr_player}, please enter the row(0-2) and col(0-2) for your marker(1 2) or q to quit: ").strip().lower()

            if raw_input in ["q", "quit"]:
                return "quit"

            split_input = raw_input.split()

            if len(split_input) == 2:
                try:
                    row = int(split_input[0])
                    col = int(split_input[1])

                    if self.game.board.isValidMove(row, col):
                        return row, col
                    
                except:
                    pass

            print("Invalid format, please enter the position for your marker correctly\n")


    def runGame(self):
        print("==WELCOME TO TIC TAC TOE==")

        while True:
            self.game.board.displayBoard()
            input = self.getPlayerInput()

            if input == "quit":
                print("GAME ENDED!")
                break 

            row, col = input 
            self.game.board.placeMarker(row, col, self.game.curr_player)

            winner = self.game.checkWinner()
            if winner:
                self.game.board.displayBoard()
                print(f"Player {winner} wins!")
                self.game.scores[winner] += 1
                break 

            if self.game.board.isFull():
                self.game.board.displayBoard()
                print("It is a tie!")
                self.game.scores["Ties"] += 1
                break 

            self.game.switchTurn()




if __name__ == "__main__":
    cli = CLIHandler()
    cli.runGame()