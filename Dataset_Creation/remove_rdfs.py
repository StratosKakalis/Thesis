import json

def create_short_json(input_file, output_file):
    # Load the original JSON data
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Create a new dictionary with keys less than or equal to 937
    short_data = {key: value for key, value in data.items() if int(key) <= 937}
    
    # Write the new data to the output file
    with open(output_file, 'w') as f:
        json.dump(short_data, f, indent=4)

# Example usage
input_file = 'C:/Users/BG/Desktop/concepts_instances_dataset.json'  # Replace with your original file name
output_file = 'C:/Users/BG/Desktop/concepts_instances_dataset_no_rdfs.json'
create_short_json(input_file, output_file)
