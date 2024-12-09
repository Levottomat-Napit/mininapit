import urllib.request, json
from entities.citation import Article, Inproceedings, Book
from repositories.citation_repository import create_article, create_inproceedings, create_book

def doi_search(doi, data_key):
    try:
        with urllib.request.urlopen(f"https://api.crossref.org/works/{doi}") as url:
            data = json.load(url)
    except:
        return False

    data_type = data["message"]["type"]
    data_title = data["message"]["title"][0]
    data_year = data['message']['published']['date-parts'][0][0]

    author = None

    if 'author' in data['message']:
        if isinstance(data['message']['author'], list):
            authors = [author['given'] + ' ' + author['family'] for author in data['message']['author']]
            author = ', '.join(authors)
        else:
            author = data['message']['author']
    elif 'author' not in data['message'] and 'editor' in data['message']:
        editors = data['message']['editor']
        if isinstance(editors, list):
            author = ', '.join([editor['given'] + ' ' + editor['family'] for editor in editors])
        else:
            author = editors

    if data_type == "journal-article":
        data_journal = data["message"]["container-title"][0]
        article = Article(
            key = data_key, 
            author = author, 
            title = data_title, 
            journal = data_journal, 
            year = data_year)
        create_article(article)
        return True
    
    elif data_type == "proceedings-article":
        data_booktype = data["message"]["container-title"][0]
        inproceeding = Inproceedings(
            key = data_key,
            author = author,
            title = data_title,
            year = data_year,
            booktitle = data_booktype
        )
        create_inproceedings(inproceeding)
        return True
    
    elif data_type == "book" or data_type == "edited_book":
        data_publisher = data["message"]["publisher"]
        book = Book(
            key = data_key,
            author = author,
            title = data_title,
            publisher = data_publisher,
            year = data_year
        )
        create_book(book)
        return True
    
    else:
        return False
    
# An example article search
# doi_search("10.1038/nature12373", "citation_key")

# An example inproceeding search
# doi_search("10.10.1109/TASLP.2019.2950099", "citation_key")

# An example book search
# doi_search("10.1145/3674127", "citation_key")