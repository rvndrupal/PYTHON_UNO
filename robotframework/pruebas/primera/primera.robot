*** Settings ***
Documentation   Existe en un documento de texto los pasos manuales
...             Esta es la Primera Automatización
Library         Selenium2Library

***Test Cases***
C1 Búsqueda de palabras en Google
    Open Browser    https://www.google.com/     chrome
    Wait Until Element is Visible   xpath=//*[@id="hplogo"]
    Input Text  xpath=//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input  casos de prueba
    Click Element   xpath=//*[@id="hplogo"]
    Click Element   xpath=//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]
    Title Should Be     casos de prueba - Buscar con Google
    Page Should Contain     casos de prueba 
    Close Browser

C2 Hacer click sin buscar nada
    Open Browser    https://www.google.com/     chrome
    Wait Until Element is Visible   xpath=//*[@id="hplogo"]
    Click Element   xpath=//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]
    Title Should Be     Google
    Close Browser