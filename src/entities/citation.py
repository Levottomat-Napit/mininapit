from util import normal_citation_str, generate_bibtex

# pylint: disable=too-many-instance-attributes, redefined-builtin
#                 ^                             ^
#                 fix this in the future,       database uses "id",
#                 or then not :)                can't really do anything rn

class Article:
    def __init__(self, *, id=None, **fields):
        self.id = id
        self.key = fields['key']
        self.author = fields['author']
        self.title = fields['title']
        self.journal = fields['journal']
        self.year = fields['year']
        self.volume = fields.get('volume')
        self.pages = fields.get('pages')
        self.number = fields.get('number')
        self.month = fields.get('month')
        self.note = fields.get('note')
        self.annote = fields.get('annote')
        self.type_as_string = 'article'

    def __str__(self):
        return normal_citation_str(self)

    def bibtex(self):
        return generate_bibtex(self)

class Inproceedings:
    def __init__(self, *, id=None, **fields):
        self.id = id
        self.key = fields['key']
        self.author = fields['author']
        self.title = fields['title']
        self.year = fields['year']
        self.booktitle = fields['booktitle']
        self.editor = fields.get('editor')
        self.volume = fields.get('volume')
        self.number = fields.get('number')
        self.series = fields.get('series')
        self.pages = fields.get('pages')
        self.month = fields.get('month')
        self.address = fields.get('address')
        self.organization = fields.get('organization')
        self.publisher = fields.get('publisher')
        self.note = fields.get('note')
        self.annote = fields.get('annote')
        self.type_as_string = 'inproceedings'

    def __str__(self):
        return normal_citation_str(self)

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
        return normal_citation_str(self)

    def bibtex(self):
        return generate_bibtex(self)
