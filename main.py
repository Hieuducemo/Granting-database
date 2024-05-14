from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import json
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = "https://apl.unob.cz/StudijniProgramy/Studium/4/Kyberneticka-bezpecnost"
driver.get(url)

# Wait for a few seconds to ensure page loads completely
time.sleep(5)
program_name = driver.find_element(By.XPATH,"//span[@class='h2 lead nabidkaH']").text
html_text = driver.page_source

soup = BeautifulSoup(html_text, "html.parser")

# Close the browser
driver.quit()

myTable = soup.find('table',{'class':"table table-sm studijniProgramTable"})

table_data = {}
table_data["name"] = program_name

for row in myTable.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 2:
        key = cells[0].get_text(strip=True)
        value = cells[1].get_text(strip=True)
        table_data[key] = value
data={
    "acprograms":table_data
}
# Write the data to a JSON file
with open("systemdata2.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data written to systemdata2.json successfully!")
# print(soup)
