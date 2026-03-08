class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        if user_answer == self.correct_answer:
            return True
        else:
            return False
        
class MultipleChoiceQuestion(Question):
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.options = options

class TrueFalseQuestion(Question):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer= correct_answer

class TextInputQuestion(Question):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer.lower()
    
    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer


class QuestionFactory:
    @staticmethod
    def create(question_type, question, correct_answer, options=None):
        if question_type == "multiple_choice":
            return MultipleChoiceQuestion(question, options, correct_answer)
        elif question_type == "true_false":
            return TrueFalseQuestion(question, correct_answer)
        elif question_type == "text_input":
            return TextInputQuestion(question, correct_answer)
        else:
            print("Unknown question type:", question_type)
            return None