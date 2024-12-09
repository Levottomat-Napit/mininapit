import urllib.request, json
from entities.citation import Article, Inproceedings, Book
from repositories.citation_repository import create_article, create_inproceedings, create_book

#Early proof of concept-version of the doi search function

def doi_search(doi, data_key):
    try:
        with urllib.request.urlopen(f"https://api.crossref.org/works/{doi}") as url:
            data = json.load(url)
    except:
        return False

    data_type = data["message"]["type"]
    data_title = data["message"]["title"][0]
    data_author = []
    data_year = ((data["message"]["indexed"]["date-time"])[:4])
    authors = data["message"]["author"]
    for author in authors:
        data_author.append(author["given"]+" "+author["family"])
    data_author = ", ".join(data_author)

    if data_type == "journal-article":
        data_journal = data["message"]["container-title"][0]
        article = Article(
            key=data_key, 
            author=data_author, 
            title=data_title, 
            journal = data_journal, 
            year = data_year)
        create_article(article)
        return True
    elif data_type == "proceedings-article":
        pass
    elif data_type == "book":
        pass
    else:
        return False
    
# An example search
doi_search("10.10.1109/TASLP.2019.2950099", "rust")
