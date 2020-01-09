*** Settings ***
Documentation   Caso de Prueba con condicionales 
Library         SeleniumLibrary

***Variables***
${navegador}    chrome
${pagina}       http://automationpractice.com/index.php
${Seleccion}    Wom


***Keywords***
Abrir navegador
    Open Browser    ${pagina}   ${navegador}
    Wait Until Element is Visible  xpath=//img[contains(@class,'logo img-responsive')]

Select option Women
    Click Element   xpath=(//a[@href='http://automationpractice.com/index.php?id_category=3&controller=category'][contains(.,'Women')])[1]
    Title Should Be     Women - My Store

Select option Dress
    Click Element   xpath=(//a[@title='Dresses'])[2]
    Title Should Be     Dresses - My Store


***Test Cases***
001 Caso uno condicionales
    Abrir navegador
    Run Keyword if    '${Seleccion}'=='Women'   Select option Women   ELSE     Select option Dress
    Close Browser
   