

class Buscar:
    def __init__(self,myDriver):
        self.driver=myDriver
        
    def bus_x(self, XPATH):
        elements = self.driver.find_element_by_xpath(XPATH)
        print("Xpath_Elements: Se interactuo con el elemento " + XPATH)
        return elements 
    
    def bus_id(self, ID):
        elements = self.driver.find_element_by_id(ID)
        print("Xpath_Elements: Se interactuo con el elemento " + ID)
        return elements 

    def bus_n(self, NAME):
        elements = self.driver.find_element_by_name(NAME)
        print("Xpath_Elements: Se interactuo con el elemento " + NAME)
        return elements   