from scraping.scraping import Scraping
from entry.entry import Entry
from bs4 import BeautifulSoup, Tag


class TestScraping:
    @staticmethod
    def test_get_html():
        html = Scraping.get_html(url=Scraping.get_url())
        assert isinstance(html, str)
        assert len(html) > 0

    @staticmethod
    def test_get_title():
        title_tr = TestScraping.__get_title_tr()
        title = Scraping.get_title(title_tr=title_tr)
        assert isinstance(title, str)
        assert title == TestScraping.__get_test_title()

    @staticmethod
    def test_get_order():
        title_tr = TestScraping.__get_title_tr()
        order = Scraping.get_order(title_tr=title_tr)
        assert isinstance(order, int)
        assert order == TestScraping.__get_test_order()

    @staticmethod
    def test_get_n_comments():
        likes_tr = TestScraping.__get_likes_tr()
        n_comments = Scraping.get_n_comments(likes_tr=likes_tr)
        assert isinstance(n_comments, int)
        assert n_comments == TestScraping.__get_test_n_comments()

    @staticmethod
    def test_get_points():
        likes_tr = TestScraping.__get_likes_tr()
        points = Scraping.get_points(likes_tr=likes_tr)
        assert isinstance(points, int)
        assert points == TestScraping.__get_test_points()

    @staticmethod
    def test_process_entry():
        entry = Scraping.process_entry(
            title_tr=TestScraping.__get_title_tr(),
            likes_tr=TestScraping.__get_likes_tr(),
        )
        assert isinstance(entry, Entry)
        assert entry.title == TestScraping.__get_test_title()
        assert entry.order == TestScraping.__get_test_order()
        assert entry.points == TestScraping.__get_test_points()
        assert entry.n_comments == TestScraping.__get_test_n_comments()

    @staticmethod
    def test_get_30_entries():
        html = Scraping.get_html(url=Scraping.get_url())
        entries = Scraping.get_30_entries(html=html)
        assert isinstance(entries, list)
        assert len(entries) == 30
        for entry in entries:
            assert isinstance(entry, Entry)

    @staticmethod
    def __get_title_tr() -> Tag:
        title_html = """
            <tr class="athing" id="38513975">
                        <td align="right" class="title" valign="top"><span class="rank">25.</span></td>
                        <td class="votelinks" valign="top">
                            <center><a href="vote?id=38513975&amp;how=up&amp;goto=news" id="up_38513975">
                                <div class="votearrow" title="upvote"></div>
                            </a></center>
                        </td>
                        <td class="title"><span class="titleline"><a
                                href="https://www.frontiersin.org/articles/10.3389/fcosc.2023.1250996/full"
                                rel="noreferrer">Capturing DNA in snow tracks of polar bear, Eurasian lynx and snow leopard</a><span
                                class="sitebit comhead"> (<a href="from?site=frontiersin.org"><span class="sitestr">frontiersin.org</span></a>)</span></span>
                        </td>
                    </tr>
            """
        soup = BeautifulSoup(title_html, features="html.parser")
        assert isinstance(soup, Tag)
        return soup

    @staticmethod
    def __get_likes_tr() -> Tag:
        title_html = """
          <td colspan="2"></td><td class="subtext"><span class="subline">
          <span class="score" id="score_38517873">67 points</span> by <a href="user?id=EastLondonCoder" class="hnuser">EastLondonCoder</a> <span class="age" title="2023-12-04T14:43:56"><a href="item?id=38517873">3 hours ago</a></span> <span id="unv_38517873"></span> | <a href="hide?id=38517873&amp;goto=news">hide</a> | <a href="item?id=38517873">54&nbsp;comments</a>        </span>
              </td>>
            """
        soup = BeautifulSoup(title_html, features="html.parser")
        assert isinstance(soup, Tag)
        return soup

    @staticmethod
    def __get_test_title() -> str:
        return (
            "Capturing DNA in snow tracks of polar bear, Eurasian lynx and snow leopard"
        )

    @staticmethod
    def __get_test_order() -> int:
        return 25

    @staticmethod
    def __get_test_n_comments() -> int:
        return 54

    @staticmethod
    def __get_test_points() -> int:
        return 67
