***Settings***
Documentation   Prueba uno Amazon
Library     String
Resource    recursos.robot

#robot -d result  diez.robot

***Variables***
@{items}    7   8   9   10   11   12    13
${buscar}   xpath=(//span[contains(.,'Amazon México')])[3]
${url}         https://www.amazon.com.mx/?ref=icp_country_us_t1
${navegador}    chrome

***Keywords*****
Buscar pelota
    Focus   xpath=(//img[contains(@src,'.jpg')])[6]

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

# 002 Prueba busqueda monitor
#     Abrir navegador
#     Tiempo  .2
#     Ventana  1400   1000     
#     Texto  xpath=(//input[@class='nav-input'])[2]   monitores para pc
#     Click  xpath=(//input[@type='submit'])[1]   
#     Visible     xpath=(//span[contains(@class,'a-size-medium a-color-base a-text-normal')])[3]
#     Focus   xpath=(//span[contains(@class,'a-size-medium a-color-base a-text-normal')])[3]
#     Click  xpath=(//span[contains(@class,'a-size-medium a-color-base a-text-normal')])[3]
#     :FOR    ${item}    IN   @{items}
#     \    MO     xpath=(//input[contains(@class,'a-button-input')])[${item}]
#     MO  xpath=(//input[@class='a-button-input'])[7]
#     Click  xpath=//input[contains(@id,'add-to-cart-button')]
#     Click  xpath=(//span[@class='a-label a-checkbox-label'][contains(.,'Es un regalo')])[1]
#     Click   xpath=(//a[contains(@id,'hlb-ptc-btn-native')])[1]
#     Texto   xpath=//input[@id='ap_email']    rodrigodrupal1@gmail.com
#     Click   xpath=//input[@id='continue']
#     Texto   xpath=//input[contains(@id,'ap_password')]      demo de la contraseña
#     Titulo  Amazon Iniciar sesión
#     Cerrar

003 Prueba de Condicional if
    Abrir navegador
    Tiempo  .9
    Ventana  1100   1000
    Maximizar
    Focus   xpath=(//h2[@class='a-color-base headline truncate-1line'])[1]
    Click  xpath=//img[contains(@data-a-hires,'https://images-na.ssl-images-amazon.com/images/I/81qnWqv45lL._AC_SY480_.jpg')]
   
    Run Keyword If   'Amazon México'=='Amazon México'   Buscar pelota  ELSE  Abrir Navegador
    Visible2  xpath=(//img[contains(@src,'.jpg')])[6]
    sleep   1
    Texto   xpath=(//input[contains(@type,'text')])[1]    Bat de Beisbol
    Limpiar     xpath=(//input[contains(@type,'text')])[1]
    Sleep   1
    Texto   xpath=(//input[contains(@type,'text')])[1]    Bat de Beisbol
    Click  xpath=(//input[contains(@type,'submit')])[1]

    Cerrar
