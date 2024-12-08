import urllib.request, json

#Early proof of concept-version of the doi search function

def doi_search(doi):
    with urllib.request.urlopen(f"https://api.crossref.org/works/{doi}") as url:
        data = json.load(url)
        print(data)
        title = data["message"]["title"][0]
        type = data["message"]["type"]
        print(title, type)

# An example search
doi_search("10.1145/3551349.3559494")