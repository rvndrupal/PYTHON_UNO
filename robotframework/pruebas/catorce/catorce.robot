***Settings***
Documentation   Prueba uno Amazon
Library     String
Resource    ../recursos.robot

#robot -d result  catorce.robot

***Variables***
@{items}    7   8   9   10   11   12    13
${buscar}   xpath=(//span[contains(.,'Amazon México')])[3]
${tiempo}   .5
${url}         http://testautomationpractice.blogspot.com/
${url2}        https://www.google.com/
${navegador}    chrome


***Keywords***


*** Test Cases ***
001 Ventanas Multiples
    Abrir navegador
    Maximizar    
    Abrir navegador2
    Maximizar

    Dormir Todos  .3

    Switch Ventana  1
    ${nom}=    Get Title 
    Print   Cambio a la Ventana uno
    Print   ${nom}
   
    Cerrar


