import requests
from bs4 import BeautifulSoup


def download(url):
    """
    Reads data from a URL and returns the data as a string
    :param url:
    :return:
    """
    # read the URL
    # pip install requests

    # return the data
    return requests.get(url).text


if __name__ == "__main__":
    wiki_url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
    url_text = download(wiki_url)

    # Create a BeatifulSoup object
    soup = BeautifulSoup(url_text, features="lxml")

    result_table = soup.find_all('table', class_="wikitable sortable")
    rows = result_table[0].find_all('tr')
    headers = rows[0].find_all('th')
    print(
        f"{headers[0].text.strip():<15} - {headers[1].text.strip():<40} - {headers[2].text.strip():<20} - {headers[3].text.strip():<15} - {headers[4].text.strip():<15}"
    )
    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        print(
            f"{cells[0].text.strip():<15} - {cells[1].text.strip():<15} - {cells[2].text.strip():<15} - {cells[3].text.strip():<15} - {cells[4].text.strip():<15}"
        )