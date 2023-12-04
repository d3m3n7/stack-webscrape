from scraping.scraping import Scraping


class TestScraping:
    @staticmethod
    def test_get_html():
        html = Scraping.get_html(url=Scraping.get_url())
        assert isinstance(html, str)
        assert len(html) > 0
