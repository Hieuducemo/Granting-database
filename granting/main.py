# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import json
# from bs4 import BeautifulSoup
# import time
# from selenium.webdriver.common.by import By
# from urllib.parse import urlparse
# import uuid

# # Selenium setup
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# url = "https://apl.unob.cz/StudijniProgramy/Studium/4/Cyber-Security?culture=cs-CZ"
# driver.get(url)

# # Wait for a few seconds to ensure the page loads completely
# time.sleep(2)
# program_name = driver.find_element(By.XPATH, "//span[@class='h2 lead nabidkaH']").text
# html_text = driver.page_source
# soup = BeautifulSoup(html_text, "html.parser")

# # Locate and click the link to the English version
# nav_link = driver.find_element(By.CSS_SELECTOR, 'a.nav-link[style*="color:white"][href*="/StudijniProgramy/Studium/4/Kyberneticka-bezpecnost"]')
# driver.execute_script("arguments[0].scrollIntoView(true);", nav_link)  # Scroll into view
# nav_link.click()
# time.sleep(2)  # Wait for the English page to load

# # Get the English page's HTML content
# html_text_eng = driver.page_source
# soup_eng = BeautifulSoup(html_text_eng, "html.parser")
# program_name_eng = driver.find_element(By.XPATH, "//span[@class='h2 lead nabidkaH']").text

# # Close the browser
# driver.quit()

# # Extract data from the original (Czech) page

# # program
# table_data_program = {}
# table_data_program["name"] = program_name
# table_data_program["name_en"]=program_name_eng
# table_data_program["type_id"]= "fd4f2082-9315-11ed-9b95-0242ac110002"
# table_data_program["lastchange"]=""
# table_data_program["id"]= str(uuid.uuid4())

# # Extract subjects from the Czech page
# data_subject = []
# subject_hrefs = []

# subjects = soup.find_all('a', attrs={'target': '_blank'})
# for subject in subjects:
#     subject_name = subject.text.strip()  # Strip whitespace from subject name
#     href = subject['href']
#     # Extract the ID from the href
#     subject_hrefs.append(href)
#     parsed_url = urlparse(href)
#     path_segments = parsed_url.path.split('/')
#     subject_id = path_segments[3]
#     data_subject.append({
#         "id":str(uuid.uuid4()),
#         "name": subject_name,
#         "name_en": "",  # Placeholder for English name
#         "program_id":table_data_program["id"],
#         "lastchange":""
#     })

# with open('subject_href.txt', 'w') as file:
#     for href in subject_hrefs:
#         file.write("https://apl.unob.cz"+href + '\n')

# # Extract subjects from the English page and match them, avoiding duplicates
# existing_names_en = set()
# subjects_eng = soup_eng.find_all('a', attrs={'target': '_blank'})
# for i, subject_eng in enumerate(subjects_eng):
#     subject_name_eng = subject_eng.text.strip()  # Strip whitespace from subject name
#     if i < len(data_subject) and subject_name_eng not in existing_names_en:
#         data_subject[i]["name_en"] = subject_name_eng
#         existing_names_en.add(subject_name_eng)

# # Filter out subjects with empty English names
# filtered_data_subject = [subject for subject in data_subject if subject["name_en"]]

# #semester 
# with open('acclassification.json', 'r', encoding='utf-8') as file:
#     classification_types = json.load(file)

# # Load existing data files
# def load_json(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         return json.load(file)

# program_types = load_json("programtype.json")
# lesson_types = load_json("lessontype.json")
# classification_types = load_json("acclassification.json")
# classification_levels = load_json("acclassificationlevel.json")


# #classification
# data_classification = [] 
# users = load_json("user.json")
# users = [users[0], users[1]]
# order= 0 
# for user in users:
#     order+=1 
#     data_classification.append({
#         "id": str(uuid.uuid4()),
#         "user_id": user["id"],
#         "semester_id": "54cd10b6-9465-45a5-88f1-02c77f8b962b",
#         "classificationlevel_id":"5fae9dd8-b095-11ed-9bd8-0242ac110002",
#         "lastchange":"", 
#         "order": order
#     })
# #topic 
# topic_data =[] 
# topic_data.append({
#     "id":str(uuid.uuid4()),
#     "semester_id":"12472709-8de6-4594-8c2e-24a1eb9993e4",
#     "lastchange":"",
#     "name":"Rozvoj základních pohybových schopností" ,
#     "name_en":"Development of basic physical abilities"
# })
# #lesson
# lesson_data=[]
# lesson_data.append({
#     "id":str(uuid.uuid4()),
#     "topic_id":topic_data[0]["id"],
#     "type_id":"e2b7cfac-95e1-11ed-a1eb-0242ac120002",
#     "lastchange":"",
#     "count":1
# })


