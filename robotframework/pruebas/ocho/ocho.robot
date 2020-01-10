***Settings***
Library     String
Resource    recursos.robot


***Variables***
#@{items}    (//i[@class='icon-eye-open'])[1]    (//i[@class='icon-eye-open'])[2]    (//i[@class='icon-eye-open'])[3]    (//i[@class='icon-eye-open'])[4]    (//i[@class='icon-eye-open'])[5]    (//i[@class='icon-eye-open'])[6]    (//i[@class='icon-eye-open'])[7]
${navegador}    chrome
${url}          http://automationpractice.com/index.php
${focus}        Set Focus To Element  
@{items}    1   2   3   4   5   6   7    
${titulo}       xpath=//h1[contains(@itemprop,'name')]  




*** Test Cases ***
001 Prueba uno de la sección del ojo
    Abrir navegador
    Focus    xpath=(//a[@data-toggle='tab'])[1]
    Tiempo  .8
    Ventana  1800   1000    
    Ventana  1000   1000
    Tiempo  .1
    :FOR    ${item}     IN      @{items}
    \       Focus   xpath=(//a[@class='product-name'])[${item}]
    \       ${nomT}=    Get Text    xpath=(//a[@class='product-name'])[${item}]
    \       Log     ${nomT}
    \       Click      xpath=(//i[@class='icon-eye-open'])[${item}]
    \       Visible   xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe   #ojo quitar el id para poder visualizarlo muy importante
    \       SF    xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe    #Para ahora seleccionar el iframe
    \       Visible   ${titulo}   #elemento visible
    \       Log         ${titulo}
    \       Comparar     ${titulo}    ${nomT}  #compara los valores    
    \       USF
    \       Click       xpath=//a[@title='Close']

    Cerrar

002 Prueba dos de la sección del dos
    Abrir navegador
    Focus    xpath=(//a[@data-toggle='tab'])[1]
    Tiempo  .8
    Ventana  1800   1000    
    Ventana  1300   1000
    Tiempo  .1
    :FOR    ${item}     IN      @{items}
    \       Focus   xpath=(//a[@class='product-name'])[${item}]
    \       ${nomT}=    Get Text    xpath=(//a[@class='product-name'])[${item}]
    \       Log     ${nomT}
    \       MO         xpath=(//img[@width='250'])[${item}]
    \       Click      xpath=(//span[contains(.,'Quick view')])[${item}]
    \       Visible   xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe   #ojo quitar el id para poder visualizarlo muy importante
    \       SF    xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe    #Para ahora seleccionar el iframe
    \       Visible   ${titulo}   #elemento visible
    \       Log         ${titulo}
    \       Comparar     ${titulo}    ${nomT}  #compara los valores    
    \       USF
    \       Click       xpath=//a[@title='Close']

    Cerrar


  