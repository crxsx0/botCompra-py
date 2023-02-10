import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Open Browser
options = uc.ChromeOptions()
options.add_argument("--user-data-dir = /User Data")
options.add_argument('--profile-directory=Default')
browser = uc.Chrome(options=options)

browser.get("https://www.nike.cl/")
time.sleep(4)

#botonCerrarpopUp = browser.find_element(By.XPATH, "//*[@id='home-content']/div/div[1]/div/h3")
#botonCerrarpopUp.click()
#time.sleep(4)

botonSNKRS = browser.find_element(By.XPATH, "//*[@id='full-menu']/ul/li[6]/a[1]")
botonSNKRS.click()
time.sleep(4)

#botonFuturos = browser.find_element(By.XPATH, "//*[@id='links']/li[3]/a")
#botonFuturos.click()
#time.sleep(4)

botonDisponibles = browser.find_element(By.XPATH, "//*[@id='links']/li[2]/a")
botonDisponibles.click()
time.sleep(4)

comprarZapatilla = browser.find_element(By.XPATH, "//*[@id='product-4578']/div[2]/a")
comprarZapatilla.click()
time.sleep(7)

tallaZapatilla = browser.find_element(By.XPATH, "//*[@id='product-page']/div[6]/div[1]/div/div[2]/div[5]/div[2]/ul[1]/li/span/label[2]")
tallaZapatilla.click()
time.sleep(4)

botonComprar = browser.find_element(By.XPATH, "//*[@id='product-page']/div[6]/div[1]/div/div[2]/div[6]/a")
botonComprar.click()
time.sleep(4)

botonEntrar = browser.find_element(By.XPATH,"//*[@id='vtexIdUI-custom-oauth']")
botonEntrar.click()
time.sleep(4)

ventanas = browser.window_handles
browser.switch_to.window(ventanas[1])

inputEmail = browser.find_element(By.XPATH, "//*[@id='username']")
inputEmail.send_keys("cr.hachim2.0@gmail.com")
botonContinuar = browser.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/form/div/div[4]/button")
botonContinuar.click()
time.sleep(60)

inputContrasena = browser.find_element(By.XPATH, "//*[@id='password']")
botonLoggeo = browser.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/form/div/div[2]/button")
inputContrasena.send_keys("$Xrd3000$")
botonLoggeo.click()
time.sleep(4)
browser.switch_to.window(ventanas[0])
time.sleep(10000)