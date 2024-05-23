from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import uuid

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver.get(url)
with open('subject_href.txt','r') as file:
    lines = file.readlines()

semester_data = []
order_id_map = {}

for line in lines:
    url = line
    driver.get(url)
    html_text = driver.page_source 
    soup = BeautifulSoup(html_text,"html.parser")
    table = soup.find('table')
    rows = table.find_all('tr')
    semester_order_str = rows[12].find_all('td')[1].text
    # Parse the order string to get the integer
    semester_order = int(semester_order_str.split('/')[1])
    
    # Check if the order is already in the map
    if semester_order in order_id_map:
        unique_id = order_id_map[semester_order]
    else:
        # Generate a new UUID for the order
        unique_id = str(uuid.uuid4())
        order_id_map[semester_order] = unique_id
        
    semester_data.append({
        "id": unique_id, 
        "subject_id":"",
        "classificationtype_id":"",
        "lastchange":"",
        "order": semester_order,
        "credits":""
    }) 

driver.quit()

with open("acsemester.json", "w", encoding="utf-8") as json_file:
    json.dump(semester_data, json_file, ensure_ascii=False, indent=4)

print("a ok")
