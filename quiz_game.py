from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quiz = Quiz()
        self.state = {}

    def run(self):
        # Main game loop
        while True:
            question = self.quiz.get_next_question()
            if question is None:
                print("No more questions available.")
                break
            print(question)
            answer = input("Your answer: ")
            self.state[question] = answer

    def write_state(self):
        # Write the current state to a file or database
        with open("quiz_state.txt", "w") as f:
            for question, answer in self.state.items():
                f.write(f"{question}: {answer}\n")
