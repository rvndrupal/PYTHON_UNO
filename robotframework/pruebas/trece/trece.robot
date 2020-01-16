***Settings***
Documentation   Prueba uno Amazon
Library     String
Resource    ../recursos.robot

#robot -d result  trece.robot

***Variables***
@{items}    7   8   9   10   11   12    13
${buscar}   xpath=(//span[contains(.,'Amazon México')])[3]
${tiempo}   .5
#${url}          http://testautomationpractice.blogspot.com  para las alertas caso uno
${url}         http://seleniumhq.github.io/selenium/docs/api/java/index
${navegador}    chrome


***Keywords***


*** Test Cases ***
# 001 Ventanas Alertas y Frames
    # Abrir navegador
    # Maximizar 
    # Dormir Todos  1
    # Click       xpath=//button[contains(.,'Click Me')]
    # Print  Alerta ok
    # Alerta texto  Press a button!
    # Print  Cierre con texto presente    
    # Cerrar

002 Manejo de Frames
    Abrir navegador
    Maximizar
    Dormir Todos  3

    SF  packageListFrame    #id name
    Print  Seleccionamos el primer frame
    Click  xpath=(//a[@target='packageFrame'])[6]
    USF
    Print  Se cierra el primer frame

    SF      packageFrame
    Print  Se abre el segundo frame
    Click   xpath=(//span[@class='interfaceName'])[1]
    USF
    Print  Cierre del segundo aframe


    SF      classFrame
    Print  Se abre el tercer frame
    Click   xpath=(//a[contains(.,'Help')])[1]
    USF
    Print  Cierre del tercer frame

    Cerrar







