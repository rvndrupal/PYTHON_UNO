from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://www.goodstartbooks.com/pruebas")

elemento=driver.find_element_by_id("noImportante")

if elemento is not None:
    print("El elemento con id noImportante fue encontrado")
           
driver.quit()