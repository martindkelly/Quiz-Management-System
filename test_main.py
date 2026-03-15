from main import get_available_quizzes

def test_get_available_quizzes_returns_correctly():
    quizzes = get_available_quizzes("quizzes/")
    assert len(quizzes) > 0