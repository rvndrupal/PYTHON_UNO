*** Settings ***
Documentation   Caso de Prueba Trucos, If y Loops
Library         String
Library         SeleniumLibrary


***Variables***
${navegador}    chrome
${pagina}       automationpractice.com/index.php
${Seleccion}    Wom
${esquema}      http
${url}          ${esquema}://${pagina}
${logo}         //img[@alt='My Store']
${web}          http://www.winstoncastillo.com/udemy/

***Keywords***
Abrir navegador
    Open Browser    ${url}   ${navegador}
    Wait Until Element is Visible  xpath=//img[contains(@class,'logo img-responsive')]

Abrir navegadorDos
    Open Browser    ${web}   ${navegador}
    Wait Until Element is Visible  xpath=//img[contains(@class,'card-img-top')]

Select option Women
    Click Element   xpath=(//a[@href='http://automationpractice.com/index.php?id_category=3&controller=category'][contains(.,'Women')])[1]
    Title Should Be     Women - My Store

Select option Dress
    Click Element   xpath=(//a[@title='Dresses'])[2]
    Title Should Be     Dresses - My Store


***Test Cases***
001 Caso uno condicionales
    Abrir navegador
    Run Keyword if    '${Seleccion}'=='Women'   Select option Women   ELSE     Select option Dress
    Close Browser

002 Caso de Prueba Loops
    Abrir navegador
    Set Global Variable     @{nombresDeContenedores}    //*[@id="homefeatured"]/li[1]/div/div[2]/h5/a       //*[@id="homefeatured"]/li[2]/div/div[2]/h5/a       //*[@id="homefeatured"]/li[3]/div/div[2]/h5/a       //*[@id="homefeatured"]/li[4]/div/div[2]/h5/a       //*[@id="homefeatured"]/li[5]/div/div[2]/h5/a       //*[@id="homefeatured"]/li[6]/div/div[2]/h5/a        //*[@id="homefeatured"]/li[7]/div/div[2]/h5/a
    :FOR    ${nombreDeContenedor}   IN      @{nombresDeContenedores}
    \   Click Element       xpath=${nombreDeContenedor}
    \   Wait Until Element Is Visible   xpath=//*[@id="bigpic"]
    \   Click Element       xpath=//*[@id="header_logo"]/a/img
    Close Browser

003 Caso de prueba Trucos
    Abrir navegadorDos
    Click Element   xpath=(//a[contains(@class,'card-link')])[1]
    Title Should Be    Winston Castillo – Un sitio para comunicarse
    Close Browser

004 Caso de Prueba abrir Ventana Modal
    Abrir navegadorDos
    Title Should Be     Hola Mundo!
    Set Focus To Element    xpath=(//a[@href='#'])[5]
    Click Link   xpath=(//a[@href='#'])[5]
    Title Should Be     Hola Mundo!
    Wait Until Element is Visible   xpath=//h5[@class='modal-title']
    Close Browser


001 Abrir pagina y cambiar tamano
    Open Browser    https://www.mobilepractice.io/en/       chrome
    Set Window Size      1500      1000
    Set Window Size      767       600
    Element Should Be Visible    xpath=//section[contains(@class,'hero')]   
    Set Window Size      900       600
    Element Should Be Visible    xpath=//section[contains(@class,'hero')]   
    Close Browser


