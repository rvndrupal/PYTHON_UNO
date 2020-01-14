***Settings***
Library     String
Resource    recursos.robot

*** Test Cases ***
001 Prueba imagen
    Abrir navegador
    Tiempo  .8
    Ventana  1800   1000  
    Focus    xpath=(//a[@data-toggle='tab'])[1]
    MO     xpath=(//img[@width='250'])[1]
    Click  xpath=(//span[contains(.,'Quick view')])[1]
    SF    xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe
    Visible  xpath=//h1[contains(@itemprop,'name')]
    USF
    Cerrar

002 Prueba imagen falla
    Abrir navegador
    Tiempo  .8
    Ventana  1800   1000  
    Focus    xpath=(//a[@data-toggle='tab'])[1]
    MO     xpath=(//img[@width='250'])[1]
    Click  xpath=(//span[contains(.,'Quick view')])[1]
    SF    xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe
    Visible  xpath=//h1[contains(@itemprop,'namess')]
    USF
    Cerrar

003 Buscar texto
    Abrir navegador
    Tiempo  .8
    Ventana  1800   1000  
    Focus    xpath=(//a[@data-toggle='tab'])[1]
   
    Cerrar