# # Write the subjects to a JSON file
# with open("acsubject.json", "w", encoding="utf-8") as json_file:
#     json.dump(filtered_data_subject, json_file, ensure_ascii=False, indent=4)

# # Load classification types from JSON file
# with open('acclassification.json', 'r', encoding='utf-8') as file:
#     classification_types = json.load(file)

# # Load subjects from JSON file
# with open('acsubject.json', 'r', encoding='utf-8') as file:
#     subjects = json.load(file)

# options = Options()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Read the URLs from file
# with open('subject_href.txt', 'r') as file:
#     lines = file.readlines()

# semester_data = []
# order_id_map = {}

# for line in lines:
#     url = line.strip()
#     driver.get(url)
#     html_text = driver.page_source
#     soup = BeautifulSoup(html_text, "html.parser")
#     table = soup.find('table')
#     rows = table.find_all('tr')
    

#         # Get the semester order
#     semester_order_str = rows[12].find_all('td')[1].text
#     semester_order = int(semester_order_str.split('/')[1])

#         # Generate or retrieve unique ID for the order
#     unique_id = str(uuid.uuid4())
#     order_id_map[semester_order] = unique_id

#         # Get the classification text
#     classification_text = rows[10].find_all('td')[1].text.strip()
        
#         # Find the classification ID
#     classification_id = ""
#     for classification in classification_types:
#             if classification['name'] == classification_text:
#                 classification_id = classification['id']
#                 break

#         # Get the semester credit
#     semester_credit = int(rows[11].find_all('td')[1].text)

#         # Get the subject name in English
#     subject_name_eng = driver.find_element(By.XPATH, "//span[@class='h2 lead nabidkaH']").text.strip()

#         # Find the corresponding subject ID
#     subject_id = ""
#     for subject in subjects:
#             if subject['name_en'].strip() == subject_name_eng:
#                 subject_id = subject['id']
#                 break

#         # Append the data
#     semester_data.append({
#             "id": unique_id,
#             "subject_id": subject_id,
#             "classificationtype_id": classification_id,
#             "lastchange": "",
#             "order": semester_order,
#             "credits": semester_credit
#         })
    

# driver.quit()

# # Write the data to a JSON file
# with open("acsemester.json", "w", encoding="utf-8") as json_file:
#     json.dump(semester_data, json_file, ensure_ascii=False, indent=4)

# print("a ok")

# semesters = load_json("acsemester.json")

# # Create the final data dictionary
# data = {
#     "acprograms": [table_data_program],
#     "acsubjects": filtered_data_subject,
#     "acprogramtypes": program_types,
#     "aclessontypes": lesson_types,
#     "acclassificationtypes": classification_types,
#     "acclassificationlevels": classification_levels,
#     "aclesson": lesson_data,
#     "acsemester": semesters,
#     "acclassification": data_classification,
#     "actopic": topic_data
# }

# # Write the complete data to a JSON file
# with open("systemdata2.json", "w", encoding="utf-8") as json_file:
#     json.dump(data, json_file, ensure_ascii=False, indent=4)

