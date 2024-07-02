
# import requests
# import json
# import os

# # Define the path to the JSON file
# script_dir = os.path.dirname(__file__)
# json_file_path = os.path.join(script_dir, 'systemdata2.json')
# # json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'systemdata2.json')

# # Print the file path for debugging
# print("JSON file path:", json_file_path)

# # Print the contents of the directory
# print("Contents of directory:", os.listdir(os.path.dirname(json_file_path)))

# # Load JSON data from the file
# with open(json_file_path, encoding='utf-8') as json_file:
#     data = json.load(json_file)

# # Define the GraphQL endpoint
# url = 'http://localhost:5000/graphql'

# # Define the GraphQL mutations
# mutation_acprogram = '''
# mutation($id: ID!, $name: String!, $nameEn: String!, $typeId: String!, $lastchange: String!) {
#   createAcprogram(id: $id, name: $name, nameEn: $nameEn, typeId: $typeId, lastchange: $lastchange) {
#     acprogram {
#       id
#       name
#       nameEn
#       typeId
#       lastchange
#     }
#   }
# }
# '''

# mutation_acsubject = '''
# mutation($id: ID!, $name: String!, $nameEn: String!, $programId: String!, $lastchange: String!) {
#   createAcsubject(id: $id, name: $name, nameEn: $nameEn, programId: $programId, lastchange: $lastchange) {
#     acsubject {
#       id
#       name
#       nameEn
#       programId
#       lastchange
#     }
#   }
# }
# '''
# mutation_aclessontype = '''
# mutation($id: ID!, $name: String!, $nameEn: String!) {
#   createAclessontype(id: $id, name: $name, nameEn: $nameEn) {
#     aclessontype {
#       id
#       name
#       nameEn
#     }
#   }
# }
# '''

# mutation_aclesson = '''
# mutation($id: ID!, $topicId: ID!, $typeId: ID!, $lastchange: String!, $count: Int!) {
#   createAclesson(id: $id, topicId: $topicId, typeId: $typeId, lastchange: $lastchange, count: $count) {
#     aclesson {
#       id
#       topicId
#       typeId
#       lastchange
#       count
#     }
#   }
# }
# '''

# mutation_actopic = '''
# mutation($id: ID!, $semesterId: ID!, $lastchange: String!, $name: String!, $nameEn: String!) {
#   createActopic(id: $id, semesterId: $semesterId, lastchange: $lastchange, name: $name, nameEn: $nameEn) {
#     actopic {
#       id
#       semesterId
#       lastchange
#       name
#       nameEn
#     }
#   }
# }
# '''

# mutation_acclassification = '''
# mutation($id: ID!, $userId: ID!, $semesterId: ID!, $classificationLevelId: ID!, $lastchange: String!, $order: Int!) {
#   createAcclassification(id: $id, userId: $userId, semesterId: $semesterId, classificationLevelId: $classificationLevelId, lastchange: $lastchange, order: $order) {
#     acclassification {
#       id
#       userId
#       semesterId
#       classificationLevelId
#       lastchange
#       order
#     }
#   }
# }
# '''

# mutation_acprogramtype = '''
# mutation($id: ID!, $name: String!, $nameEn: String!, $titleId: ID!, $formId: ID!, $languageId: ID!, $levelId: ID!) {
#   createAcprogramtype(id: $id, name: $name, nameEn: $nameEn, titleId: $titleId, formId: $formId, languageId: $languageId, levelId: $levelId) {
#     acprogramtype {
#       id
#       name
#       nameEn
#       titleId
#       formId
#       languageId
#       levelId
#     }
#   }
# }
# '''

# mutation_acsemester = '''
# mutation($id: ID!, $subjectId: ID!, $classificationtypeId: ID!, $lastchange: String!, $order: Int!, $credits: Int!) {
#   createAcsemester(id: $id, subjectId: $subjectId, classificationtypeId: $classificationtypeId, lastchange: $lastchange, order: $order, credits: $credits) {
#     acsemester {
#       id
#       subjectId
#       classificationtypeId
#       lastchange
#       order
#       credits
#     }
#   }
# }
# '''

