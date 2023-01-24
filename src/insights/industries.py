from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    read_data = read(path)
    all_industries = []
    for row in read_data:
        if row["industry"] and row["industry"] not in all_industries:
            all_industries.append(row["industry"])

    return all_industries


get_unique_industries("data/jobs.csv")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    data = read(jobs)
    filtered_by_industry = []
    for row in data:
        if row["industry"] == industry:
            filtered_by_industry.append(row)

        return filtered_by_industry


# filter_by_industry("data/jobs.csv", 'Restaurants, Bars & Food Services')
