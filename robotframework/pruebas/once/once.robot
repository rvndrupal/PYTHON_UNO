***Settings***
Documentation   Prueba uno Amazon
Library     String
Resource    ../recursos.robot

#robot -d result  once.robot

***Variables***
@{items}    7   8   9   10   11   12    13
${buscar}   xpath=(//span[contains(.,'Amazon México')])[3]
${tiempo}   .1
${url}          http://www.practiceselenium.com/practice-form.html
${navegador}    chrome

***Keywords*****


*** Test Cases ***
001 Prueba Ofertas del Día
    Abrir navegador
    Ventana  1000   1000
    Maximizar     
    Texto  xpath=(//input[@type='text'])[1]  Rodrigo
    Dormir  ${tiempo}
    Texto  xpath=(//input[@type='text'])[2]  Villanueva
    Dormir  ${tiempo}
    SR   sex    Female      #se pasa el valor del name y el value
    Dormir  ${tiempo}
    SR  exp  5
    Dormir    ${tiempo}
    Texto  xpath=(//input[@type='text'])[3]     19/09/1977
    Dormir  ${tiempo}
    SC  xpath=(//input[contains(@type,'checkbox')])[1]
    Dormir  ${tiempo}
    SC  xpath=(//input[contains(@type,'checkbox')])[6]
    Dormir  ${tiempo}
    USC  xpath=(//input[contains(@type,'checkbox')])[6]
    Dormir  ${tiempo}
    Focus   xpath=//label[contains(.,'Now that you had tea, lets get back to work:)')]
    SLL  continents  Antartica
    Dormir  ${tiempo}
    SLI  continents  2
    Dormir  ${tiempo}
    SLI   selenium_commands     3
    Dormir  2
    SLL  selenium_commands      Switch Commands   
    Dormir  3
 
    Cerrar



