import os
import json
import requests
import pandas as pd
from Models.GPT import GPT_Inference
from Models.REL import REL_Inference
from Models.WAT import WAT_Inference

class Benchmark():
    df = None

    def Model_Inference(self, model, question):
        if (model == 'gpt-one'):
            return GPT_Inference(question, "one")
        elif (model == "gpt-few"):
            return GPT_Inference(question, "few")
        elif (model == "wat"):
            return WAT_Inference(question)
        elif (model == "rel"):
            return REL_Inference(question)

    def Create_Dataframe(self):
        print("Creating ground truth dataframe.")

        # Create dataframe containing question key (number), question, typonym1, wiki1, toponym2, wiki2, toponym3, wiki3.
        columns = ['key', 'question', 'toponym1', 'wiki1', 'toponym2', 'wiki2', 'toponym3', 'wiki3']
        self.df = pd.DataFrame(columns=columns)

        # Read questions from JSON file
        with open('GeoQuestionsNoAnswers.json', 'r') as json_file:
            data = json.load(json_file)

            for key, question_data in data.items():
                    question = question_data['Question']
                    # Append to DataFrame
                    key = int(key)
                    self.df = self.df._append({'key': key, 'question': question}, ignore_index=True)

        # Read answers from text file and update the DataFrame
        labels_path = os.path.join(os.getcwd(), 'Dataset', 'labels.txt')
        with open(labels_path, 'r') as txt_file:
            for line in txt_file:
                key, answer = map(str.strip, line.split(':', 1))
                key = int(key)  # Assuming key is an integer

                stop = False
                toponym1, wiki1, toponym2, wiki2, toponym3, wiki3 = None, None, None, None, None, None
                # Get first toponym.
                if ':' in answer:
                    toponym1, answer = map(str.strip, answer.split(':', 1))
                if ',' in answer:
                    wiki1, answer = map(str.strip, answer.split(',', 1))
                else:
                    wiki1 = answer
                    stop = True

                if stop == False:
                    if ':' in answer:
                        toponym2, answer = map(str.strip, answer.split(':', 1))
                    if ',' in answer:
                        wiki2, answer = map(str.strip, answer.split(',', 1))
                    else:
                        wiki2 = answer
                        stop = True

                if stop == False:
                    if ':' in answer:
                        toponym3, answer = map(str.strip, answer.split(':', 1))
                    if ',' in answer:
                        wiki3, answer = map(str.strip, answer.split(',', 1))
                    else:
                        wiki3 = answer

                
                #print (f"{toponym1}, {wiki1}, {toponym2}, {wiki2}, {toponym3}, {wiki3}")

                # Update DataFrame with answer
                self.df.loc[self.df['key'] == key, 'toponym1'] = toponym1
                self.df.loc[self.df['key'] == key, 'wiki1'] = wiki1
                self.df.loc[self.df['key'] == key, 'toponym2'] = toponym2
                self.df.loc[self.df['key'] == key, 'wiki2'] = wiki2
                self.df.loc[self.df['key'] == key, 'toponym3'] = toponym3
                self.df.loc[self.df['key'] == key, 'wiki3'] = wiki3

        # Display the resulting DataFrame
        print(self.df)

    def Inference_Pipeline(self):
        skip_until = 0
        #model_list = {"gpt-one", "gpt-few", "rel", "wat"}
        model_list = {"rel", "wat"}
        # For each model that we test, run all the questions and save the results in a respective file.
        for model in model_list:
            print("Testing model: " + model)
            with open('Predictions/'+model+'.txt', 'a', encoding='utf-8', errors='ignore') as output_file:
                counter = 0
                # Iterate through each question
                for index, row in self.df.iterrows():
                    key = row['key']
                    question = row['question']

                    if (counter < skip_until):
                        counter+=1
                        continue

                    answer = self.Model_Inference(model, question)
                    print (key)
                    output_file.write(f"{key}: {answer}\n")

    def Evaluate_Pipeline(self):
        pred_path = os.path.join(os.getcwd(), 'Predictions')
        for filename in os.listdir(pred_path):
            filepath = os.path.join(pred_path, filename)
            
            # Create dataframe to contain the answers of the model.
            columns = ['key', 'toponym1', 'wiki1', 'toponym2', 'wiki2', 'toponym3', 'wiki3']
            df = pd.DataFrame(columns=columns)

            # Read the predictions and compare them to the ground truth.
            with open(filepath, 'r') as file:
                print(f"Contents of {filename}:")
                for line in file:
                    key, answer = map(str.strip, line.split(':', 1))
                    key = int(key)  # Assuming key is an integer
    
                    stop = False
                    toponym1, wiki1, toponym2, wiki2, toponym3, wiki3 = None, None, None, None, None, None
                    
                    # Get first toponym.
                    if ':' in answer:
                        toponym1, answer = map(str.strip, answer.split(':', 1))
                    if ',' in answer:
                        wiki1, answer = map(str.strip, answer.split(',', 1))
                    else:
                        wiki1 = answer
                        stop = True
    
                    if stop == False:
                        if ':' in answer:
                            toponym2, answer = map(str.strip, answer.split(':', 1))
                        if ',' in answer:
                            wiki2, answer = map(str.strip, answer.split(',', 1))
                        else:
                            wiki2 = answer
                            stop = True
    
                    if stop == False:
                        if ':' in answer:
                            toponym3, answer = map(str.strip, answer.split(':', 1))
                        if ',' in answer:
                            wiki3, answer = map(str.strip, answer.split(',', 1))
                        else:
                            wiki3 = answer

                    # Update DataFrame with answer
                    df = df._append({'key': key, 'toponym1': toponym1, 'wiki1': wiki1, 'toponym2': toponym2, 'wiki2': wiki2, 'toponym3': toponym3, 'wiki3': wiki3}, ignore_index=True)

            # Display the resulting DataFrame
            print(df)

# First run the benchmark and generate model responses.
bench = Benchmark()
# Create a dataframe from the labaled dataset.
bench.Create_Dataframe()
# Run inference on the selected models.
#bench.Inference_Pipeline()
# Compare model responses to the ground truth. 
bench.Evaluate_Pipeline()