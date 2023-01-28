import pytest

from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('books_for_adding', ['Гордость и предубеждение и зомби',
                                                  'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_two_books(self, books_for_adding):
        books = BooksCollector()
        books.add_new_book(books_for_adding)
        assert list(books.books_rating.keys()) == [books_for_adding]
    def test_add_new_book_rating_by_new_book_is_one(self):
        books = BooksCollector()
        book_for_adding = 'Гордость и предубеждение и зомби'
        books.add_new_book(book_for_adding)
        assert books.books_rating[book_for_adding] == 1
    def test_add_new_book_one_book_add_once(self, indi_books):
        book_number_in_dict = 1
        dict_books_rating_before = indi_books.books_rating
        indi_books.add_new_book(list(indi_books.books_rating.keys())[book_number_in_dict])
        dict_books_rating_after = indi_books.books_rating
        assert dict_books_rating_before == dict_books_rating_after
    def test_set_book_rating_set_valid_rating_for_existing_book(self, indi_books):
        rating_for_set = 3
        book_number_in_dict = 1
        indi_books.set_book_rating(list(indi_books.books_rating.keys())[book_number_in_dict], rating_for_set)
        assert indi_books.books_rating[list(indi_books.books_rating.keys())[book_number_in_dict]] == rating_for_set
    def test_set_book_rating_set_valid_rating_for_not_existing_book(self, indi_books):
        rating_for_invalid_book = 5
        indi_books.set_book_rating('Отсутствующая в словаре книга', rating_for_invalid_book)
        assert not indi_books.books_rating.get('Отсутствующая в словаре книга')
    def test_set_book_rating_set_rating_more_than_10_for_existing_book(self, indi_books):
        invalid_rating_more_than_10 = 11
        book_number_in_dict = 2
        rating_book_number_in_dict_before = indi_books.books_rating[list(indi_books.books_rating.keys())[book_number_in_dict]]
        indi_books.set_book_rating(list(indi_books.books_rating.keys())[book_number_in_dict], invalid_rating_more_than_10)
        rating_book_number_in_dict_after = indi_books.books_rating[list(indi_books.books_rating.keys())[book_number_in_dict]]
        assert rating_book_number_in_dict_before == rating_book_number_in_dict_after
    def test_set_book_rating_set_rating_less_than_1_for_existing_book(self, indi_books):
        invalid_rating_less_than_1 = 0
        book_number_in_dict = 3
        rating_book_number_in_dict_before = indi_books.books_rating[list(indi_books.books_rating.keys())[book_number_in_dict]]
        indi_books.set_book_rating(list(indi_books.books_rating.keys())[book_number_in_dict], invalid_rating_less_than_1)
        rating_book_number_in_dict_after = indi_books.books_rating[list(indi_books.books_rating.keys())[book_number_in_dict]]
        assert rating_book_number_in_dict_before == rating_book_number_in_dict_after
    def test_set_book_rating_rating_is_char(self, indi_books):
        invalid_rating_is_char = 'A'
        book_number_in_dict = 1
        rating_book_number_in_dict_before = indi_books.books_rating[list(indi_books.books_rating.keys())[book_number_in_dict]]
        indi_books.set_book_rating(list(indi_books.books_rating.keys())[book_number_in_dict], invalid_rating_is_char)
        rating_book_number_in_dict_after = indi_books.books_rating[list(indi_books.books_rating.keys())[book_number_in_dict]]
        assert  rating_book_number_in_dict_before == rating_book_number_in_dict_after
    def test_get_book_rating_given_rating_for_book_from_books_rating(self, indi_books):
        book_number_in_dict = 1
        assert indi_books.get_book_rating(list(indi_books.books_rating.keys())[book_number_in_dict]) == \
               indi_books.books_rating[list(indi_books.books_rating.keys())[book_number_in_dict]]
    def test_get_book_rating_not_added_book_has_no_rating(self, indi_books):
        assert not indi_books.get_book_rating('Отсутствующая в словаре книга')
    @pytest.mark.parametrize('more_books', ['Прощай оружие', 'Лолита', 'Пушкинский дом'])
    def test_get_books_with_specific_rating_get_all_books_with_valid_rating_n(self, indi_books, more_books):
        valid_rating = 5
        indi_books.books_rating[more_books] = valid_rating
        assert indi_books.get_books_with_specific_rating(valid_rating) == [more_books]
    def test_get_books_rating_get_correct_dict(self, indi_books):
        assert indi_books.books_rating == indi_books.get_books_rating()
    def test_add_book_in_favorites_add_book_from_books_rating(self, indi_books):
        book_from_books_rating = 'Гордость и предубеждение и зомби'
        indi_books.add_book_in_favorites(book_from_books_rating)
        assert book_from_books_rating in indi_books.favorites
    def test_add_book_in_favorites_add_book_not_from_books_rating(self,indi_books):
        book_not_from_books_rating = 'Книги не из словаря'
        indi_books.add_book_in_favorites(book_not_from_books_rating)
        assert book_not_from_books_rating not in indi_books.favorites
    def test_add_book_in_favorites_add_same_book_in_favorites_twice(self, indi_books):
        indi_books.add_book_in_favorites('Репка')
        favorites_before = indi_books.favorites
        indi_books.add_book_in_favorites('Репка')
        favorites_after = indi_books.favorites
        assert favorites_before == favorites_after
    def test_delete_book_from_favorites_delete_added_book(self, indi_books):
        favorites_before = indi_books.favorites
        book_for_add_and_del = 'Гордость и предубеждение и зомби'
        indi_books.favorites.append(book_for_add_and_del)
        indi_books.delete_book_from_favorites(book_for_add_and_del)
        favorites_after = indi_books.favorites
        assert (book_for_add_and_del not in indi_books.favorites) and (favorites_before == favorites_after)
    @pytest.mark.parametrize('favorite_books', ['Гордость и предубеждение и зомби',
                                                    'Что делать, если ваш кот хочет вас убить'])
    def test_get_list_of_favorites_books_get_all_favorites(self, indi_books, favorite_books):
        indi_books.favorites.append(favorite_books)
        assert indi_books.get_list_of_favorites_books() == indi_books.favorites


