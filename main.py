from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://apl.unob.cz/StudijniProgramy/Studium/4/Kyberneticka-bezpecnost")
driver.maximize_window()

programtypes = driver.find_element(By.XPATH,"//span[@class='h2 lead nabidkaH']")
print(programtypes.text)
driver.close()
