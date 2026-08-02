import random
import time

class TextProvider:
    """ 
        This is the class that generates the prompt and stores candidate prompts
    """
    def __init__(self):
        self.prompts_sentences = [
            "The quick brown fox jumps over the lazy dog",
            "Another sentence for the purpose of this test"
        ]
        self.prompts_paragraphs = [
            """This is a multi-line paragraph.
You can break lines naturally using triple quotes,
and Python will preserve the text cleanly!""",
            """Another long paragraph goes here.
It makes reading and editing long texts in your code
much easier!"""
        ]


    def sentencePromptGenerator(self):
        return random.choice(self.prompts_sentences)


    def paragraphPromptGenerator(self):
        return random.choice(self.prompts_paragraphs)





class TypingEngine:
    """ 
        This is the class that manages the timer, calculation of wpm and calculation of accuracy
    """
    def __init__(self):
        self.start_time = 0
        self.end_time = 0


    def startTimer(self ):
        self.start_time = time.time()


    def stopTimer(self):
        self.end_time = time.time()
        return (self.end_time - self.start_time) / 60


    def wpmCalculator(self, input, time_min):
        if time_min <= 0:
            return 0.0 
        
        x = input.strip()
        total_char = len(x)
        char = total_char / 5

        wpm = char / time_min
        return round(wpm, 2)


    def accuracyCalculation(self, prompt, input):
        if not prompt:
            return 0.0

        total_char = len(prompt)
        zipped = zip(prompt, input)
        correct_char = sum(1 for p, u in zipped if p == u)
        
        accuracy = (correct_char / total_char) * 100
        return round(accuracy, 2)


    def scoreSummary(self, prompt, input, time):
        wpm = self.wpmCalculator(input, time)
        acc = self.accuracyCalculation(prompt, input)
        net_wpm = round(wpm * (acc / 100), 2)

        return {
            "time": round(time*60, 2),
            "wpm": wpm,
            "acc": acc,
            "net_wpm": net_wpm
        }





class CLIHandler:
    """
        Handles user input and runs a round of the test
    """
    def __init__(self):
        self.text = TextProvider()
        self.test = TypingEngine()


    def runRound(self):
        print("\n")
        print("===WELCOME TO THE SPEED TYPING TEST===")
        print("1. Single sentence")
        print("2. Single paragraph")
        print("3. Exit")

        option = input("Choose one of the three options (1-3): ")

        if option == '3':
            print("\nThank you for playing")
            return False

        if option == '1':
            prompt = self.text.sentencePromptGenerator()
        elif option == '2':
            prompt = self.text.paragraphPromptGenerator()
        else:
            print("Invalid option, please select from (1-3)\n")
            return True

        print("Type out the following prompt:")
        print(prompt)

        input("\nPress enter when you are ready to start!")
        self.test.startTimer()

        user_input = input("\nType here: ")
        time_min = self.test.stopTimer()

        stats = self.test.scoreSummary(prompt, user_input, time_min)

        print("\n")
        print("SUMMARY OF TEST")
        print(f"Elapsed Time: {stats['time']} seconds")
        print("Words per minute: ", stats["wpm"])
        print(f"Accuracy: {stats['acc']}%")
        print("Net words per minute: ", stats["net_wpm"])
        print("\n")
        return True


    def mainLoop(self):
        running = True

        while running:
            running = self.runRound()
        




if __name__ == "__main__":
    cli = CLIHandler()
    cli.mainLoop()