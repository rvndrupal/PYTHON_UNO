***Settings***
Library     String
Resource    recursos.robot


***Variables***
@{items}    (//i[@class='icon-eye-open'])[1]    (//i[@class='icon-eye-open'])[2]    (//i[@class='icon-eye-open'])[3]    (//i[@class='icon-eye-open'])[4]    (//i[@class='icon-eye-open'])[5]    (//i[@class='icon-eye-open'])[6]    (//i[@class='icon-eye-open'])[7]
${navegador}    chrome
${url}          http://automationpractice.com/index.php

***Keywords***
Abrir navegador
    Open Browser    ${url}   ${navegador}
    Wait Until Element is Visible  xpath=//img[contains(@class,'logo img-responsive')]


*** Test Cases ***
001 Prueba uno de la sección del ojo
    Abrir navegador
    Set Focus To Element    xpath=(//a[@data-toggle='tab'])[1]
    Set Window Size  1000   1000
    Set Selenium Speed  0.1 seconds
    :FOR    ${item}     IN      @{items}
    \       Set Focus To Element    ${item}    #focus del elemento
    \       ${nomT}=    Get Text    xpath=(//a[@class='product-name'])[${item}]
    \       Click Element       xpath=(//i[@class='icon-eye-open'])[1][${item}]
    \       Wait Until Element is Visible   xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe   #ojo quitar el id para poder visualizarlo muy importante
    \       Select Frame    xpath=//*[@id="index"]/div[2]/div/div/div/div/iframe    #Para ahora seleccionar el iframe
    \       Wait Until Element is Visible   xpath=//h1[@itemprop='name']    #elemento visible
    \       Element Text Should Be     xpath=//h1[@itemprop='name']     ${nomT}  #compara los valores
    \       Unselect Frame
    \       Click Element       xpath=//a[@title='Close']

    Close Browser

  