# mutation_acclassificationtype = '''
# mutation($id: ID!, $name: String!, $nameEn: String!) {
#   createAcclassificationtype(id: $id, name: $name, nameEn: $nameEn) {
#     acclassificationtype {
#       id
#       name
#       nameEn
#     }
#   }
# }
# '''

# mutation_acclassificationlevel = '''
# mutation($id: ID!, $name: String!, $nameEn: String!) {
#   createAcclassificationlevel(id: $id, name: $name, nameEn: $nameEn) {
#     acclassificationlevel {
#       id
#       name
#       nameEn
#     }
#   }
# }
# '''

# # Function to send mutation request
# def send_mutation(url, mutation, variables):
#     response = requests.post(url, json={'query': mutation, 'variables': variables})
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Failed to execute mutation: {response.status_code}, {response.text}")

# # Send acprograms data
# for program in data['acprograms']:
#     variables = {
#         'id': program['id'],
#         'name': program['name'],
#         'nameEn': program['name_en'],
#         'typeId': program['type_id'],
#         'lastchange': program['lastchange']
#     }
#     result = send_mutation(url, mutation_acprogram, variables)
#     print('AcProgram imported successfully:', result)

# # Send acsubjects data
# for subject in data['acsubjects']:
#     variables = {
#         'id': subject['id'],
#         'name': subject['name'],
#         'nameEn': subject['name_en'],
#         'programId': subject['program_id'],
#         'lastchange': subject['lastchange']
#     }
#     result = send_mutation(url, mutation_acsubject, variables)
#     print('AcSubject imported successfully:', result)

# # Send aclessontypes data
# for lessontype in data['aclessontypes']:
#     variables = {
#         'id': lessontype['id'],
#         'name': lessontype['name'],
#         'nameEn': lessontype['name_en']
#     }
#     result = send_mutation(url, mutation_aclessontype, variables)
#     print('AcLessonType imported successfully:', result)
    
# # Send aclessons data
# for lesson in data['aclesson']:
#     variables = {
#         'id': lesson['id'],
#         'topicId': lesson['topic_id'],
#         'typeId': lesson['type_id'],
#         'lastchange': lesson['lastchange'],
#         'count': lesson['count']
#     }
#     result = send_mutation(url, mutation_aclesson, variables)
#     print('AcLesson imported successfully:', result)

# # Send actopic data
# for topic in data['actopic']:
#     variables = {
#         'id': topic['id'],
#         'semesterId': topic['semester_id'],
#         'lastchange': topic['lastchange'],
#         'name': topic['name'],
#         'nameEn': topic['name_en']
#     }
#     result = send_mutation(url, mutation_actopic, variables)
#     print('AcTopic imported successfully:', result)

# # Send acclassifications data
# for classification in data['acclassification']:
#     variables = {
#         'id': classification['id'],
#         'userId': classification['user_id'],
#         'semesterId': classification['semester_id'],
#         'classificationLevelId': classification['classificationlevel_id'],
#         'lastchange': classification['lastchange'],
#         'order': classification['order']
#     }
#     result = send_mutation(url, mutation_acclassification, variables)
#     print('AcClassification imported successfully:', result)
    
# for programtype in data['acprogramtypes']:
#     variables = {
#         'id': programtype['id'],
#         'name': programtype['name'],
#         'nameEn': programtype['name_en'],
#         'titleId': programtype['title_id'],
#         'formId': programtype['form_id'],
#         'languageId': programtype['language_id'],
#         'levelId': programtype['level_id']
#     }
#     result = send_mutation(url, mutation_acprogramtype, variables)
#     print('AcProgramtypes imported successfully:', result)

# for semester in data['acsemester']:
#     variables = {
#         'id': semester['id'],
#         'subjectId': semester['subject_id'],
#         'classificationtypeId': semester['classificationtype_id'],
#         'lastchange': semester['lastchange'],
#         'order': semester['order'],
#         'credits': semester['credits']
#     }
#     result = send_mutation(url, mutation_acsemester, variables)
#     print('AcSemesters imported successfully:', result)
    
# for classificationtype in data['acclassificationtypes']:
#     variables = {
#         'id': classificationtype['id'],
#         'name': classificationtype['name'],
#         'nameEn': classificationtype['name_en'],
#     }
#     result = send_mutation(url, mutation_acclassificationtype, variables)
#     print('AcClassificationtypes imported successfully:', result)
    
