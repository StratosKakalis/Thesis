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

# Function to check if the query starts with 'SELECT' or 'ASK'
def is_valid_query(query):
    # Check if the query starts with 'select' or 'ask' (case-insensitive)
    return re.match(r'^\s*(select|ask)', query, re.IGNORECASE) is not None

# Load the dataset
dataset = load_json('1290_Geo_Questions.json')

# Scan and remove invalid queries
valid_dataset = {}
invalid_keys = []
for key, item in dataset.items():
    query = item.get('Query', '')
    if is_valid_query(query):
        valid_dataset[key] = item
    else:
        invalid_keys.append(key)

# Debugging information
print(f"Total items in original dataset: {len(dataset)}")
print(f"Total invalid queries found: {len(invalid_keys)}")
print(f"Keys of invalid queries: {invalid_keys}")
print(f"Total items in valid dataset before reindexing: {len(valid_dataset)}")

# Ensure proper indexing
reindexed_dataset = {str(index + 1): value for index, (key, value) in enumerate(valid_dataset.items())}

# Debugging information after reindexing
print(f"Total items in reindexed dataset: {len(reindexed_dataset)}")

# Save the cleaned and reindexed dataset to a new JSON file
save_json(reindexed_dataset, 'cleaned_reindexed_dataset.json')

print("Cleaned and reindexed dataset created and saved as cleaned_reindexed_dataset.json")
