def generate_bibtex(citation):
    btxfields = []

    if citation.type_as_string == 'article':
        btxfields = [
            'author', 'title', 'journal', 'year', 'volume', 'pages',
            'number', 'month', 'note', 'annote'
            ]

    if citation.type_as_string == 'inproceedings':
        btxfields = [
            'author', 'title', 'year', 'booktitle', 'editor', 'volume',
            'number', 'series', 'pages', 'month', 'address', 'organization',
            'publisher', 'note', 'annote'
        ]

    if citation.type_as_string == 'book':
        btxfields = [
            'author', 'title', 'publisher', 'year', 'volume', 'number',
            'series', 'address', 'edition', 'month', 'note', 'annote'
        ]

    btx = f'@{citation.type_as_string}{{{citation.key},\n'

    for field in btxfields:
        value = getattr(citation, field)

        if value:
            btx += f'  {field} = {{{value}}},\n'

    return btx + '}'

def normal_citation_str(citation):
    return f'{citation.author}: {citation.title} ({citation.key})'
