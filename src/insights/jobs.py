from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    # https://www.delftstack.com/pt/howto/python/python-csv-to-dictionary/
    # final_file = []
    with open(path) as file:
        reader = list(csv.DictReader(file))
        return reader


# read("data/jobs.csv")


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    full_list_job_types = []
    for row in data:
        if row["job_type"] and row["job_type"] not in full_list_job_types:
            full_list_job_types.append(row["job_type"])
    return full_list_job_types


# get_unique_job_types("data/jobs.csv")


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
