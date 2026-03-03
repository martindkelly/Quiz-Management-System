class Question:
    def __init__(self, question, correctAnswer):
        self.question = question
        self.correctAnswer = correctAnswer

    def checkAnswer(self, userAnswer):
        if userAnswer == self.correctAnswer:
            return True
        else:
            return False


