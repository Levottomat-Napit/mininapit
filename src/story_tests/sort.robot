*** Settings ***
Resource         resource.robot
Suite Setup      Open Browser And Reset DB 
Suite Teardown   Close Browser
Test Setup       go home


*** Variables ***
${bibtex1}  @article{Python,\n \ author = {Krisu},\n \ title = {Tutorial},\n \ journal = {myblog},\n \ year = {2020},\n}

${bibtex2}  @article{C,\n \ author = {Alec},\n \ title = {overview},\n \ journal = {lehti},\n \ year = {2021},\n}

${bibtex3}  @article{Rust,\n \ author = {Hanno},\n \ title = {tips},\n \ journal = {web},\n \ year = {2022},\n}

@{CITATIONS}     
...    Python    Krisu    Tutorial    myblog    2020
...    C    Alec    overview    lehti    2021
...    Rust    Hanno    tips    web    2022

*** Test Cases ***
Add And Check Multiple Article Citations
    FOR    ${key}    ${author}    ${title}    ${journal}    ${year}    IN    @{CITATIONS}
        Add And Check For Article Citation    ${key}    ${author}    ${title}    ${journal}    ${year}
    END

Order by key
    Select Radio Button    sort_by    key
    Click Button    Järjestä
    Click Button  BibTeX viitteet
    Page Should Contain  ${bibtex1}  

Order by author
    Select Radio Button    sort_by    author
    Click Button    Järjestä
    Click Button  BibTeX viitteet
    Page Should Contain  ${bibtex2}

Order by title
    Select Radio Button    sort_by    title
    Click Button    Järjestä
    Click Button  BibTeX viitteet
    Page Should Contain  ${bibtex3}

*** Keywords ***
Add And Check For Article Citation
    [Arguments]    ${key}    ${author}    ${title}    ${journal}    ${year}
    Go To    ${NEW_URL}
    Select From List By Value    formSelector    article
    Input Text    key_article  ${key}
    Input Text    author_article  ${author}
    Input Text    title_article  ${title}
    Input Text    journal_article  ${journal}
    Input Text    year_article  ${year}
    Click Button    article
    Page Should Contain    ${author}: ${title} (${key})