import re
import json

def shorten_uris(uri):
    # This prefix map will be used to shrink the uri's down to the prefix level, to help the model better understand them and decrease mistakes.
    prefix_map = {"http://www.opengis.net/ont/geosparql#" : "geo:",
               "http://www.opengis.net/def/function/geosparql/" : "geof:",
               "http://www.w3.org/1999/02/22-rdf-syntax-ns#" : "rdf:",
               "http://www.w3.org/2000/01/rdf-schema#" : "rdfs:",
               "http://www.w3.org/2001/XMLSchema#" : "xsd:",
               "http://yago-knowledge.org/resource/" : "yago:",
               "http://kr.di.uoa.gr/yago2geo/resource/" : "y2geor:",
               "http://kr.di.uoa.gr/yago2geo/ontology/" : "y2geoo:",
               "http://strdf.di.uoa.gr/ontology#" : "strdf:",
               "http://www.opengis.net/def/uom/OGC/1.0/" : "uom:",
               "http://www.w3.org/2002/07/owl#" : "owl:"}
    
    for uri_map, prefix in prefix_map.items():
        uri = uri.replace(uri_map, prefix)
    return uri


# Function to extract URIs
def extract_uris(query):
    # Regular expression to match both fully expanded and prefixed URIs
    uri_pattern = r'<([^>]+)>|(\b[a-zA-Z0-9_]+):([a-zA-Z0-9_]+)'
    
    uris = []
    matches = re.findall(uri_pattern, query)
    for match in matches:
        if match[0]:  # Fully expanded URI
            uris.append(match[0])
        else:  # Prefixed URI
            uris.append(f"{match[1]}:{match[2]}")

    wat = []
    for uri in uris:
        hm = shorten_uris(uri)
        wat.append(hm)

    return wat

# Load the JSON data from a file
input_file = 'c:/Users/strat/Desktop/validation_set.json'
with open(input_file, 'r') as file:
    data = json.load(file)

# Process each item in the JSON data
for key, value in data.items():
    query = value.get("Query", "")
    uris = extract_uris(query)
    value["URI"] = uris

# Save the updated data to a new JSON file
output_file = 'Dataset_Creation/validation_set_URI.json'
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Updated data has been saved to {output_file}.")
