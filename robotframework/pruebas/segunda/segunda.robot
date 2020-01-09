*** Settings ***
Documentation   Existe en un documento de texto los pasos manuales
...             Esta es la Primera Automatización
Library         Selenium2Library

***Variables***
${pb}    casos de prueba
${navegador}    chrome
${url}      https://www.google.com/
${logo}     xpath=//*[@id="hplogo"]

***Test Cases***
C1 Búsqueda de palabras en Google
    Open Browser    ${url}     ${navegador}
    Wait Until Element is Visible  ${logo}
    Input Text  xpath=//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input  ${pb}
    Click Element  ${logo}
    Click Element   xpath=//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]
    Title Should Be     ${pb} - Buscar con Google
    Page Should Contain     ${pb} 
    Close Browser

C2 Hacer click sin buscar nada
    Open Browser    ${url}     ${navegador}
    Wait Until Element is Visible  ${logo}
    Click Element   xpath=//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]
    Title Should Be     Google
    Close Browser