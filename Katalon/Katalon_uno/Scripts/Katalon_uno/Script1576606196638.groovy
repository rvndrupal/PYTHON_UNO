import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://localhost:8000/login/')

WebUI.setText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Bienvenido de Nuevo_username'), 
    'juan')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Bienvenido de Nuevo_password'), 
    'j9hAjqIhulY=')

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/button_Acceder'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/button_ok'))

WebUI.setText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Bienvenido de Nuevo_username'), 
    'rodrigo')

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/button_Acceder'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/button_ok'))

WebUI.setText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Bienvenido de Nuevo_username'), 
    'rodrigo')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Bienvenido de Nuevo_password'), 
    '4kAQk6V+Nxj1ag62BRjXEg==')

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/button_Acceder'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/a_Catlogos'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/a_Categorias'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/i_Listado de Sub Categoras_fas fa-ellipsis-_f238ac'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/a_Nueva'))

WebUI.setText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Nueva  Categora_descripcion'), 
    'demo uno')

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Estado_estado'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/a_Cancelar'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/a_Listado de Sub Categoras_dropdownMenuLink'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/a_Nueva'))

WebUI.setText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Nueva  Categora_descripcion'), 
    'Nuevo 1234')

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Estado_estado'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/button_Guardar'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/button_ok'))

WebUI.setText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Search_form-control form-control-sm'), 
    'nuevo')

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/i_Activo_far fa-edit'))

WebUI.setText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Nueva  Categora_descripcion'), 
    ' NUEVO 12345')

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/a_Cancelar'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/i_Activo_far fa-edit_1'))

WebUI.setText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Nueva  Categora_descripcion'), 
    ' NUEVO 12345')

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/button_Guardar'))

WebUI.click(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/button_ok'))

WebUI.closeBrowser()

WebUI.setText(findTestObject('Object Repository/Page_Sistema de Compras e Inventarios/input_Nueva  Categora_descripcion'), 
    'demo uno')

WebUI.closeBrowser()

