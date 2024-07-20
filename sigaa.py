from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##Login Informations
username='222025100'
password='Neves2906'

driver=webdriver.Chrome()
driver.get('https://autenticacao.unb.br/sso-server/login?service=https://sig.unb.br/sigaa/login/cas')
try:
    initial=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"username")))
finally:
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.NAME,"submit").click()
    try:
        second=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"menu:form_menu_discente")))
    finally:
        driver.find_element(By.CLASS_NAME,"ThemeOfficeMainItem").click()