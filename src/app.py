from flask import render_template, request, redirect
from db_helper import reset_db
from repositories.citation_repository import (
    get_citations,
    create_article,
    create_inproceedings,
    create_book,
    delete_citation_by_id
)
from config import app, test_env
from entities.citation import (
    Article,
    Inproceedings,
    Book
)
from doi_search import doi_search

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
        key=request.form['key_article'],
        author=request.form['author_article'],
        title=request.form['title_article'],
        journal=request.form['journal_article'],
        year=request.form['year_article'],
        volume=request.form.get('volume_article'),
        pages=request.form.get('pages_article')
    )

    create_article(info)

    return redirect('/')

@app.post('/inproceedings_new')
def inproceedings_new():

    info = Inproceedings(
        key=request.form['key_inproceedings'],
        author=request.form['author_inproceedings'],
        title=request.form['title_inproceedings'],
        year=request.form['year_inproceedings'],
        booktitle=request.form['booktitle_inproceedings']
    )

    create_inproceedings(info)

    return redirect('/')

@app.post('/book_new')
def book_new():

    info = Book(
        key=request.form['key_book'],
        author=request.form['author_book'],
        title=request.form['title_book'],
        publisher=request.form['publisher_book'],
        year=request.form['year_book']
    )

    create_book(info)

    return redirect('/')

@app.post('/delete')
def delete_citation():
    citation_id = request.form['id']
    citation_type = request.form['type']
    delete_citation_by_id(citation_id, citation_type)

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
    
@app.post('/doi')
def add_doi_citation():
    if request.method == "POST":
        doi = request.form.get('doi')
        key = request.form.get('key')
        try:
            doi_search(doi, key)
        except ValueError:
            print('Error: DOI query did not succeed')

    return redirect('/')
