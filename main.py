from scraping.scraping import Scraping

if __name__ == "__main__":
    html = Scraping.get_html(url=Scraping.get_url())
    entries = Scraping.get_30_entries(html=html)
    print(entries)
