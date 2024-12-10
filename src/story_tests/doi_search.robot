*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       reset db

*** Test Cases ***
Perform a succesful DOI search for an article
    Go To  ${HOME_URL}
    Input Text  doi_identifier  10.1504/IJTEL.2013.059495
    Input Text  citation_key  TMC
    Click Button  doi_submit
    Page Should Contain  Martin Pärtel, Matti Luukkainen, Arto Vihavainen, Thomas Vikberg: Test My Code (TMC) 