# for classificationlevel in data['acclassificationlevels']:
#     variables = {
#         'id': classificationlevel['id'],
#         'name': classificationlevel['name'],
#         'nameEn': classificationlevel['name_en'],
#     }
#     result = send_mutation(url, mutation_acclassificationlevel, variables)
#     print('AcClassificationlevels imported successfully:', result)

import requests
import json
import os

# Define the path to the JSON file
script_dir = os.path.dirname(__file__)
json_file_path = os.path.join(script_dir, 'systemdata2.json')

# Print the file path for debugging
print("JSON file path:", json_file_path)

# Print the contents of the directory
print("Contents of directory:", os.listdir(os.path.dirname(json_file_path)))

# Load JSON data from the file
with open(json_file_path, encoding='utf-8') as json_file:
    data = json.load(json_file)

# Define the GraphQL endpoint
url = 'http://localhost:5000/graphql'

# Define the GraphQL mutations
mutation_acprogram = '''
mutation($id: ID!, $name: String!, $nameEn: String!, $typeId: String!, $lastchange: String!) {
  createAcprogram(id: $id, name: $name, nameEn: $nameEn, typeId: $typeId, lastchange: $lastchange) {
    acprogram {
      id
      name
      nameEn
      typeId
      lastchange
    }
  }
}
'''

mutation_acsubject = '''
mutation($id: ID!, $name: String!, $nameEn: String!, $programId: String!, $lastchange: String!) {
  createAcsubject(id: $id, name: $name, nameEn: $nameEn, programId: $programId, lastchange: $lastchange) {
    acsubject {
      id
      name
      nameEn
      programId
      lastchange
    }
  }
}
'''

mutation_aclessontype = '''
mutation($id: ID!, $name: String!, $nameEn: String!) {
  createAclessontype(id: $id, name: $name, nameEn: $nameEn) {
    aclessontype {
      id
      name
      nameEn
    }
  }
}
'''

mutation_aclesson = '''
mutation($id: ID!, $topicId: ID!, $typeId: ID!, $lastchange: String!, $count: Int!) {
  createAclesson(id: $id, topicId: $topicId, typeId: $typeId, lastchange: $lastchange, count: $count) {
    aclesson {
      id
      topicId
      typeId
      lastchange
      count
    }
  }
}
'''

mutation_actopic = '''
mutation($id: ID!, $semesterId: ID!, $lastchange: String!, $name: String!, $nameEn: String!) {
  createActopic(id: $id, semesterId: $semesterId, lastchange: $lastchange, name: $name, nameEn: $nameEn) {
    actopic {
      id
      semesterId
      lastchange
      name
      nameEn
    }
  }
}
'''

mutation_acclassification = '''
mutation($id: ID!, $userId: ID!, $semesterId: ID!, $classificationLevelId: ID!, $lastchange: String!, $order: Int!) {
  createAcclassification(id: $id, userId: $userId, semesterId: $semesterId, classificationLevelId: $classificationLevelId, lastchange: $lastchange, order: $order) {
    acclassification {
      id
      userId
      semesterId
      classificationLevelId
      lastchange
      order
    }
  }
}
'''

mutation_acprogramtype = '''
mutation($id: ID!, $name: String!, $nameEn: String!, $titleId: ID!, $formId: ID!, $languageId: ID!, $levelId: ID!) {
  createAcprogramtype(id: $id, name: $name, nameEn: $nameEn, titleId: $titleId, formId: $formId, languageId: $languageId, levelId: $levelId) {
    acprogramtype {
      id
      name
      nameEn
      titleId
      formId
      languageId
      levelId
    }
  }
}
'''

mutation_acsemester = '''
mutation($id: ID!, $subjectId: ID!, $classificationtypeId: ID!, $lastchange: String!, $order: Int!, $credits: Int!) {
  createAcsemester(id: $id, subjectId: $subjectId, classificationtypeId: $classificationtypeId, lastchange: $lastchange, order: $order, credits: $credits) {
    acsemester {
      id
      subjectId
      classificationtypeId
      lastchange
      order
      credits
    }
  }
}
'''

mutation_acclassificationtype = '''
mutation($id: ID!, $name: String!, $nameEn: String!) {
  createAcclassificationtype(id: $id, name: $name, nameEn: $nameEn) {
    acclassificationtype {
      id
      name
      nameEn
    }
  }
}
'''

