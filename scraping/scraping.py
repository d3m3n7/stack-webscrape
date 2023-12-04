import requests
from bs4 import BeautifulSoup, Tag

from entry.entry import Entry


class Scraping:
    @staticmethod
    def get_url():
        return "https://news.ycombinator.com/"

    @staticmethod
    def get_html(*, url) -> str:
        return requests.get(url).content.decode("utf-8")

    @staticmethod
    def get_30_entries(html: str) -> list[Entry]:
        soup = BeautifulSoup(html, features="html.parser")
        outer_table = soup.find(id="hnmain")
        tables = outer_table.find_all(name="table")
        second_table = tables[1]
        table_rows = second_table.find_all(name="tr")
        title_table_rows = (table_rows[::3])[:30]
        likes_table_rows = (table_rows[1::3])[:30]
        entries = list()
        for title, likes in zip(title_table_rows, likes_table_rows):
            entries.append(Scraping.process_entry(title_tr=title, likes_tr=likes))
        return entries

    @staticmethod
    def process_entry(*, title_tr: Tag, likes_tr: Tag) -> Entry:
        return Entry(
            title=Scraping.get_title(title_tr=title_tr),
            order=Scraping.get_order(title_tr=title_tr),
            points=Scraping.get_points(likes_tr=likes_tr),
            n_comments=Scraping.get_n_comments(likes_tr=likes_tr),
        )

    @staticmethod
    def get_title(*, title_tr: Tag) -> str:
        return title_tr.select_one("span.titleline a").text

    @staticmethod
    def get_order(*, title_tr: Tag) -> int:
        span = title_tr.select_one("span.rank")
        return int(span.text[:-1])

    @staticmethod
    def get_n_comments(*, likes_tr: Tag) -> int | None:
        anchors = likes_tr.select("td.subtext span.subline a")
        for anchor in anchors:
            text = anchor.text
            if "comment" in text:
                return int(text.split("\xa0")[0])
        return None

    @staticmethod
    def get_points(*, likes_tr: Tag) -> int | None:
        span = likes_tr.select_one("span.score")
        if span is not None:
            return int(span.text.split(" ")[0])
        return None
