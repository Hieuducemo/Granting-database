from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager

options= Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://apl.unob.cz/StudijniProgramy/Studium/4/Kyberneticka-bezpecnost")