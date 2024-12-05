from sqlalchemy import text
from config import db, app

TABLES = ['articles', 'inproceedings', 'books']

def table_exists(name):
    sql_table_existence = text(
      'SELECT EXISTS ('
      '  SELECT 1'
      '  FROM information_schema.tables'
      f' WHERE table_name = \'{name}\''
      ')'
    )

    print(f'Checking if table {name} exists')

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]

def reset_db():
    for table in TABLES:
        print(f'Clearing contents from table {table}')
        sql = text(f'DELETE FROM {table}')
        db.session.execute(sql)
        db.session.commit()

def setup_db():
    for table in TABLES:
        if table_exists(table):
            print(f'Table {table} exists, dropping')
            sql = text(f'DROP TABLE {table}')
            db.session.execute(sql)
            db.session.commit()

    print('Creating table articles')
    sql = text(
    'CREATE TABLE articles ('
    '  id SERIAL PRIMARY KEY,'
    '  key TEXT UNIQUE NOT NULL,'
    '  author TEXT NOT NULL,'
    '  title TEXT NOT NULL,'
    '  journal TEXT NOT NULL,'
    '  year INT NOT NULL,'
    '  volume TEXT,'
    '  pages TEXT,'
    '  number TEXT,' # deliberately TEXT
    '  month TEXT,'
    '  note TEXT,'
    '  annote TEXT'
    ')'
    )

    db.session.execute(sql)
    db.session.commit()

    print('Creating table inproceedings')
    sql = text(
    'CREATE TABLE inproceedings ('
    '  id SERIAL PRIMARY KEY,'
    '  key TEXT UNIQUE NOT NULL,'
    '  author TEXT NOT NULL,'
    '  title TEXT NOT NULL,'
    '  year INT NOT NULL,'
    '  booktitle TEXT NOT NULL,'
    '  editor TEXT,'
    '  volume TEXT,'
    '  number TEXT,' # deliberately TEXT
    '  series TEXT,'
    '  pages TEXT,'
    '  month TEXT,'
    '  address TEXT,'
    '  organization TEXT,'
    '  publisher TEXT,'
    '  note TEXT,'
    '  annote TEXT'
    ')'
    )

    db.session.execute(sql)
    db.session.commit()

    print('Creating table books')
    sql = text(
    'CREATE TABLE books ('
    '  id SERIAL PRIMARY KEY,'
    '  key TEXT UNIQUE NOT NULL,'
    '  author TEXT NOT NULL,'
    '  title TEXT NOT NULL,'
    '  publisher TEXT NOT NULL,'
    '  year INT NOT NULL,'
    '  volume INT,'
    '  number TEXT,' # deliberately TEXT
    '  series TEXT,'
    '  address TEXT,'
    '  edition TEXT,'
    '  month TEXT,'
    '  note TEXT,'
    '  annote TEXT'
    ')'
    )

    db.session.execute(sql)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        setup_db()
