*** Settings ***
Resource         resource.robot
Library          OperatingSystem
Library          SeleniumLibrary
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       reset db

*** Variables ***

#vaihda latauskansion osoite koneelle josta testi tapahtuu
#${DOWNLOAD_FOLDER}    /home/sadlaiho/Downloads
#${BROWSER_OPTIONS}    prefs={"download.default_directory": "${DOWNLOAD_FOLDER}", "download.prompt_for_download": False}
${key}     tiedoston_lataus_testi
${author}     samuli
${title}     lataustutkimus
${journal}     latauslehti
${year}     2077
${volume}     616
${pages}     40-60
${booktitle}     Tiedostojen lataamisen alkeet
${BIBTEX}    @article{testi,\n \
...          author = {samuli},\n \
...          title = {lataustutkimus},\n \
...          journal = {latauslehti},\n \
...          year = {2077},\n \
...          volume = {616},\n \
...          pages = {40-60}\n}
${EXPECTED_FILE}    mun_bibtex.bib

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
    Page Should Contain  samuli: lataustutkimus (tiedoston_lataus_testi)

#kytketty toisaiseksi pois ettei ci herjaa
#Download the file
#    GO TO  ${HOME_URL}
#    Click Element  xpath=//a[@download="mun_bibtex.bib"]
#    Sleep  2s

#Check downloaded file exists
#    ${file_path}=    Set Variable    ${DOWNLOAD_FOLDER}/${EXPECTED_FILE}
#    File Should Exist    ${file_path}