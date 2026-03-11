from questions import MultipleChoiceQuestion, QuestionFactory, TextInputQuestion, TrueFalseQuestion
from scores import Scores


class Quiz:

    def __init__(self):
        self.questions = []
        self.scores = Scores()

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        print("Quiz starting!\n")

        for i in range(len(self.questions)):
            q = self.questions[i]
            print(f"Question {i + 1}: {q.question}")

            if isinstance(q, MultipleChoiceQuestion):
                for j in range(len(q.options)):
                    print(str(j + 1) + ".", q.options[j])
                answer = input("Your answer: ")

            elif isinstance(q, TrueFalseQuestion):
                user_input = input("True or False: ").strip().lower()
                if user_input == "true":
                    answer = True
                else:
                    answer = False

            else:
                answer = input("Your answer: ")

            if q.check_answer(answer):
                print("Correct!\n")
                self.scores.inc_score()
            else:
                print("Wrong, the answer was:", q.correct_answer, "\n")
                self.scores.inc_wrong()

        print("Finished!")
        print("You got", self.scores.get_correct(), "out of", self.scores.get_total())
        print("Percentage:", self.scores.get_percentage(), "%")


if __name__ == "__main__":
    quiz = Quiz()

    quiz.add_question(
        QuestionFactory.create(
            "multiple_choice", "What colour is the sky?", 
            "blue", 
            ["yellow", "red", "green", "blue"]))
    quiz.add_question(
        QuestionFactory.create(
            "true_false", 
            "Are there 7 days in a week?", 
            True))
    quiz.add_question(
        QuestionFactory.create(
            "text_input", 
            "What is the last month of the year?", 
            "December"))

    quiz.run()