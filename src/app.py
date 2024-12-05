from flask import render_template, request, redirect
from db_helper import reset_db
from repositories.citation_repository import (
    get_citations,
    create_article,
    create_inproceedings,
    delete_citation_by_id
)
from config import app, test_env
from entities.citation import (
    Article,
    Inproceedings
)

@app.get('/')
def index():
    sort_by = request.args.get('sort_by', None)

    citations = get_citations(sort_by=sort_by)

    return render_template('index.html', citations=citations)

@app.get('/new')
def new():
    return render_template('new.html')

@app.post('/article_new')
def article_new():

    info = Article(
            0,
            request.form['key_article'],
            request.form['author_article'],
            request.form['title_article'],
            request.form['journal_article'],
            request.form['year_article'],
            request.form.get('volume_article'),
            request.form.get('number_article'),
            request.form.get('pages_article'),
            request.form.get('month_article'),
            request.form.get('note_article'),
            request.form.get('annote_article'),
    )

    create_article(info)

    return redirect('/')

@app.post('/inproceedings_new')
def inproceedings_new():

    info = Inproceedings(
        0,
        request.form['key_inproceedings'],
        request.form['author_inproceedings'],
        request.form['title_inproceedings'],
        request.form['year_inproceedings'],
        request.form['booktitle_inproceedings']
    )

    create_inproceedings(info)

    return redirect('/')

@app.post('/delete')
def delete_citation():
    cid = request.form['id']
    ctype = request.form['type']
    delete_citation_by_id(cid, ctype)

    return redirect('/')

@app.get('/toggle-bibtex')
def toggle_bibtex():

    sort_by = request.args.get('sort_by', None)

    citations = get_citations(sort_by=sort_by)

    return render_template('index.html', citations=citations, is_bibtex=True)

if test_env:
    @app.get('/reset-db')
    def reset_database():
        reset_db()
        return 'db reset'

    @app.get('/alive')
    def alive():
        return 'yes'
