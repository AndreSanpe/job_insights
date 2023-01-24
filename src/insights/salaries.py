from typing import Union, List, Dict
import src.insights.jobs as jobs

# from jobs import read


def get_max_salary(path: str) -> int:
    data = jobs.read(path)
    max_salary = 0
    for row in data:
        if (
            row["max_salary"]
            and row["max_salary"] != "invalid"
            and int(row["max_salary"]) > max_salary
        ):
            max_salary = int(row["max_salary"])

    return max_salary


# get_max_salary("data/jobs.csv")


def get_min_salary(path: str) -> int:
    data = jobs.read(path)
    min_salary_list = []

    for row in data:
        if row["min_salary"] and row["max_salary"] != "invalid":
            min_salary_list.append(int(row["min_salary"]))
    min_salary = min(min_salary_list)
    return min_salary


# get_min_salary("data/jobs.csv")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        value_min = int(job["min_salary"])
        value_max = int(job["max_salary"])
        salary_value = int(salary)
    except Exception:
        raise ValueError

    if value_min > value_max:
        raise ValueError
    return value_min <= salary_value <= value_max


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    list_all_salaries = []
    for job in jobs:
        try:
            value_min = int(job["min_salary"])
            value_max = int(job["max_salary"])
            salary_value = int(salary)
            if value_min <= salary_value <= value_max:
                list_all_salaries.append(job)
        except Exception:
            pass

    return list_all_salaries
