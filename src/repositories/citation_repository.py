from sqlalchemy import text
from config import db
from entities.citation import Article, Inproceedings, Book

def get_citations():
    articles = db.session.execute(text('SELECT * FROM articles')).mappings().fetchall()
    inproceedings = db.session.execute(text('SELECT * FROM inproceedings')).mappings().fetchall()
    books = db.session.execute(text('SELECT * FROM books')).mappings().fetchall()

    return (
        [Article(**art) for art in articles] +
        [Inproceedings(**ip) for ip in inproceedings] +
        [Book(**bk) for bk in books]
    )

def create_article(info: Article):
    sql = text('''INSERT INTO articles (key, author, title, journal, year, volume, pages)
             VALUES (:key, :author, :title, :journal, :year, :volume, :pages)''')

    db.session.execute(sql, {
        'key': info.key,
        'author': info.author,
        'title': info.title,
        'journal': info.journal,
        'year': info.year,
        'volume': info.volume,
        'pages': info.pages
    })
    db.session.commit()

def create_inproceedings(info: Inproceedings):
    sql = text('''INSERT INTO inproceedings (key, author, title, year, booktitle)
             VALUES (:key, :author, :title, :year, :booktitle)''')

    db.session.execute(sql, {
        'key': info.key,
        'author': info.author,
        'title': info.title,
        'year': info.year,
        'booktitle': info.booktitle
    })
    db.session.commit()

def create_book(info: Book):
    sql = text('''INSERT INTO books (key, author, title, publisher, year)
             VALUES (:key, :author, :title, :publisher, :year)''')

    db.session.execute(sql, {
        'key': info.key,
        'author': info.author,
        'title': info.title,
        'publisher': info.publisher,
        'year': info.year
    })
    db.session.commit()

def delete_citation_by_id(cid, ctype):
    # no sql injections
    if not ctype in ('article', 'inproceedings', 'book'):
        return

    # change to plural if needed
    if ctype[-1] != 's':
        ctype += 's'

    sql = text(f'DELETE FROM {ctype} WHERE id = :id')
    db.session.execute(sql, {'id': cid})
    db.session.commit()

def sort_citations(sort_by):

    fields = ['year', 'author', 'title']

    if sort_by not in fields:
        sort_by = 'year'  

    sql = text(f'SELECT * FROM articles ORDER BY {sort_by}')
    articles = db.session.execute(sql).mappings().fetchall()

    sql = text(f'SELECT * FROM inproceedings ORDER BY {sort_by}')
    inproceedings = db.session.execute(sql).mappings().fetchall()

    sql = text(f'SELECT * FROM books ORDER BY {sort_by}')
    books = db.session.execute(sql).mappings().fetchall()

    return (
        [Article(**art) for art in articles] +
        [Inproceedings(**ip) for ip in inproceedings] +
        [Book(**bk) for bk in books]
    )
