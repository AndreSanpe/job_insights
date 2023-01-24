from typing import List, Dict
from jobs import read


def get_unique_industries(path: str) -> List[str]:
    read_data = read(path)
    all_industries = []
    for row in read_data:
        if row["industry"] and row["industry"] not in all_industries:
            all_industries.append(row["industry"])

    return all_industries


get_unique_industries("data/jobs.csv")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
