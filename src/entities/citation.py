from util import string_or_empty_string

# pylint: disable=too-many-instance-attributes, redefined-builtin
#                 maybe fix this later          database uses "id" so can't really do anything

class Article:
    def __init__(self, *, id=None, **a):
        self.id = id
        self.key = a['key']
        self.author = a['author']
        self.title = a['title']
        self.journal = a['journal']
        self.year = a['year']
        self.volume = a.get('volume')
        self.pages = a.get('pages')
        self.number = a.get('number')
        self.month = a.get('month')
        self.note = a.get('note')
        self.annote = a.get('annote')
        self.type_as_string = 'article'

    def __str__(self):
        return f'{self.author}: {self.title} ({self.key})'

    def bibtex(self):
        return (
            f'@{self.type_as_string}{{{self.key},\n'
            f'  author = {{{self.author}}},\n'
            f'  title = {{{self.title}}},\n'
            f'  journal = {{{self.journal}}},\n'
            f'  year = {{{self.year}}},\n'
            f'  volume = {{{string_or_empty_string(self.volume)}}},\n'
            f'  pages = {{{string_or_empty_string(self.pages)}}}\n'
            f'}}'
        )

class Inproceedings:
    def __init__(self, *, id=None, **a):
        self.id = id
        self.key = a['key']
        self.author = a['author']
        self.title = a['title']
        self.year = a['year']
        self.booktitle = a['booktitle']
        self.editor = a.get('editor')
        self.volume = a.get('volume')
        self.number = a.get('number')
        self.series = a.get('series')
        self.pages = a.get('pages')
        self.month = a.get('month')
        self.address = a.get('address')
        self.organization = a.get('organization')
        self.publisher = a.get('publisher')
        self.note = a.get('note')
        self.annote = a.get('annote')
        self.type_as_string = 'inproceedings'

    def __str__(self):
        return f'{self.author}: {self.title} ({self.key})'

    def bibtex(self):
        return (
            f'@{self.type_as_string}{{{self.key},\n'
            f'  author = {{{self.author}}},\n'
            f'  title = {{{self.title}}},\n'
            f'  year = {{{self.year}}},\n'
            f'  booktitle = {{{self.booktitle}}}\n'
            f'}}'
        )

class Book:
    def __init__(self, *, id=None, **a):
        self.id = id
        self.key = a['key']
        self.author = a['author']
        self.title = a['title']
        self.publisher = a['publisher']
        self.year = a['year']
        self.volume = a['volume']
        self.number = a['number']
        self.series = a['series']
        self.address = a['address']
        self.edition = a['edition']
        self.month = a['month']
        self.note = a['note']
        self.annote = a['annote']
        self.type_as_string = 'book'

    def __str__(self):
        return f'{self.author}: {self.title} ({self.key})'

    def bibtex(self):
        return 'not implemented'
