from collections import Counter
import bs4
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    table_rows = soup.find('div', class_='middle_info_noborder').find('table').find_all('tr')
    result = []
    for tr in table_rows:
        entry = list(tr.children)[2]
        result.append(str(entry)[4:-5])
    return result


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
    count = []
    for e in emails:
        e_parts = e.split("@")
        if e_parts[1] not in common_domains:
            count.append(e_parts[1])
    counter = Counter(count)
    return counter.most_common()

    # your code
if __name__ == "__main__":
    emails=["a@gmail.com", "b@pybit.es", "c@pybit.es", "d@domain.de"]
    print(get_most_common_domains(emails))
