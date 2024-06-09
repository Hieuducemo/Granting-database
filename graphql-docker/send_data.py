## import json
# import os

# # Define the path to the JSON file
# json_file_path = os.path.join('D:\\Granting-database', 'systemdata2.json')

# # Load JSON data from the file
# with open(json_file_path,encoding='utf-8') as json_file:
#     data = json.load(json_file)

# # Define the GraphQL endpoint
# url = 'http://localhost:5000/graphql'

# # Define the GraphQL mutations
# mutation_acprogram = '''
# mutation($id: ID!, $name: String!, $nameEn: String!, $typeId: String!, $lastchange: String!) {
#   createAcProgram(id: $id, name: $name, nameEn: $nameEn, typeId: $typeId, lastchange: $lastchange) {
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
#   createAcSubject(id: $id, name: $name, nameEn: $nameEn, programId: $programId, lastchange: $lastchange) {
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
#         'nameEn': program['name_en'],  # Use camelCase
#         'typeId': program['type_id'],  # Use camelCase
#         'lastchange': program['lastchange']
#     }
#     result = send_mutation(url, mutation_acprogram, variables)
#     print('AcProgram imported successfully:', result)

# # Send acsubjects data
# for subject in data['acsubjects']:
#     variables = {
#         'id': subject['id'],
#         'name': subject['name'],
#         'nameEn': subject['name_en'],  # Use camelCase
#         'programId': subject['program_id'],  # Use camelCase
#         'lastchange': subject['lastchange']
#     }
#     result = send_mutation(url, mutation_acsubject, variables)
#     print('AcSubject imported successfully:', result)
# import requests
# import json
# import os

# # Define the path to the JSON file
# # json_file_path = os.path.join('D:\\Granting-database', 'systemdata2.json')
# json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'systemdata2.json')
# # Load JSON data from the file
# with open(json_file_path, encoding='utf-8') as json_file:
#     data = json.load(json_file)
# print("JSON file path:", json_file_path)

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
import requests
import json
import os

# Define the path to the JSON file
json_file_path = os.path.join('D:\\Granting-database', 'systemdata2.json')
# json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'systemdata2.json')

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

# Function to send mutation request
def send_mutation(url, mutation, variables):
    response = requests.post(url, json={'query': mutation, 'variables': variables})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to execute mutation: {response.status_code}, {response.text}")

# Send acprograms data
for program in data['acprograms']:
    variables = {
        'id': program['id'],
        'name': program['name'],
        'nameEn': program['name_en'],
        'typeId': program['type_id'],
        'lastchange': program['lastchange']
    }
    result = send_mutation(url, mutation_acprogram, variables)
    print('AcProgram imported successfully:', result)

# Send acsubjects data
for subject in data['acsubjects']:
    variables = {
        'id': subject['id'],
        'name': subject['name'],
        'nameEn': subject['name_en'],
        'programId': subject['program_id'],
        'lastchange': subject['lastchange']
    }
    result = send_mutation(url, mutation_acsubject, variables)
    print('AcSubject imported successfully:', result)
