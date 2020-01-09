*** Settings ***
Documentation   Caso de Prueba con condicionales y Loops
Library         String
Library         SeleniumLibrary


***Variables***
${navegador}    chrome
${pagina}       automationpractice.com/index.php
${Seleccion}    Wom
${esquema}      http
${url}          ${esquema}://${pagina}
${logo}         //img[@alt='My Store']


***Keywords***
Abrir navegador
    Open Browser    ${url}   ${navegador}
    Wait Until Element is Visible  xpath=//img[contains(@class,'logo img-responsive')]

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