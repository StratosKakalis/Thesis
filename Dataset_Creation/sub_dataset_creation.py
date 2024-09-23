import json
import random

# Load the original dataset
with open('GeoQuestionsNoAnswersStripped.json', 'r') as file:
    original_dataset = json.load(file)

# Randomly select 300 question-query pairs
random_selection = random.sample(list(original_dataset.items()), 100)

# Create a new dataset with the selected pairs
new_dataset = {}
for key, value in random_selection:
    new_dataset[key] = value

# Save the new dataset to a JSON file
with open('100_Sub_Dataset.json', 'w') as file:
    json.dump(new_dataset, file, indent=4)

print("Randomly selected dataset saved as randomly_selected_dataset.json")
