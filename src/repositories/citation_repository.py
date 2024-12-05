from sqlalchemy import text
from config import db
from entities.citation import Article, Inproceedings

def get_citations(sort_by=None):
    articles = db.session.execute(text('SELECT * FROM articles')).fetchall()
    inproceedings = db.session.execute(text('SELECT * FROM inproceedings')).fetchall()


    citations = [Article(*art) for art in articles] + [Inproceedings(*ip) for ip in inproceedings]

    if sort_by is None:
        pass
    elif sort_by == 'year':
        citations.sort(key=lambda x: x.year, reverse=True)
    elif sort_by == 'author':
        citations.sort(key=lambda x: x.author.lower())
    elif sort_by == 'title':
        citations.sort(key=lambda x: x.title.lower())

    return citations

def create_article(info:Article):
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

def create_inproceedings(info:Inproceedings):
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

def delete_citation_by_id(cid, ctype):
    # no sql injections
    if not ctype in ('article', 'inproceedings'):
        return

    # change to plural if needed
    if ctype[-1] != 's':
        ctype += 's'

    sql = text(f'DELETE FROM {ctype} WHERE id = :id')
    db.session.execute(sql, {'id': cid})
    db.session.commit()
