from collections.abc import Callable

import pandas as pd


def filter_title_and_sort(
    *, df: pd.DataFrame, filter_title_length: Callable[[str], bool], order_by: str
) -> pd.DataFrame:
    filtered_df = df[df["title"].apply(filter_title_length)]
    return filtered_df.sort_values(by=order_by, ascending=False)


def filter_by_title_length(
    *, title: str, comparator: Callable[[int, int], bool], length: int
) -> bool:
    title_length = len(title.split())
    return comparator(title_length, length)


def filter_more_than_five(df: pd.DataFrame) -> pd.DataFrame:
    order_by = "n_comments"
    return filter_title_and_sort(
        df=df,
        filter_title_length=lambda x: filter_by_title_length(
            title=x, comparator=lambda a, b: a > b, length=5
        ),
        order_by=order_by,
    )


def filter_less_than_five(df: pd.DataFrame) -> pd.DataFrame:
    order_by = "points"
    return filter_title_and_sort(
        df=df,
        filter_title_length=lambda x: filter_by_title_length(
            title=x, comparator=lambda a, b: a < b, length=5
        ),
        order_by=order_by,
    )
