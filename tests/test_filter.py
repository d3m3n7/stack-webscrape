from entry.entry import Entry
from entry.entry_utils import entries2dataframe
from filter.filter import filter_more_than_five, filter_less_than_five
import pandas as pd


class TestFilter:
    @staticmethod
    def test_filter_more_than_five():
        df = TestFilter.__get_test_dataframe()
        filtered_and_sorted_df = filter_more_than_five(df)
        expected_result = df.loc[[4, 3]]
        pd.testing.assert_frame_equal(filtered_and_sorted_df, expected_result)

    @staticmethod
    def test_filter_less_than_five():
        df = TestFilter.__get_test_dataframe()
        filtered_and_sorted_df = filter_less_than_five(df)
        expected_result = df.loc[[1, 2]]
        pd.testing.assert_frame_equal(filtered_and_sorted_df, expected_result)

    @staticmethod
    def __get_test_dataframe() -> pd.DataFrame:
        entries = [
            Entry(title="This is a long title", order=1, n_comments=1, points=5),
            Entry(title="Short title", order=2, n_comments=2, points=4),
            Entry(title="Another short title", order=3, n_comments=3, points=3),
            Entry(
                title="Title with more than five words", order=4, n_comments=4, points=2
            ),
            Entry(
                title="Another long title with more words",
                order=5,
                n_comments=5,
                points=1,
            ),
        ]
        return entries2dataframe(entries)
