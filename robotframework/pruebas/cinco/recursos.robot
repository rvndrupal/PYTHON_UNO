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