import unittest
from unittest.mock import patch, MagicMock
import json
from doi_search import doi_search
from entities.citation import Article, Inproceedings, Book

class TestDOISearch(unittest.TestCase):

    def test_doi_not_found(self):
        result = doi_search('invalid-doi', 'citation_key')
        self.assertEqual(result, 'DOI not found')

    @patch('doi_search.urllib.request.urlopen')
    @patch('doi_search.create_article')
    def test_doi_search_creates_article(self, mock_create_article, mock_urlopen):
        mock_response = {
            'message': {
                'type': 'journal-article',
                'title': ['A Great Article'],
                'published': {'date-parts': [[2021]]},
                'author': [
                    {'given': 'Ains', 'family': 'Tain'},
                    {'given': 'Haw', 'family': 'Kings'}
                ],
                'container-title': ['Great Journal']
            }
        }

        mock_urlopen.return_value.__enter__.return_value = MagicMock()
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response).encode('utf-8')

        doi = '10.1038/nature12373'
        data_key = 'citation_key'
        result = doi_search(doi, data_key)

        self.assertEqual(result, 'OK')

        mock_create_article.assert_called_once()
        article_args = mock_create_article.call_args[0][0]
        self.assertIsInstance(article_args, Article)
        self.assertEqual(article_args.key, data_key)
        self.assertEqual(article_args.author, 'Ains Tain, Haw Kings')
        self.assertEqual(article_args.title, 'A Great Article')
        self.assertEqual(article_args.journal, 'Great Journal')
        self.assertEqual(article_args.year, 2021)

    @patch('doi_search.urllib.request.urlopen')
    @patch('doi_search.create_inproceedings')
    def test_doi_search_creates_inproceedings(self, mock_create_inproceedings, mock_urlopen):
        mock_response = {
            'message': {
                'type': 'proceedings-article',
                'title': ['A Great Paper'],
                'published': {'date-parts': [[2022]]},
                'author': [
                    {'given': 'Jason', 'family': 'Jason'},
                    {'given': 'Jack', 'family': 'Jack'}
                ],
                'container-title': ['Great Conference']
            }
        }

        mock_urlopen.return_value.__enter__.return_value = MagicMock()
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response).encode('utf-8')

        doi = '10.1109/GreatConference.2022.1234567'
        data_key = 'inproceedings_key'
        result = doi_search(doi, data_key)

        self.assertEqual(result, 'OK')

        mock_create_inproceedings.assert_called_once()
        inproceedings_args = mock_create_inproceedings.call_args[0][0]
        self.assertIsInstance(inproceedings_args, Inproceedings)
        self.assertEqual(inproceedings_args.key, data_key)
        self.assertEqual(inproceedings_args.author, 'Jason Jason, Jack Jack')
        self.assertEqual(inproceedings_args.title, 'A Great Paper')
        self.assertEqual(inproceedings_args.year, 2022)
        self.assertEqual(inproceedings_args.booktitle, 'Great Conference')

    @patch('doi_search.urllib.request.urlopen')
    @patch('doi_search.create_book')
    def test_doi_search_creates_book(self, mock_create_book, mock_urlopen):
        mock_response = {
            'message': {
                'type': 'book',
                'title': ['Harry Potter'],
                'published': {'date-parts': [[2023]]},
                'author': [
                    {'given': 'asdf', 'family': 'McAsdf'}
                ],
                'publisher': 'Great Publisher'
            }
        }

        mock_urlopen.return_value.__enter__.return_value = MagicMock()
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response).encode('utf-8')

        doi = '10.1234/GreatBook.2023.123456'
        data_key = 'book_key'
        result = doi_search(doi, data_key)

        self.assertEqual(result, 'OK')

        mock_create_book.assert_called_once()
        book_args = mock_create_book.call_args[0][0]
        self.assertIsInstance(book_args, Book)
        self.assertEqual(book_args.key, data_key)
        self.assertEqual(book_args.author, 'asdf McAsdf')
        self.assertEqual(book_args.title, 'Harry Potter')
        self.assertEqual(book_args.publisher, 'Great Publisher')
        self.assertEqual(book_args.year, 2023)
