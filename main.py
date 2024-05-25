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

# Selenium setup
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = "https://apl.unob.cz/StudijniProgramy/Studium/4/Cyber-Security?culture=cs-CZ"
driver.get(url)

# Wait for a few seconds to ensure the page loads completely
time.sleep(2)
program_name = driver.find_element(By.XPATH, "//span[@class='h2 lead nabidkaH']").text
html_text = driver.page_source
soup = BeautifulSoup(html_text, "html.parser")

# Locate and click the link to the English version
nav_link = driver.find_element(By.CSS_SELECTOR, 'a.nav-link[style*="color:white"][href*="/StudijniProgramy/Studium/4/Kyberneticka-bezpecnost"]')
driver.execute_script("arguments[0].scrollIntoView(true);", nav_link)  # Scroll into view
nav_link.click()
time.sleep(2)  # Wait for the English page to load

# Get the English page's HTML content
html_text_eng = driver.page_source
soup_eng = BeautifulSoup(html_text_eng, "html.parser")
program_name_eng = driver.find_element(By.XPATH, "//span[@class='h2 lead nabidkaH']").text

# Close the browser
driver.quit()

# Extract data from the original (Czech) page

# program
table_data_program = {}
table_data_program["name"] = program_name
table_data_program["name_en"]=program_name_eng
table_data_program["type_id"]= "fd4f2082-9315-11ed-9b95-0242ac110002"
table_data_program["lastchange"]=""
parsed_url = urlparse(url)
path_segments = parsed_url.path.split('/')
program_id = path_segments[3]
table_data_program["id"]= program_id

# Extract subjects from the Czech page
data_subject = []
subject_hrefs = []

subjects = soup.find_all('a', attrs={'target': '_blank'})
for subject in subjects:
    subject_name = subject.text.strip()  # Strip whitespace from subject name
    href = subject['href']
    # Extract the ID from the href
    subject_hrefs.append(href)
    parsed_url = urlparse(href)
    path_segments = parsed_url.path.split('/')
    subject_id = path_segments[3]
    data_subject.append({
        "id":str(uuid.uuid4()),
        "name": subject_name,
        "name_en": "",  # Placeholder for English name
        "program_id":program_id,
        "lastchange":""
    })

with open('subject_href.txt', 'w') as file:
    for href in subject_hrefs:
        file.write("https://apl.unob.cz"+href + '\n')

# Extract subjects from the English page and match them, avoiding duplicates
existing_names_en = set()
subjects_eng = soup_eng.find_all('a', attrs={'target': '_blank'})
for i, subject_eng in enumerate(subjects_eng):
    subject_name_eng = subject_eng.text.strip()  # Strip whitespace from subject name
    if i < len(data_subject) and subject_name_eng not in existing_names_en:
        data_subject[i]["name_en"] = subject_name_eng
        existing_names_en.add(subject_name_eng)

# Filter out subjects with empty English names
filtered_data_subject = [subject for subject in data_subject if subject["name_en"]]

# Load existing data files
def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

program_types = load_json("programtype.json")
lesson_types = load_json("lessontype.json")
classification_types = load_json("acclassification.json")
classification_levels = load_json("acclassificationlevel.json")
semesters = load_json("acsemester.json")

#classification
data_classification = [] 
users = load_json("user.json")
users = [users[0], users[1]]
order= 0 
for user in users:
    order+=1 
    data_classification.append({
        "id": str(uuid.uuid4()),
        "user_id": user["id"],
        "semester_id": "54cd10b6-9465-45a5-88f1-02c77f8b962b",
        "classificationlevel_id":"5fae9dd8-b095-11ed-9bd8-0242ac110002",
        "lastchange":"", 
        "order": order
    })


# Create the final data dictionary
data = {
    "acprograms": [table_data_program],
    "acsubjects": filtered_data_subject,
    "acprogramtypes": program_types,
    "aclessontypes": lesson_types,
    "acclassificationtypes": classification_types,
    "acclassificationlevels": classification_levels,
    "aclesson": "",
    "acsemester": semesters,
    "acclassification": data_classification,
    "actopic": ""
}

# Write the subjects to a JSON file
with open("acsubject.json", "w", encoding="utf-8") as json_file:
    json.dump(filtered_data_subject, json_file, ensure_ascii=False, indent=4)

# Write the complete data to a JSON file
with open("systemdata2.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Ok!")
