import json
import re

# Function to load a JSON file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to save a JSON file
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to clean up query strings
def clean_query(query):
    # Replace multiple spaces with a single space
    query = re.sub(r'\s{2,}', ' ', query)
    # Replace tab characters with a single space
    query = query.replace('\t', ' ')
    return query

# Load the dataset
dataset = load_json('1290_Geo_Questions.json')

# Clean the queries in the dataset
for item in dataset.values():
    if 'Query' in item:
        item['Query'] = clean_query(item['Query'])

# Save the cleaned dataset to a new JSON file
save_json(dataset, 'cleaned_dataset.json')

print("Cleaned dataset created and saved as cleaned_dataset.json")
