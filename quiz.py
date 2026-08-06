class Quiz:
    def __init__(self):
        self.questions = [
            "What is the capital of France?",
            "What is 2 + 2?",
            "What is the largest ocean on Earth?"
        ]
        self.current_index = 0

    def get_next_question(self):
        if self.current_index < len(self.questions):
            question = self.questions[self.current_index]
            self.current_index += 1
            return question
        else:
            return None