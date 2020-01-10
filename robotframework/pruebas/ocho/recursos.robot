***Settings***
Library     SeleniumLibrary


***Keywords***
Abrir navegador
    Open Browser    ${url}   ${navegador}
    Wait Until Element is Visible  xpath=//img[contains(@class,'logo img-responsive')]

Cerrar
    Close Browser

Ventana
    [Arguments]     ${arg1}     ${arg2}
    Set Window Size     ${arg1}     ${arg2}

Tiempo
    [Arguments]     ${arg1}     
    Set Selenium Speed     ${arg1} seconds


Focus 
    [Arguments]    ${arg1}    
    Set Focus To Element    ${arg1}

Click
    [Arguments]    ${arg1}
    Click Element   ${arg1}

Visible
    [Arguments]    ${arg1}
    Wait Until Element is Visible   ${arg1}

SF
    #SELECCIONAR UN IFRAME
    [Arguments]    ${arg1}
    Select Frame   ${arg1}

USF
    #DESELECCIONAR IFRAME ES IMPORTANTE PARA CIERRE
    Unselect Frame

Comparar
    #Compara dos valores  que se pasan 
    [Arguments]    ${arg1}  ${arg2}
    Element Text Should Be   ${arg1}  ${arg2}



    



    