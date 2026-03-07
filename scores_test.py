from scores import Scores


def test_initial_score():
    s = Scores()
    assert s.get_correct() == 0
    assert s.get_total() == 0

def test_inc_score_increases_correct():
    s = Scores()
    s.inc_score()

    assert s.get_correct() == 1
    assert s.get_total() == 1

def test_wrong_answer_increases_total():
    s = Scores()
    s.inc_wrong()

    assert s.get_total() == 1
    assert s.get_correct() == 0

def test_percentage_calculation():
    s = Scores()
    s.inc_score()  # 1 correct
    s.inc_wrong()  # 1 wrong
    s.inc_wrong()  # 2 wrong

    assert s.get_percentage() == 33.3

def test_percentage_div_by_zero():
    s = Scores()
    assert s.get_percentage() == 0.0

def test_percentage_all_correct():
    s = Scores()
    s.inc_score()  # 1 correct
    s.inc_score()  # 2 correct

    assert s.get_percentage() == 100.0

def test_percentage_all_wrong():
    s = Scores()
    s.inc_wrong()  # 1 wrong
    s.inc_wrong()  # 2 wrong

    assert s.get_percentage() == 0.0

def test_really_long_quiz():
    s = Scores()
    for _ in range(10000):
        s.inc_score()
    assert s.get_correct() == 10000
    assert s.get_total() == 10000

def test_realistic_quiz():
    s = Scores()
    
    s.inc_score()  # 1 correct
    s.inc_wrong()  # 1 wrong
    s.inc_score()  # 2 correct 
    s.inc_score()  # 3 correct
    s.inc_wrong()  # 2 wrong
    s.inc_wrong()  # 3 wrong
    s.inc_score()  # 4 correct
    s.inc_score()  # 5 correct
    s.inc_score()  # 6 correct

    assert s.get_correct() == 6
    assert s.get_total() == 9
    assert s.get_percentage() == 66.7

def test_multiple_users():
    s1 = Scores()
    s2 = Scores()

    s1.inc_score()  # User 1: 1 correct
    s2.inc_wrong()  # User 2: 1 wrong
    s1.inc_wrong()  # User 1: 1 wrong
    s2.inc_wrong()  # User 2: 1 wrong
    s1.inc_score()  # User 1: 2 correct
    s2.inc_wrong()  # User 2: 2 wrong

    assert s1.get_correct() == 2
    assert s1.get_total() == 3
    assert s1.get_percentage() == 66.7

    assert s2.get_correct() == 0
    assert s2.get_total() == 3
    assert s2.get_percentage() == 0.0

def run_tests():
    test_initial_score()
    test_inc_score_increases_correct()
    test_wrong_answer_increases_total()
    test_percentage_calculation()
    test_percentage_div_by_zero()
    test_percentage_all_correct()
    test_percentage_all_wrong()
    test_really_long_quiz()
    test_realistic_quiz()
    test_multiple_users()

run_tests()