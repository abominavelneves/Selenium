from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

##Login Informations
print('Username: ')
username=input()
print('Password: ')
password=input()
print('Options: ')
print('1.Regular \n2.Extraordinary \n3.Summer Classes')
option=int(input())

##Using Chrome
driver=webdriver.Chrome()
driver.get('https://autenticacao.unb.br/sso-server/login?service=https://sig.unb.br/sigaa/login/cas')
driver.maximize_window()
try:
    initial=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"username")))
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.NAME,"submit").click()
    second=WebDriverWait(driver,50).until(EC.presence_of_element_located((By.ID,"conteudo")))
    ensino=driver.find_element(By.CLASS_NAME,"ThemeOfficeMainItem")
    if option==1:
        AC(driver).move_to_element(ensino).click().move_to_element_with_offset(ensino,0,250).click().move_by_offset(390,0).click().perform()

finally:
    WebDriverWait(driver,10)
    driver.quit()
