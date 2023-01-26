from src.pre_built.sorting import sort_by
import src.insights.jobs as jobs


def test_sort_by_criteria():
    job_list = jobs.read("data/jobs.csv")
    sort_by(job_list, "min_salary")
    print(job_list[1]["min_salary"])
    print(job_list[4]["min_salary"])

    assert int(job_list[3]["min_salary"]) >= int(job_list[4]["min_salary"])
