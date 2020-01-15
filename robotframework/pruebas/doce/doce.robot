***Settings***
Documentation   Prueba uno Amazon
Library     String
Resource    ../recursos.robot

#robot -d result  doce.robot

***Variables***
@{items}    7   8   9   10   11   12    13
${buscar}   xpath=(//span[contains(.,'Amazon México')])[3]
${tiempo}   .5
${url}          http://demowebshop.tricentis.com/register
${navegador}    chrome


***Keywords*****


*** Test Cases ***
001 Prueba Carro de Compra
    Abrir navegador
    Ventana  1000   1000
    Maximizar 
    Esperar Iniciar  10
    Esperar Objeto  Register
    Dormir Todos  .2
    Print  Inica test
    SR  Gender  M    
    Texto  xpath=(//input[contains(@class,'text-box single-line')])[1]  Rodrigo
    Print  Nombre ok
    
    Texto  xpath=(//input[contains(@class,'text-box single-line')])[2]  Villanueva
    Print  Apellidos Ok
    
    Texto  xpath=(//input[contains(@class,'text-box single-line')])[3]  rodrigo@gmail.com
    
    Texto  xpath=(//input[contains(@class,'text-box single-line password')])[1]  demo
     
    Texto  xpath=(//input[contains(@class,'text-box single-line password')])[2]  demo
    Print  Termina el test
    
 
 
    Cerrar



