from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "Python"
    word_2 = "Javascript"
    result = count_ocurrences(path, word)
    result_2 = count_ocurrences(path, word_2)
    assert result == 1639
    assert result_2 == 122
