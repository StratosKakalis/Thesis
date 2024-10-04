import json

# Path to the matched URIs file
input_file_path = 'C:/Users/strat/Desktop/EKPA/Thesis/Dataset_Creation/matched_uris.json'

# Load the matched URIs from the JSON file
with open(input_file_path, 'r') as input_file:
    matched_uris = json.load(input_file)

# Count the total number of URIs
count = sum(len(uris) for uris in matched_uris.values())

print(f"Total number of matched URIs: {count}")
