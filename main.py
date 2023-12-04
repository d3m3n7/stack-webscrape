import requests

if __name__ == "__main__":
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    print(response.content)
