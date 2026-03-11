from quiz import Quiz
from questions import QuestionFactory
from unittest.mock import patch


# check quiz has no questions at the start
def test_quiz_starts_empty():
    quiz = Quiz()
    assert len(quiz.questions) == 0


# check adding one question works
def test_add_question():
    quiz = Quiz()
    q = QuestionFactory.create("true_false", "Is the sky blue?", True)
    quiz.add_question(q)
    assert len(quiz.questions) == 1


# check adding two questions works
def test_add_multiple_questions():
    quiz = Quiz()
    q1 = QuestionFactory.create("true_false", "Is the sky blue?", True)
    q2 = QuestionFactory.create("text_input", "What is the last month of the year?", "December")
    quiz.add_question(q1)
    quiz.add_question(q2)
    assert len(quiz.questions) == 2


# score should be zero before any questions answered
def test_score_starts_zero():
    quiz = Quiz()
    assert quiz.scores.get_correct() == 0
    assert quiz.scores.get_total() == 0


# correct answer should increase score
@patch("builtins.input", return_value="blue")
def test_correct_answer_increases_score(mock_input):
    quiz = Quiz()
    q = QuestionFactory.create("multiple_choice", "What colour is the sky?", "blue", ["yellow", "red", "green", "blue"])
    quiz.add_question(q)
    quiz.run()
    assert quiz.scores.get_correct() == 1
    assert quiz.scores.get_total() == 1


# wrong answer should not increase correct count
@patch("builtins.input", return_value="red")
def test_wrong_answer_increases_total_only(mock_input):
    quiz = Quiz()
    q = QuestionFactory.create("multiple_choice", "What colour is the sky?", "blue", ["yellow", "red", "green", "blue"])
    quiz.add_question(q)
    quiz.run()
    assert quiz.scores.get_correct() == 0
    assert quiz.scores.get_total() == 1


# true false - right answer
@patch("builtins.input", return_value="true")
def test_true_false_correct(mock_input):
    quiz = Quiz()
    q = QuestionFactory.create("true_false", "Are there 7 days in a week?", True)
    quiz.add_question(q)
    quiz.run()
    assert quiz.scores.get_correct() == 1


# true false - wrong answer
@patch("builtins.input", return_value="false")
def test_true_false_wrong(mock_input):
    quiz = Quiz()
    q = QuestionFactory.create("true_false", "Are there 7 days in a week?", True)
    quiz.add_question(q)
    quiz.run()
    assert quiz.scores.get_correct() == 0
    assert quiz.scores.get_total() == 1


# text input - right answer
@patch("builtins.input", return_value="December")
def test_text_input_correct(mock_input):
    quiz = Quiz()
    q = QuestionFactory.create("text_input", "What is the last month of the year?", "December")
    quiz.add_question(q)
    quiz.run()
    assert quiz.scores.get_correct() == 1


# text input should work even if lowercase
@patch("builtins.input", return_value="december")
def test_text_input_case_insensitive(mock_input):
    quiz = Quiz()
    q = QuestionFactory.create("text_input", "What is the last month of the year?", "December")
    quiz.add_question(q)
    quiz.run()
    assert quiz.scores.get_correct() == 1


# run a full quiz and get everything right
@patch("builtins.input", side_effect=["blue", "true", "December"])
def test_full_quiz_all_correct(mock_input):
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
    assert quiz.scores.get_correct() == 3
    assert quiz.scores.get_total() == 3
    assert quiz.scores.get_percentage() == 100.0


# run a full quiz and get some wrong
@patch("builtins.input", side_effect=["red", "false", "December"])
def test_full_quiz_some_wrong(mock_input):
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
    assert quiz.scores.get_correct() == 1
    assert quiz.scores.get_total() == 3
    assert quiz.scores.get_percentage() == 33.3