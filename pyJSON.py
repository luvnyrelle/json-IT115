#Importing the JSON library
import json

#Creating the data dictionary
data1 = {


    'name': 'OJ Simpson',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Traveling', 'Football', 'Golf', 'Running', 'Videogames', 'History'],
    'is_student': False


}

# Creating a JSON file and writing the Python object contents to it as data1.json

with open('data1.json', 'w') as json_file:
    # Dumping the data dictionary into the JSON
    json.dump(data1, json_file, indent=4)

print("You have successfully written to data1.json")

# Reading the JSON file
with open('data1.json', 'r') as json_file:
    loaded_data = json.load(json_file)

print("Successfully able to read data1.json")
print(loaded_data)

#Updating the specific fields in load_data

loaded_data['age'] = 11
loaded_data['interests'].append('Reading')

#Writing the updated data back to data1.json

with open('data1.json', 'w') as json_file:

    json.dump(loaded_data, json_file, indent=4)

print("You have successfully re-written to data1.json")