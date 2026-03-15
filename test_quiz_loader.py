from quiz_loader import load_quiz

def test_load_quiz_returns_all_questions():
    questions = load_quiz("quizzes/maths.json")
    assert len(questions) == 10