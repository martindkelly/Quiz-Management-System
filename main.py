import os
from quiz_loader import load_quiz
from quiz import Quiz

def get_available_quizzes(folder):
    files = os.listdir("quizzes/")
    return [f for f in files if f.endswith(".json")]

def main():
    folder = "quizzes/"
    quizzes = get_available_quizzes(folder)

    print("Available quizzes:")
    for i, quiz in enumerate(quizzes):
        print(f"{i+1}. {quiz.replace('.json', '')}")

    choice = int(input("\nSelect a quiz (enter number): ")) -1
    chosen = quizzes[choice]

    questions = load_quiz(folder + chosen)
    quiz = Quiz()
    for q in questions:
        quiz.add_question(q)
    quiz.run()

if __name__ == "__main__":
    main()