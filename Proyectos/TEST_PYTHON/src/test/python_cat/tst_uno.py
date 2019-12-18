# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://localhost:8000/login/")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("juan")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Bienvenido de Nuevo!'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Este campo es obligatorio.'])[2]/following::button[1]").click()
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("paco")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("paco")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Este campo es obligatorio.'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='×'])[2]/following::button[1]").click()
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("rodrigo")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("rorro131319+")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Bienvenido de Nuevo!'])[1]/following::button[1]").click()
        driver.find_element_by_link_text(u"Catálogos").click()
        driver.find_element_by_link_text("Categorias").click()
        driver.find_element_by_xpath("//a[@id='dropdownMenuLink']/i").click()
        driver.find_element_by_link_text("Nueva").click()
        driver.find_element_by_id("id_descripcion").click()
        driver.find_element_by_id("id_descripcion").clear()
        driver.find_element_by_id("id_descripcion").send_keys("nuevo123")
        driver.find_element_by_id("id_estado").click()
        driver.find_element_by_link_text("Cancelar").click()
        driver.find_element_by_xpath("//a[@id='dropdownMenuLink']/i").click()
        driver.find_element_by_link_text("Nueva").click()
        driver.find_element_by_id("id_descripcion").click()
        driver.find_element_by_id("id_descripcion").clear()
        driver.find_element_by_id("id_descripcion").send_keys("nuevo9123")
        driver.find_element_by_id("id_estado").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Estado'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Categoria Creada Satisfactoriamente'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        driver.find_element_by_xpath("//input[@type='search']").clear()
        driver.find_element_by_xpath("//input[@type='search']").send_keys("nuevo")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Activo'])[2]/following::td[6]").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        driver.find_element_by_xpath("//input[@type='search']").click()
        driver.find_element_by_xpath("//input[@type='search']").clear()
        driver.find_element_by_xpath("//input[@type='search']").send_keys("")
        driver.find_element_by_xpath("(//a[@id='cat_edit']/i)[4]").click()
        driver.find_element_by_id("id_descripcion").click()
        driver.find_element_by_id("id_descripcion").clear()
        driver.find_element_by_id("id_descripcion").send_keys("NUEVO91235")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Estado'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Categoria Editada Satisfactoriamente'])[1]/following::button[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
