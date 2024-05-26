import json

# Function to load a JSON file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to save a JSON file
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Load the two JSON datasets
dataset1 = load_json('201_questions_dataset.json')
dataset2 = load_json('GeoQuestionsNoAnswers.json')

# Find the maximum key in dataset1 to offset dataset2 keys
max_key_dataset1 = max(int(key) for key in dataset1.keys())

# Offset dataset2 keys
offset = max_key_dataset1
offset_dataset2 = {str(int(key) + offset): value for key, value in dataset2.items()}

# Combine the datasets
combined_dataset = {**dataset1, **offset_dataset2}

# Save the combined dataset to a new JSON file
save_json(combined_dataset, '1291_Geo_Questions.json')

print("Combined dataset created and saved as combined_dataset.json")
