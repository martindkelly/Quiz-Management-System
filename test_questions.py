from questions import MultipleChoiceQuestion

def test_correct_answer_returns_true():
    q = MultipleChoiceQuestion(question="What colour is the sky",
                               options=["yellow", "red", "green", "blue"],
                               correct_answer="blue")
    assert q.check_answer("blue") == True