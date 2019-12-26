from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    book_title = soup.find(class_='dotd-title').h2.get_text().strip()
    
    book_summary = soup.find(class_='dotd-main-book-summary').contents[7].get_text().strip()

    link = soup.find(class_='dotd-main-book-image').a['href']
    image = soup.find(class_='bookimage')['src']

    book = Book(title=book_title, 
                description=book_summary, 
                image=image, 
                link=link)

    return book

if __name__ == '__main__':
    print(get_book())
