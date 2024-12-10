*** Settings ***
Resource  resource.robot
Suite Setup      Open Browser And Reset DB 
Suite Teardown   Close Browser


*** Variables ***
@{CITATIONS}     
...    Python    Krisu    Tutorial    myblog    2020
...    C    Alec    overview    lehti    2021
...    Rust    Hanno    tips    web    2022

*** Test Cases ***
Add And Check Multiple Article Citations
    FOR    ${key}    ${author}    ${title}    ${journal}    ${year}    IN    @{CITATIONS}
        Add And Check For Article Citation    ${key}    ${author}    ${title}    ${journal}    ${year}
    END

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

Order by key
    GO TO ${HOME_URL}
    Select Radio Button    sort_by    key
    Click Button    Järjestä
    Sleep    5   
    Close Browser

Order by author
    GO TO ${HOME_URL}
    Select Radio Button    sort_by    author
    Click Button    Järjestä
    Sleep    5    
    Close Browser

Order by title
    GO TO ${HOME_URL}
    Select Radio Button    sort_by    title
    Click Button    Järjestä
    Sleep    5  
    Close Browser