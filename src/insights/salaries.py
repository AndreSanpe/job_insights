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


# Returns
# -------
# bool
#     True if the salary is in the salary range of the job, False otherwise

# Raises
# ------
# ValueError
#     If `job["min_salary"]` or `job["max_salary"]` doesn't exists
#     If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
#     If `job["min_salary"]` is greather than `job["max_salary"]`
#     If `salary` isn't a valid integer
# """


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """


# raise NotImplementedError
