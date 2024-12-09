import unittest
from entities.citation import Article

class TestBibtexGeneration(unittest.TestCase):
    def test_generate_bibtex_returns_correctly_formatted_article(self):
        article1 = Article(
            key='article1',
            author='John Doe',
            title='Example Article',
            journal='Example Journal',
            year=2022,
            volume=1,
            pages='1-10'
        )
        article2 = Article(
            key='article2',
            author='Jane Doe',
            title='Another Example Article',
            journal='Another Example Journal',
            year=2023,
            volume=2,
            pages='11-20'
        )
        citations = [article1, article2]
        expected_bibtex = [
            '@article{article1,\n'
            '  author = {John Doe},\n'
            '  title = {Example Article},\n'
            '  journal = {Example Journal},\n'
            '  year = {2022},\n'
            '  volume = {1},\n'
            '  pages = {1-10}\n'
            '}',
            '@article{article2,\n'
            '  author = {Jane Doe},\n'
            '  title = {Another Example Article},\n'
            '  journal = {Another Example Journal},\n'
            '  year = {2023},\n'
            '  volume = {2},\n'
            '  pages = {11-20}\n'
            '}'
        ]

        bibtex_citations = [art.bibtex() for art in citations]
        self.assertEqual(bibtex_citations, expected_bibtex)
