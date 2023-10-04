import json
import openai
import requests
from Models.GPT import GPT_Inference
from Models.REL import REL_Inference
from Models.WAT import WAT_Inference

def Model_Inference(model, question):
    if (model == 'gpt'):
        return GPT_Inference(question)
    elif (model == "wat"):
        return WAT_Inference(question)
    elif (model == "rel"):
        return REL_Inference(question)

with open('GeoQuestionsNoAnswers.json', 'r') as json_file:
    data = json.load(json_file)

skip_until = 69

#model_list = {"gpt", "rel", "wat"}
model_list = {"gpt"}
# For each model that we test, run all the questions and save the results in a respective file.
for model in model_list:
    print("Testing model: " + model)
    with open('Results/'+model+'.txt', 'a', encoding='utf-8', errors='ignore') as output_file:
        counter = 0
        # Iterate through each question
        for key, question_data in data.items():
            if (counter < skip_until):
                counter+=1
                continue

            question = question_data['Question']

            answer = Model_Inference(model, question)
            print (key)
            output_file.write(f"{key}: {answer}\n")