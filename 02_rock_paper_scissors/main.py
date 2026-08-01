import random

class GameEngine:
    """ 
        Manages rules, choices and current game session state 
        Basically manages all game logic
    """

    def __init__(self):
        self.valid_moves = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.ai_score = 0
        self.ties = 0


    def AIMove(self):
        """ Chooses from a list of valid moves for the AI """
        ai_move = random.choice(self.valid_moves)
        return ai_move


    def determineWinner(self, AI_move, user_move):
        """ determines the winner from the player and the AI """
        if AI_move == user_move:
            return "tie"

        win_conditions = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if win_conditions[user_move] == AI_move:
            return "user"
        return "AI"


    def updateScore(self, winner):
        """ Updates the score of the winner """

        if winner == "user":
            self.user_score += 1
        elif winner == "AI":
            self.ai_score += 1
        else: 
            self.ties += 1        


    def getScoreSummary(self):
        """ So that the score can be displayed during and at the end of the game """
        print(f"User score: {self.user_score} || AI score: {self.ai_score} || Total Ties: {self.ties}")




class CLIHandler:
    """
        This class is to read input from player and print the score
        CLI : Command-line-interface
            This is used when the input taken from the user is in written / text format
            instead of a button / icon
        GUI : Graphical-user-interface 
            This is used when the input comes from buttons / icons / menus etc
    """

    def __init__(self):
        self.game = GameEngine()


    def getUserInput(self):
        """ Get user input and validate """
        while True:
            user_input = input("Enter rock, paper or scissors (enter q to quit game): ").strip().lower()

            if user_input in ["q", "quit"]:
                return "quit"

            if user_input in self.game.valid_moves:
                return user_input

            print("Invalid move, please enter rock, paper or scissors. \n")


    def runGame(self):
        """ to start the game, and through a while loop, keep the game running """
        while True:
            user_input = self.getUserInput()

            if user_input == "quit":
                print("Thanks for Playing!\n")
                print("Final score summary:")
                self.game.getScoreSummary()
                break

            ai_move = self.game.AIMove()
            winner = self.game.determineWinner(ai_move, user_input)
            self.game.updateScore(winner)

            print(f"\nYou chose: {user_input.capitalize()} | AI chose: {ai_move.capitalize()}")
            if winner == "tie":
                print("It's a tie!")
            elif winner == "user":
                print("You win this round!")
            else:
                print("AI wins this round!")

            self.game.getScoreSummary()




if __name__ == "__main__":
    cli = CLIHandler()
    cli.runGame()