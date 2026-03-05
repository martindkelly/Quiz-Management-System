from questions import MultipleChoiceQuestion, TrueFalseQuestion, TextInputQuestion

def test_multiple_choice_correct_answer_returns_true():
    q = MultipleChoiceQuestion(question="What colour is the sky",
                               options=["yellow", "red", "green", "blue"],
                               correct_answer="blue")
    assert q.check_answer("blue") == True

def test_true_false_correct_answer_returns_true():
    q = TrueFalseQuestion(question="Are there 7 days in a week?",
                          correct_answer=True)
    assert q.check_answer(True) == True

def test_text_input_correct_answer_returns_true():
    q =  TextInputQuestion(question="What's the last month of the year?",
                           correct_answer="December")
    assert q.check_answer("December") == True

def test_text_input_case_insensitivity():
    q =  TextInputQuestion(question="What's the last month of the year?",
                           correct_answer="December")
    assert q.check_answer("december") == True

def test_factory_creating_multiple_choice_question():
    q = QuestionFactory.create(
        question_type="multiple_choice",
        question="What colour is the sky?",
        correct_answer="blue",
        options=["yellow", "red", "green", "blue"]
    )
    assert isinstance(q, MultipleChoiceQuestion)

def test_factory_creating_true_false_question():
    q = QuestionFactory.create(
        question_type="true_false",
        question="Are there 7 days in a week?",
        correct_answer=True
    )
    assert isinstance(q, TrueFalseQuestion)
