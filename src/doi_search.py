import urllib.request, json

#Early proof of concept-version of the doi search function

def doi_search(doi):
    with urllib.request.urlopen(f"https://api.crossref.org/works/{doi}") as url:
        data = json.load(url)
        print(data)
        data_type = data["message"]["type"]
        data_author = []
        data_year = (data["message"]["indexed"]["date-time"])
        authors = data["message"]["author"]
        for author in authors:
            data_author.append(author["family"]+" "+author["given"])
        data_author = ", ".join(data_author)
        print(data_author)
        print(data_year[:4])

        # if data_type == "journal-article":
        #     pass
        # elif data_type == "proceedings-article":
        #     pass
        # elif data_type == "book":
        #     pass
        # else:
        #     pass
        # title = data["message"]["title"][0]
        

# An example search
doi_search("10.1145/3551349.3559494")
