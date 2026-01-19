# filters.py

import pandas as pd
from taxonomy import PRACTICE_TO_MAIN

def filter_by_category(df: pd.DataFrame, main_category: str) -> pd.DataFrame:
    """
    Returns rows where ANY practice area maps to the selected main category.
    """

    def matches(practice_areas: str) -> bool:
        if pd.isna(practice_areas):
            return False

        areas = [a.strip().lower() for a in practice_areas.split(",")]

        for area in areas:
            if PRACTICE_TO_MAIN.get(area) == main_category:
                return True
        return False

    return df[df["PracticeAreas"].apply(matches)].copy()


# filters.py (ADD BELOW EXISTING CODE)

def find_unmapped_practice_areas(df: pd.DataFrame) -> set:
    """
    Returns a set of practice areas that do NOT exist in the taxonomy.
    """
    unmapped = set()

    for val in df["PracticeAreas"].dropna():
        for area in val.split(","):
            normalized = area.strip().lower()
            if normalized and normalized not in PRACTICE_TO_MAIN:
                unmapped.add(area.strip())

    return unmapped