mutation_acclassificationlevel = '''
mutation($id: ID!, $name: String!, $nameEn: String!) {
  createAcclassificationlevel(id: $id, name: $name, nameEn: $nameEn) {
    acclassificationlevel {
      id
      name
      nameEn
    }
  }
}
'''

# Function to send mutation request
def send_mutation(url, mutation, variables):
    response = requests.post(url, json={'query': mutation, 'variables': variables})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to execute mutation: {response.status_code}, {response.text}")

# Function to import data
def import_data(data, mutation, entity_name):
    for item in data:
        result = send_mutation(url, mutation, item)
        print(f'{entity_name} imported successfully:', result)

# Prepare data for import
acprograms_data = [
    {
        'id': program['id'],
        'name': program['name'],
        'nameEn': program['name_en'],
        'typeId': program['type_id'],
        'lastchange': program['lastchange']
    }
    for program in data['acprograms']
]

acsubjects_data = [
    {
        'id': subject['id'],
        'name': subject['name'],
        'nameEn': subject['name_en'],
        'programId': subject['program_id'],
        'lastchange': subject['lastchange']
    }
    for subject in data['acsubjects']
]

aclessontypes_data = [
    {
        'id': lessontype['id'],
        'name': lessontype['name'],
        'nameEn': lessontype['name_en']
    }
    for lessontype in data['aclessontypes']
]

aclesson_data = [
    {
        'id': lesson['id'],
        'topicId': lesson['topic_id'],
        'typeId': lesson['type_id'],
        'lastchange': lesson['lastchange'],
        'count': lesson['count']
    }
    for lesson in data['aclesson']
]

actopic_data = [
    {
        'id': topic['id'],
        'semesterId': topic['semester_id'],
        'lastchange': topic['lastchange'],
        'name': topic['name'],
        'nameEn': topic['name_en']
    }
    for topic in data['actopic']
]

acclassifications_data = [
    {
        'id': classification['id'],
        'userId': classification['user_id'],
        'semesterId': classification['semester_id'],
        'classificationLevelId': classification['classificationlevel_id'],
        'lastchange': classification['lastchange'],
        'order': classification['order']
    }
    for classification in data['acclassification']
]

acprogramtypes_data = [
    {
        'id': programtype['id'],
        'name': programtype['name'],
        'nameEn': programtype['name_en'],
        'titleId': programtype['title_id'],
        'formId': programtype['form_id'],
        'languageId': programtype['language_id'],
        'levelId': programtype['level_id']
    }
    for programtype in data['acprogramtypes']
]

acsemester_data = [
    {
        'id': semester['id'],
        'subjectId': semester['subject_id'],
        'classificationtypeId': semester['classificationtype_id'],
        'lastchange': semester['lastchange'],
        'order': semester['order'],
        'credits': semester['credits']
    }
    for semester in data['acsemester']
]

acclassificationtypes_data = [
    {
        'id': classificationtype['id'],
        'name': classificationtype['name'],
        'nameEn': classificationtype['name_en']
    }
    for classificationtype in data['acclassificationtypes']
]

acclassificationlevels_data = [
    {
        'id': classificationlevel['id'],
        'name': classificationlevel['name'],
        'nameEn': classificationlevel['name_en']
    }
    for classificationlevel in data['acclassificationlevels']
]

# Import all data
def import_datas():
  import_data(acprograms_data, mutation_acprogram, 'AcProgram')
  import_data(acsubjects_data, mutation_acsubject, 'AcSubject')
  import_data(aclessontypes_data, mutation_aclessontype, 'AcLessonType')
  import_data(aclesson_data, mutation_aclesson, 'AcLesson')
  import_data(actopic_data, mutation_actopic, 'AcTopic')
  import_data(acclassifications_data, mutation_acclassification, 'AcClassification')
  import_data(acprogramtypes_data, mutation_acprogramtype, 'AcProgramType')
  import_data(acsemester_data, mutation_acsemester, 'AcSemester')
  import_data(acclassificationtypes_data, mutation_acclassificationtype, 'AcClassificationType')
  import_data(acclassificationlevels_data, mutation_acclassificationlevel, 'AcClassificationLevel')
