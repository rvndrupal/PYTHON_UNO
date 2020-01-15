***Settings***
Library     SeleniumLibrary
Library     String

***Variables***
#${navegador}    chrome
#${url}         http://automationpractice.com/index.php
#${url}         https://www.amazon.com.mx/?ref=icp_country_us_t1
#${url}          http://www.practiceselenium.com/practice-form.html
#${url}          http://demowebshop.tricentis.com/register


***Keywords***
Abrir navegador
    Open Browser    ${url}   ${navegador}
   

Cerrar
    Close Browser

Ventana
    [Arguments]     ${arg1}     ${arg2}
    Set Window Size     ${arg1}     ${arg2}

Maximizar
    Maximize Browser Window

Tiempo
    [Arguments]     ${arg1}     
    Set Selenium Speed     ${arg1} seconds


Focus 
    [Arguments]    ${arg1}    
    Set Focus To Element    ${arg1}

Click
    [Arguments]    ${arg1}
    Click Element   ${arg1}

Limpiar
    [Arguments]    ${arg1}
    Clear Element Text   ${arg1}

Visible
    [Arguments]    ${arg1}
    Wait Until Element is Visible   ${arg1}

Visible2
    [Arguments]    ${arg1}  
    Element Should Be Visible   ${arg1}    

NoVisible
    [Arguments]    ${arg1}
    Element Should Not Be Visible   ${arg1}

Texto
    [Arguments]    ${arg1}  ${arg2}
    Input Text   ${arg1}    ${arg2}

Obtener
    [Arguments]    ${arg1}  
    Get Value   ${arg1}    

Titulo
    [Arguments]    ${arg1}
    Title Should Be    ${arg1} 

Dormir
    [Arguments]    ${arg1}
    sleep    ${arg1} 

Dormir Todos
    [Arguments]    ${arg1}
    set selenium speed    ${arg1} seconds

Print
    [Arguments]    ${arg1}
    log to console    ${arg1} 

Esperar Objeto
    [Arguments]    ${arg1}
    Wait Until Page Contains    ${arg1} 

Esperar Iniciar
    [Arguments]    ${arg1}
    Set Selenium Timeout    ${arg1} seconds
    

# If
#     [Arguments]     ${arg1}     ${arg2}     ${arg3}
#     Run Keyword if      '${arg1}'=='${arg2}'  ${arg3}

#Opciones del Raton
##################################
MO
    [Arguments]    ${arg1}
    Mouse Over   ${arg1}

   
###################################


#################################
#Select radio
SR
    [Arguments]    ${arg1}  ${arg2}
    Select Radio Button   ${arg1}   ${arg2}

#Select checkbox
SC
    [Arguments]    ${arg1}  
    Select Checkbox	   ${arg1}  

USC
    [Arguments]    ${arg1}  
    Unselect Checkbox   ${arg1}  

#Select lista
SLI
    [Arguments]    ${arg1}  ${arg2}
    Select From List By Index   ${arg1}     ${arg2}
SLL
    [Arguments]    ${arg1}  ${arg2}
    Select From List By Label   ${arg1}    ${arg2}


    
#################################

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
    