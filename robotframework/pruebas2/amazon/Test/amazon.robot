***Settings***
Documentation   Primer Caso de test Amazon
Library     Selenium2Library

#correr
#robot -d results Test/amazon.robot
#robot -d results -v navegador:chrome Test/amazon.robot



*** Variables ***
${navegador}    firefox


*** Test Cases ***
p001 Usuario oprime ckeckout
    [Documentation]     Información Basica sobre este test
    [Tags]      Smoke
    Open Browser        http://www.amazon.com  ${navegador}
    

    Close Browser



*** Keywords ***