# print("Ok!")
import json
import time
import uuid
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def extract_program_data(url):
    driver = initialize_driver()
    driver.get(url)
    time.sleep(2)
    
    program_name = driver.find_element(By.XPATH, "//span[@class='h2 lead nabidkaH']").text
    html_text = driver.page_source
    soup = BeautifulSoup(html_text, "html.parser")
    
    nav_link = driver.find_element(By.CSS_SELECTOR, 'a.nav-link[style*="color:white"][href*="/StudijniProgramy/Studium/4/Kyberneticka-bezpecnost"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", nav_link)
    nav_link.click()
    time.sleep(2)
    
    html_text_eng = driver.page_source
    soup_eng = BeautifulSoup(html_text_eng, "html.parser")
    program_name_eng = driver.find_element(By.XPATH, "//span[@class='h2 lead nabidkaH']").text
    
    driver.quit()
    
    program_data = {
        "name": program_name,
        "name_en": program_name_eng,
        "type_id": "fd4f2082-9315-11ed-9b95-0242ac110002",
        "lastchange": datetime.now().isoformat(),
        "id": str(uuid.uuid4())
    }
    
    return program_data, soup, soup_eng


def extract_subjects(soup, soup_eng, program_id):
    subjects = soup.find_all('a', attrs={'target': '_blank'})
    subjects_eng = soup_eng.find_all('a', attrs={'target': '_blank'})
    
    data_subject = []
    subject_hrefs = []
    existing_names_en = set()
    
    for i, subject in enumerate(subjects):
        subject_name = subject.text.strip()
        href = subject['href']
        subject_hrefs.append(href)
        data_subject.append({
            "id": str(uuid.uuid4()),
            "name": subject_name,
            "name_en": "",
            "program_id": program_id,
            "lastchange": datetime.now().isoformat()
        })
        
    for i, subject_eng in enumerate(subjects_eng):
        subject_name_eng = subject_eng.text.strip()
        if i < len(data_subject) and subject_name_eng not in existing_names_en:
            data_subject[i]["name_en"] = subject_name_eng
            existing_names_en.add(subject_name_eng)
    
    filtered_data_subject = [subject for subject in data_subject if subject["name_en"]]
    
    with open('subject_href.txt', 'w') as file:
        for href in subject_hrefs:
            file.write("https://apl.unob.cz" + href + '\n')
    
    return filtered_data_subject


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def create_classifications(users, semester_id, classification_level_id):
    data_classification = []
    order = 0
    for user in users:
        order += 1
        data_classification.append({
            "id": str(uuid.uuid4()),
            "user_id": user["id"],
            "semester_id": semester_id,
            "classificationlevel_id": classification_level_id,
            "lastchange": datetime.now().isoformat(),
            "order": order
        })
    return data_classification


def create_topics():
    return [{
        "id": str(uuid.uuid4()),
        "semester_id": "12472709-8de6-4594-8c2e-24a1eb9993e4",
        "lastchange": datetime.now().isoformat(),
        "name": "Rozvoj základních pohybových schopností",
        "name_en": "Development of basic physical abilities"
    }]


def create_lessons(topic_id):
    return [{
        "id": str(uuid.uuid4()),
        "topic_id": topic_id,
        "type_id": "e2b7cfac-95e1-11ed-a1eb-0242ac120002",
        "lastchange": datetime.now().isoformat(),
        "count": 1
    }]


def extract_semester_data(driver, lines, subjects, classification_types):
    semester_data = []
    order_id_map = {}
    
    for line in lines:
        url = line.strip()
        driver.get(url)
        html_text = driver.page_source
        soup = BeautifulSoup(html_text, "html.parser")
        table = soup.find('table')
        rows = table.find_all('tr')
        
        semester_order_str = rows[12].find_all('td')[1].text
        semester_order = int(semester_order_str.split('/')[1])
        
        unique_id = str(uuid.uuid4())
        order_id_map[semester_order] = unique_id
        
        classification_text = rows[10].find_all('td')[1].text.strip()
        
        classification_id = ""
        for classification in classification_types:
            if classification['name'] == classification_text:
                classification_id = classification['id']
                break
        
        semester_credit = int(rows[11].find_all('td')[1].text)
        
        subject_name_eng = driver.find_element(By.XPATH, "//span[@class='h2 lead nabidkaH']").text.strip()
        
        subject_id = ""
        for subject in subjects:
            if subject['name_en'].strip() == subject_name_eng:
                subject_id = subject['id']
                break
        
        semester_data.append({
            "id": unique_id,
            "subject_id": subject_id,
            "classificationtype_id": classification_id,
            "lastchange": datetime.now().isoformat(),
            "order": semester_order,
            "credits": semester_credit
        })
    
    return semester_data


def main():
    url = "https://apl.unob.cz/StudijniProgramy/Studium/4/Cyber-Security?culture=cs-CZ"
    program_data, soup, soup_eng = extract_program_data(url)
    
    filtered_data_subject = extract_subjects(soup, soup_eng, program_data["id"])
    
    with open("acsubject.json", "w", encoding="utf-8") as json_file:
        json.dump(filtered_data_subject, json_file, ensure_ascii=False, indent=4)
    
    program_types = load_json("programtype.json")
    lesson_types = load_json("lessontype.json")
    classification_types = load_json("acclassification.json")
    classification_levels = load_json("acclassificationlevel.json")
    users = load_json("user.json")[:2]
    
    data_classification = create_classifications(users, "54cd10b6-9465-45a5-88f1-02c77f8b962b", "5fae9dd8-b095-11ed-9bd8-0242ac110002")
    
    topic_data = create_topics()
    lesson_data = create_lessons(topic_data[0]["id"])
    
    with open('subject_href.txt', 'r') as file:
        lines = file.readlines()
    
    driver = initialize_driver()
    semesters = extract_semester_data(driver, lines, filtered_data_subject, classification_types)
    driver.quit()
    
    with open("acsemester.json", "w", encoding="utf-8") as json_file:
        json.dump(semesters, json_file, ensure_ascii=False, indent=4)
    
    data = {
        "acprograms": [program_data],
        "acsubjects": filtered_data_subject,
        "acprogramtypes": program_types,
        "aclessontypes": lesson_types,
        "acclassificationtypes": classification_types,
        "acclassificationlevels": classification_levels,
        "aclesson": lesson_data,
        "acsemester": semesters,
        "acclassification": data_classification,
        "actopic": topic_data
    }
    
    with open("systemdata2.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print("Ok!")


if __name__ == "__main__":
    main()
