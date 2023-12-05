import pandas as pd

from entry.entry import Entry


def entries2dataframe(entries: list[Entry]) -> pd.DataFrame:
    entry_dicts = [entry.to_dict() for entry in entries]
    dataframes = [
        pd.DataFrame(entry_dict, index=[i]) for i, entry_dict in enumerate(entry_dicts)
    ]
    df = pd.concat(dataframes)
    return df
