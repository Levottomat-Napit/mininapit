*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       reset db

*** Variables ***
${key}     testi
${author}     mikko
${title}     tutkimus
${journal}     lehti
${year}     2000
${volume}     15
${pages}     20
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
    Input Text  pages_article  ${pages}
    Click Button  article
    Page Should Contain   mikko: tutkimus (testi)

Submit inproceedings html form that isn't connected to anything
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
    Input Text  pages_article  ${pages}
    Click Button  article
    Page Should Contain   mikko: tutkimus (testi)
    Click Button  BibTeX viitteet
    Page Should Contain  ${bibtex}
    Click Button  Normaalit viitteet
    Page Should Contain   mikko: tutkimus (testi)
