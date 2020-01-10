***Settings***
Library     String
Resource    recursos.robot


***Variables***
@{items}    (//i[@class='icon-eye-open'])[1]    (//i[@class='icon-eye-open'])[2]    (//i[@class='icon-eye-open'])[3]    (//i[@class='icon-eye-open'])[4]    (//i[@class='icon-eye-open'])[5]    (//i[@class='icon-eye-open'])[6]    (//i[@class='icon-eye-open'])[7]
${navegador}    chrome
${url}          http://automationpractice.com/index.php
${focus}        Set Focus To Element        




*** Test Cases ***
001 Prueba uno de la sección del ojo
    Abrir navegador
    Focus    xpath=(//a[@data-toggle='tab'])[1]
    Ventana  1000   1000
    Tiempo  .5 
    :FOR    ${item}     IN      @{items}
    \       Focus   ${item}
    \       ${nomT}=    Get Text    xpath=(//a[@class='product-name'])[${item}]
    \       Click      xpath=(//i[@class='icon-eye-open'])[1][${item}]
    \       Visible   xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe   #ojo quitar el id para poder visualizarlo muy importante
    \       SF    xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe    #Para ahora seleccionar el iframe
    \       Visible   xpath=//h1[@itemprop='name']    #elemento visible
    \       Comparar     xpath=//h1[@itemprop='name']     ${nomT}  #compara los valores
    \       USF
    \       Click       xpath=//a[@title='Close']

    Cerrar

  