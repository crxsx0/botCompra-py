import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Open Browser
options = uc.ChromeOptions()
options.add_argument("--user-data-dir = C:/Users/cris_/Documents/botCompra-py/User Data/")
options.add_argument('--profile-directory=Default')
browser = uc.Chrome(options=options)

browser.get("https://www.google.com/?hl=es")
time.sleep(4)