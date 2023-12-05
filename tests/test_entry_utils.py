import pandas as pd
from pandas._testing import assert_frame_equal

from entry.entry import Entry
from entry.entry_utils import entries2dataframe


class TestEntryUtils:
    @staticmethod
    def test_entries2dataframe():
        entries = [
            Entry(title="Title 1", order=1, n_comments=None, points=10),
            Entry(title="Title 2", order=2, n_comments=5, points=None),
            Entry(title="Title 3", order=3, n_comments=5, points=10),
        ]
        df = entries2dataframe(entries)
        df_aux = pd.DataFrame(
            {
                "title": ["Title 1", "Title 2", "Title 3"],
                "order": [1, 2, 3],
                "n_comments": [0, 5, 5],
                "points": [10, 0, 10],
            }
        )
        assert_frame_equal(df, df_aux)
