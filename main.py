from scraping.scraping import Scraping
from filter.filter import filter_less_than_five, filter_more_than_five
from entry.entry_utils import entries2dataframe
import pandas as pd

if __name__ == "__main__":
    html = Scraping.get_html(url=Scraping.get_url())
    entries = Scraping.get_30_entries(html=html)
    df = entries2dataframe(entries)

    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)

    print("Original Dataframe")
    print(df)

    df_less_than_five = filter_less_than_five(df=df)
    print(
        "Dataframe with less than five words in the title ordered by the number of points first"
    )
    print(df_less_than_five)

    df_more_than_five = filter_more_than_five(df=df)
    print(
        "Dataframe with more than five words in the title ordered by the number of comments first"
    )
    print(df_more_than_five)
