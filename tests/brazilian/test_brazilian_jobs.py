from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    portuguese_file_path = "tests/mocks/brazilians_jobs.csv"
    english_result = read_brazilian_file(portuguese_file_path)

    assert "title" in english_result[0].keys()
    assert "salario" not in english_result[0].keys()
