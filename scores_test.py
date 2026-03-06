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