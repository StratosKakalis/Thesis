import json

# Function to merge two datasets by concatenating the "Gen_URI" fields
def merge_datasets(dataset1, dataset2):
    merged_data = {}

    for key in dataset1:
        if key in dataset2:
            # Concatenate the "Gen_URI" fields and remove duplicates
            merged_gen_uri = list(set(dataset1[key]["Gen_URI"] + dataset2[key]["Gen_URI"]))
            merged_data[key] = {
                **dataset1[key],
                "Gen_URI": merged_gen_uri  # Replace with the merged Gen_URI
            }
        else:
            # If the key is only in dataset1, copy it as is
            merged_data[key] = dataset1[key]

    for key in dataset2:
        if key not in dataset1:
            # If the key is only in dataset2, copy it as is
            merged_data[key] = dataset2[key]

    return merged_data

# Read JSON data from files
with open("auto-uri-datasets/concepts_dataset.json", "r") as file1, open("auto-uri-datasets/instances_dataset.json", "r") as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

# Merge the datasets
merged_data = merge_datasets(data1, data2)

# Write the merged data into a new JSON file
with open("auto-uri-datasets/concepts_instances_dataset.json", "w") as json_file:
    json.dump(merged_data, json_file, indent=4)

print("Merged JSON data saved to 'merged_data.json'")
