import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def InicioSesion (email, password):

    login_en_pantalla = browser.find_element(By.XPATH, "//*[@id='header']/div[1]/div/div[2]/a").is_displayed()

    if login_en_pantalla == True:
        botonLogin = browser.find_element(By.XPATH, "//*[@id='header']/div[1]/div/div[2]/a")
        botonLogin.click()
        time.sleep(4)

        botonEntrar = browser.find_element(By.XPATH,"//*[@id='vtexIdUI-custom-oauth']")
        botonEntrar.click()
        time.sleep(7)

        ventanas = browser.window_handles
        browser.switch_to.window(ventanas[1])
        time.sleep(5)
        inicioSesion = str(browser.find_element(By.CSS_SELECTOR, "h1").text)
        time.sleep(3)
        print(inicioSesion)

        if inicioSesion != "Ingresa tu correo electrónico para unirte o iniciar sesión.":
            botonContinuarSesion = browser.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/form/div/div[2]/button[1]")
            botonContinuarSesion.click()
            time.sleep(4)
            browser.switch_to.window(ventanas[0])
            time.sleep(4)

        else:
            inputEmail = browser.find_element(By.XPATH, "//*[@id='username']")
            inputEmail.send_keys(email)
            botonContinuar = browser.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/form/div/div[4]/button")
            botonContinuar.click()
            time.sleep(5)

            inputContrasena = browser.find_element(By.XPATH, "//*[@id='password']")
            botonLoggeo = browser.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/form/div/div[2]/button")
            inputContrasena.send_keys(password)
            botonLoggeo.click()
            time.sleep(4)
            browser.switch_to.window(ventanas[0])
            time.sleep(4)

correo = input("Ingrese el email de la cuenta de nike.cl: ")
contraseña = input("Ingrese su contraseña: ")
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

InicioSesion(correo, contraseña)
botonSNKRS = browser.find_element(By.XPATH, "//*[@id='full-menu']/ul/li[6]/a[1]")
botonSNKRS.click()
time.sleep(4)


#botonFuturos = browser.find_element(By.XPATH, "//*[@id='links']/li[3]/a")
#botonFuturos.click()
#time.sleep(4)