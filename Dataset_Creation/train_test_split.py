import json
import random

# File paths
original_dataset_path = 'Dataset_Creation/GeoQuestionsNoAnswersStripped.json'
test_dataset_path = 'Dataset_Creation/100_Sub_Dataset.json'
training_set_path = 'Dataset_Creation/training_set.json'
validation_set_path = 'Dataset_Creation/validation_set.json'

# Load the original dataset
with open(original_dataset_path, 'r') as f:
    original_dataset = json.load(f)

# Load the test dataset
with open(test_dataset_path, 'r') as f:
    test_dataset = json.load(f)

# Identify keys in the original dataset that are not in the test dataset
test_keys = set(test_dataset.keys())
unused_items = {k: v for k, v in original_dataset.items() if k not in test_keys}

# Randomly select 100 items for the validation set
validation_keys = random.sample(list(unused_items.keys()), 100)
validation_set = {k: unused_items.pop(k) for k in validation_keys}

# The remaining items form the training set
training_set = unused_items

# Export the validation set to a JSON file
with open(validation_set_path, 'w') as f:
    json.dump(validation_set, f, indent=4)

# Export the training set to a JSON file
with open(training_set_path, 'w') as f:
    json.dump(training_set, f, indent=4)

print("Training and validation sets have been created successfully.")
