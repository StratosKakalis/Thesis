import json
import re
import torch

# Define the regex pattern for the prefixes in their shortened form
prefix_pattern = re.compile(r"^(yago:)")

# Load the JSON dataset
with open('C:/Users/strat/Desktop/EKPA/Thesis/Dataset_Creation/validation_set_URI.json', 'r') as file:
    original_dataset = json.load(file)

matched_uris = {}  # Dictionary to store matched URIs

# Iterate through the dataset and collect URIs matching the prefixes
for key in original_dataset:
    uris = original_dataset[key]['URI']
    question = original_dataset[key]['Question']
    query = original_dataset[key]['Query']

    if key not in matched_uris:
        matched_uris[key] = {}

    matched_uris[key]['Question'] = question
    matched_uris[key]['Query'] = query
    matched_uris[key]['URI'] = [uri for uri in uris if prefix_pattern.match(uri)]

# Save the matched URIs to a new JSON file
output_file_path = 'Dataset_Creation/validation_set_Instances.json'
with open(output_file_path, 'w') as output_file:
    json.dump(matched_uris, output_file, indent=4)

print(f"Matched URIs have been written to {output_file_path}")
