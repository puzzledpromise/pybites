from collections import Counter

import bs4
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    raw_site_page = requests.get(url)
    raw_site_page.raise_for_status()
    soup = bs4.BeautifulSoup(raw_site_page.text, "html.parser")
    target = soup.find("div", class_=TARGET_DIV["class"])
    elements = target.find_all("td")
    result = list()
    for e in elements:
        if "%" in e.text:
            continue
        if "<img src" in e.text:
            continue
        if e.text.isdigit():
            continue
        if not e.text.strip():
            continue
        result.append(e.text)
    return result


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
    filter_list = list()
    for email in emails:
        name, domain = email.split("@")
        if domain not in common_domains:
            filter_list.append(domain)
    counter = Counter(filter_list)
    return counter.most_common()




if __name__ == "__main__":
    emails = ["volkmar.petschnig@gmail.com", "volkmar.petschnig@verbund.com"]
    print(get_most_common_domains(emails))
