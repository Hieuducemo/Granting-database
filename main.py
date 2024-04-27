# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options 
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import json
# import time
# options = Options()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# url = "https://apl.unob.cz/rozvrh/api/read/rozvrh?id=7"
# driver.get(url)
# driver.refresh()
# with open('login_info.txt','r') as file:
#     lines= file.readlines()
#     username=lines[0].split(":")[1].strip()
#     password=lines[1].split(":")[1].strip()
# driver.find_element(By.NAME,"Username").send_keys(username)
# driver.find_element(By.NAME,"Password").send_keys(password)
# driver.find_element(By.NAME,"button").click()
# time.sleep(5)
# data= driver.page_source

# with open("systemdata2.json", "w") as json_file:
#     json.dump(data, json_file,indent=4 )
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import time
from bs4  import BeautifulSoup
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = "https://apl.unob.cz/rozvrh/api/read/rozvrh?id=7"
driver.get(url)
driver.refresh()

# Read username and password from file
with open('login_info.txt', 'r') as file:
    lines = file.readlines()
    username = lines[0].split(":")[1].strip()
    password = lines[1].split(":")[1].strip()

# Fill in login form and submit
driver.find_element(By.NAME, "Username").send_keys(username)
driver.find_element(By.NAME, "Password").send_keys(password)
driver.find_element(By.NAME, "button").click()
time.sleep(5)
data = driver.find_element(By.TAG_NAME, "pre").text
json_data = json.loads(data)
print(json_data)
with open('systemdata2.json','w') as json_file:
    json.dump(json_data, json_file, indent=4)
# Get the page source (HTML content)
# data = driver.page_source
# soup = BeautifulSoup(data, 'html.parser')
# programs = soup.find('pre')
# data = json.loads(soup)
# Write the data into a JSON file
# with open("systemdata2.json", "w") as json_file:
#     # Convert HTML content into JSON string
#     json.dump({"page_source": data}, json_file, indent=4)
driver.quit()
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     driver.quit()
