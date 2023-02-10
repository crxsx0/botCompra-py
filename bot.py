from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import os
import pandas as reader

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\\chromedriver.exe")
#browser = webdriver.Chrome()


#file = 'data.xlsx'
#data = reader.read_excel(file)

#e_mail = str("cr.hachim2.0@gmail.com") #str(data.iloc[0,3])
#contra = str("$Xrd3000$")#str(data.iloc[0,4])
#rows = len(data)
#choice = data.iloc[0,2]

#def entrar():
#aqui entramos para logearnos
driver.get("https://bold.cl/login")
time.sleep(7)

#nos rellena el correo
email = driver.find_element("xpath","/html/body/app-root/ynk-custom-storefront/div/main/cx-page-layout/cx-page-slot[1]/ynk-custom-login-form/form/div[1]/label/input")
email.send_keys("cris_arredondo26@hotmail.com")

#nos rellena la contra
constrasena = driver.find_element("xpath", "/html/body/app-root/ynk-custom-storefront/div/main/cx-page-layout/cx-page-slot[1]/ynk-custom-login-form/form/div[2]/label/input")
contra = str("Canchis9!!")
constrasena.send_keys(contra)
time.sleep(7)

submit = driver.find_element("xpath","/html/body/app-root/ynk-custom-storefront/div/main/cx-page-layout/cx-page-slot[1]/ynk-custom-login-form/form/button")
submit.click()
time.sleep(7)

driver.get("https://bold.cl/Colecciones/Air-Max-90-Nike/ZAPATILLA-NIKE-WMNS-AIR-MAX-90-SE-%27SIEMPRE-FAMILIA%27-BLACK-GREEN-NOISE-SAIL/p/NIDO2154010080")
time.sleep(5)
agregarCarro = driver.find_element("xpath", "/html/body/app-root/ynk-custom-storefront/div/main/cx-page-layout/cx-page-slot[1]/ynk-custom-add-to-cart/form/button")
agregarCarro.click()
time.sleep(7)

carro = driver.find_element("xpath", "/html/body/ngb-modal-window/div/div/ynk-custom-added-to-cart-dialog/div/div[3]/div/div[3]/div[2]/a[1]")
carro.click()
time.sleep(10)

finalizarCompra = driver.find_element("xpath", "/html/body/app-root/ynk-custom-storefront/div/main/cx-page-layout/cx-page-slot[2]/ynk-custom-cart-totals/div/button[2]")
finalizarCompra.click()
time.sleep(4)
