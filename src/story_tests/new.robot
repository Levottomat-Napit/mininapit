*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       reset db

** Variables ***
${key}     testi
${author}     mikko
${title}     tutkimus
${journal}     lehti
${year}     2000
${volume}     15
${number}     71
${pages}     20
${month}     12
${note}     mahtava 
${annote}     lol
${booktitle}     kirjannimi
${bibtex}    @article{testi,\n \ author = {mikko},\n \ title = {tutkimus},\n \ journal = {lehti},\n \ year = {2000},\n \ volume = {15},\n \ pages = {20}\n}

*** Test Cases ***
Submit and check for article citation
    GO TO  ${NEW_URL}
    Select From List By Value  formSelector  article
    Input Text  key_article  ${key}
    Input Text  author_article  ${author}
    Input Text  title_article  ${title}
    Input Text  journal_article  ${journal}
    Input Text  year_article  ${year}
    Input Text  volume_article  ${volume}
    Input Text  number_article  ${number}
    Input Text  pages_article  ${pages}
    Input Text  month_article  ${month}
    Input Text  note_article  ${note}
    Input Text  annote_article  ${annote}
    Click Button  article
    Page Should Contain   mikko: tutkimus (testi)

Submit and check for inproceedings citation
    GO TO  ${NEW_URL}
    Select From List By Value  formSelector  inproceedings
    Input Text  key_inproceedings  ${key}2
    Input Text  author_inproceedings  ${author}
    Input Text  title_inproceedings  ${title}
    Input Text  year_inproceedings  ${year}
    Input Text  booktitle_inproceedings  ${booktitle}
    Click Button  inproceedings
    Page Should Contain   mikko: tutkimus (testi2)

Submit and check that the toggle BibTeX button works
    GO TO  ${NEW_URL}
    Select From List By Value  formSelector  article
    Input Text  key_article  ${key}
    Input Text  author_article  ${author}
    Input Text  title_article  ${title}
    Input Text  journal_article  ${journal}
    Input Text  year_article  ${year}
    Input Text  volume_article  ${volume}
    Input Text  number_article  ${number}
    Input Text  pages_article  ${pages}
    Input Text  month_article  ${month}
    Input Text  note_article  ${note}
    Input Text  annote_article  ${annote}
    Click Button  article
    Page Should Contain   mikko: tutkimus (testi)
    Click Button  BibTeX viitteet
    Page Should Contain  ${bibtex}
    Click Button  Normaalit viitteet
    Page Should Contain   mikko: tutkimus (testi)

Submit and check for book citation with required fields
    GO TO  ${NEW_URL}
    Select From List By Value  formSelector  book
    Input Text  key_book  ${key}
    Input Text  author_book  ${author}
    Input Text  title_book  kirja
    Input Text  publisher_book  julkaisija
    Input Text  year_book  ${year}
    Click Button  book
    Page Should Contain   mikko: kirja (testi)