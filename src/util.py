def generate_bibtex(a):
    btxfields = []

    if a.type_as_string == 'article':
        btxfields = [
            'author', 'title', 'journal', 'year', 'volume', 'pages',
            'number', 'month', 'note', 'annote'
            ]

    if a.type_as_string == 'inproceedings':
        btxfields = [
            'author', 'title', 'year', 'booktitle', 'editor', 'volume',
            'number', 'series', 'pages', 'month', 'address', 'organization',
            'publisher', 'note', 'annote'
        ]

    if a.type_as_string == 'book':
        btxfields = [
            'author', 'title', 'publisher', 'year', 'volume', 'number',
            'series', 'address', 'edition', 'month', 'note', 'annote'
        ]

    btx = f'@{a.type_as_string}{{{a.key},\n'

    for x in btxfields:
        xx = getattr(a, x)

        if xx:
            btx += f'  {x} = {{{xx}}},\n'

    return btx + '}'
