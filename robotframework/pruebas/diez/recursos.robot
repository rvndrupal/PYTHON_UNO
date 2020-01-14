***Settings***
Library     SeleniumLibrary

***Variables***
${navegador}    chrome
#${url}         http://automationpractice.com/index.php
${url}          https://www.amazon.com.mx/?ref=icp_country_us_t1


***Keywords***
Abrir navegador
    Open Browser    ${url}   ${navegador}
   

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

NoVisible
    [Arguments]    ${arg1}
    Element Should Not Be Visible   ${arg1}

Texto
    [Arguments]    ${arg1}  ${arg2}
    Input Text   ${arg1}    ${arg2}

Tiempo2
    [Arguments]    ${arg1}
    Set Selenium Timeout    ${arg1} second

#Opciones del Raton
##################################
MO
    [Arguments]    ${arg1}
    Mouse Over   ${arg1}



   
###################################

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



    


######################
# checar el de tiempo  Wait Until Keyword Succeeds 
    