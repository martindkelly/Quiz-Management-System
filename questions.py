class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        if user_answer == self.correct_answer:
            return True
        else:
            return False