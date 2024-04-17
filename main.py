from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://apl.unob.cz/StudijniProgramy/Studium/4/Kyberneticka-bezpecnost")
driver.maximize_window()

programs = driver.find_element(By.XPATH,"//span[@class='h2 lead nabidkaH']")
program_text=programs.text
program_table =driver.find_element(By.XPATH,"//table[@class='table table-sm studijniProgramTable']")
program_table_text = program_table.text
data = {"acprograms": program_text,
        "acprogramtypes":program_table_text}

# Write the data into the JSON file
with open("systemdata2.json", "w") as json_file:
    json.dump(data, json_file)

driver.close()