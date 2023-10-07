import json

with open('GeoQuestionsNoAnswers.json', 'r') as json_file:
    data = json.load(json_file)

with open('questions.txt', 'a', encoding='utf-8', errors='ignore') as output_file:
    
    # Iterate through each question
    for key, question_data in data.items():
        question = question_data['Question']
        output_file.write(f"{key}: {question}\n")