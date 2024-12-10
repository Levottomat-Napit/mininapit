from util import generate_bibtex

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
        return generate_bibtex(self)

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
        return generate_bibtex(self)

class Book:
    def __init__(self, *, id=None, **a):
        self.id = id
        self.key = a['key']
        self.author = a['author']
        self.title = a['title']
        self.publisher = a['publisher']
        self.year = a['year']
        self.volume = a.get('volume')
        self.number = a.get('number')
        self.series = a.get('series')
        self.address = a.get('address')
        self.edition = a.get('edition')
        self.month = a.get('month')
        self.note = a.get('note')
        self.annote = a.get('annote')
        self.type_as_string = 'book'

    def __str__(self):
        return f'{self.author}: {self.title} ({self.key})'

    def bibtex(self):
        return generate_bibtex(self)
