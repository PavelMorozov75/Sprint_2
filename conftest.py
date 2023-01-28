import pytest
from main import BooksCollector
@pytest.fixture
def indi_books():
    collector = BooksCollector()
    collector.books_rating['Гордость и предубеждение и зомби'] = 2
    collector.books_rating['Что делать, если ваш кот хочет вас убить'] = 1
    collector.books_rating['Сказки старого Вильнюса'] = 6
    collector.books_rating['Репка'] = 2
    collector.favorites.append('Сказки старого Вильнюса')
    return collector

