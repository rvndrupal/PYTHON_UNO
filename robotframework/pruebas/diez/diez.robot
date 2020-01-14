***Settings***
Documentation   Prueba uno Amazon
Library     String
Resource    recursos.robot

#robot -d result  diez.robot

***Variables***
@{items}    7   8   9   10   11   12    13

*** Test Cases ***
# 001 Prueba Ofertas del Día
#     Abrir navegador
#     Tiempo  .2
#     Ventana  1400   1000     
#     Texto  xpath=(//input[@class='nav-input'])[2]   ofertas del dia
#     Click  xpath=(//input[@type='submit'])[1]
#     Click  xpath=(//i[contains(@class,'a-icon a-icon-checkbox')])[1]
#     Click  xpath=(//i[contains(@class,'a-icon a-icon-checkbox')])[1]
#     Focus  xpath=(//span[contains(@class,'a-size-base a-color-base a-text-bold')])[5]
#     Click  xpath=(//i[contains(@class,'a-icon a-icon-checkbox')])[5]
#     Focus  xpath=(//span[contains(.,'¿Necesitas ayuda?')])[4]
#     Visible     xpath=//span[@class='a-size-base-plus a-color-base a-text-normal']
#     Cerrar

002 Prueba busqueda monitor
    Abrir navegador
    Tiempo  .2
    Ventana  1400   1000     
    Texto  xpath=(//input[@class='nav-input'])[2]   monitores para pc
    Click  xpath=(//input[@type='submit'])[1]   
    Visible     xpath=(//span[contains(@class,'a-size-medium a-color-base a-text-normal')])[3]
    Focus   xpath=(//span[contains(@class,'a-size-medium a-color-base a-text-normal')])[3]
    Click  xpath=(//span[contains(@class,'a-size-medium a-color-base a-text-normal')])[3]
    :FOR    ${item}    IN   @{items}
    \    MO     xpath=(//input[contains(@class,'a-button-input')])[${item}]
    MO  xpath=(//input[@class='a-button-input'])[7]
    Click  xpath=//input[contains(@id,'add-to-cart-button')]
    Click  xpath=(//span[@class='a-label a-checkbox-label'][contains(.,'Es un regalo')])[1]
    Click   xpath=(//a[contains(@id,'hlb-ptc-btn-native')])[1]
    Texto   xpath=//input[@id='ap_email']    rodrigodrupal1@gmail.com
    Click   xpath=//input[@id='continue']
    Texto   xpath=//input[contains(@id,'ap_password')]      demo de la contraseña

    Cerrar

