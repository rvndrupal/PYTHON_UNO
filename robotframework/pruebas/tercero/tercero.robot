*** Settings ***
Documentation   Casos de Prueba con Variables y Keywords
...             Se ejecutan tres busquedas
...             La ultima busqueda se carga un manual de Python
Library         Selenium2Library

***Variables***
${pb}    casos de prueba
${navegador}    chrome
${url}      https://www.google.com/
${logo}     xpath=//*[@id="hplogo"]
${enter}    xpath=//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]
${caja}     xpath=//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input


***Keywords***
Abrir navegador
    Open Browser    ${url}     ${navegador}
    Wait Until Element is Visible  ${logo}


***Test Cases***
C1 Búsqueda de palabras en Google
    Abrir navegador
    Input Text  xpath=//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input  ${pb}
    Click Element  ${logo}
    Click Element   xpath=//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]
    Title Should Be     ${pb} - Buscar con Google
    Page Should Contain     ${pb} 
    Close Browser

C2 Hacer click sin buscar nada
    Abrir navegador
    Click Element   xpath=//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]
    Title Should Be     Google
    Close Browser

C3 Búsqueda de Documentación Python
    Abrir navegador
    Input Text  ${caja}  python
    Click Element  ${logo}
    Click Element   ${enter}
    Click Element   xpath=(//h3[contains(@class,'LC20lb')])[1]
    Title Should Be     Welcome to Python.org 
    Click Element   xpath=(//a[@href='/doc/'])[1]
    Click Element   xpath=(//a[@href='https://wiki.python.org/moin/BeginnersGuide'])[2]
    Close Browser
