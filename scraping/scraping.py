import requests


class Scraping:
    @staticmethod
    def get_url():
        return "https://news.ycombinator.com/"

    @staticmethod
    def get_html(*, url) -> str:
        return requests.get(url).content.decode("utf-8")
