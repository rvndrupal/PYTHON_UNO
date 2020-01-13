***Settings***
Documentation   Primer Caso de test Amazon
Library     Selenium2Library



*** Variables ***


*** Test Cases ***
p001 Usuario oprime ckeckout
    [Documentation]     Información Basica sobre este test
    [Tags]      Smoke
    Open Browser        http://www.amazon.com  firefox
    #Open Browser        http://www.amazon.com  chrome

    Close Browser



*** Keywords ***