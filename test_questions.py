from questions import MultipleChoiceQuestion, TrueFalseQuestion

def test_multiple_choice_correct_answer_returns_true():
    q = MultipleChoiceQuestion(question="What colour is the sky",
                               options=["yellow", "red", "green", "blue"],
                               correct_answer="blue")
    assert q.check_answer("blue") == True

def test_true_false_correct_answer_returns_true():
    q = TrueFalseQuestion(question="Are there 7 days in a week?",
                          correct_answer=True)
    assert q.check_answer("True") == True