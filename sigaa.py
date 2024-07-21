from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

##Login Informations
username='222025100'
password='Neves2906'

##Using Chrome
driver=webdriver.Chrome()
driver.get('https://autenticacao.unb.br/sso-server/login?service=https://sig.unb.br/sigaa/login/cas')
try:
    initial=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"username")))
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.NAME,"submit").click()
    second=WebDriverWait(driver,50).until(EC.presence_of_element_located((By.ID,"conteudo")))
    ensino=driver.find_element(By.CLASS_NAME,"ThemeOfficeMainItem")
    AC(driver).move_to_element(ensino).click().perform()
    
finally:
    driver.quit()
