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
    Input Text  key_inproceedings  ${key}
    Input Text  author_inproceedings  ${author}
    Input Text  title_inproceedings  ${title}
    Input Text  year_inproceedings  ${year}    
    Input Text  booktitle_inproceedings  ${booktitle} 
    Click Button  inproceedings

Submit and check that the toggle BibTeX button works
    GO TO  ${NEW_URL}
    Input Text  key  ${key}
    Input Text  author  ${author}
    Input Text  title  ${title}
    Input Text  journal  ${journal}
    Input Text  year  ${year}     
    Input Text  volume  ${volume}
    Input Text  pages  ${pages}
    Click Button  submit
    Page Should Contain   mikko: tutkimus (testi)
    Click Button  Toggle BibTeX
    Page Should Contain  ${bibtex}
    Click Button  Toggle normal citations
    Page Should Contain   mikko: tutkimus (testi)
