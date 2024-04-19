import os
import json
import requests
import pandas as pd
from Models.GPT import GPT_Inference
from Models.REL import REL_Inference
from Models.WAT import WAT_Inference
import Levenshtein

def is_similar(value1, value2, threshold=0.65):
    # Check if two values are similar using Levenshtein distance
    distance = Levenshtein.distance(value1.lower(), value2.lower())
    max_len = max(len(value1), len(value2))
    similarity = 1 - distance / max_len
    return similarity >= threshold

def is_subset(value1, value2, threshold=0.65):
    # Check if one value is a subset of the other, considering singular/plural differences and typos.
    set1 = set(value1.lower().split())
    set2 = set(value2.lower().split())

    if value1 == value2 == '':
        return False

    return (
        is_similar(value1, value2, threshold) or
        set1 <= set2 or
        set2 <= set1 or
        ("usa" in value1.lower() and "united" in value2.lower() and "states" in value2.lower()) or
        ("usa" in value2.lower() and "united" in value1.lower() and "states" in value1.lower()) or
        ("us" in value1.lower() and "united" in value2.lower() and "states" in value2.lower()) or
        ("us" in value2.lower() and "united" in value1.lower() and "states" in value1.lower()) or
        ("uk" in value1.lower() and "united" in value2.lower() and "kingdom" in value2.lower()) or
        ("uk" in value2.lower() and "united" in value1.lower() and "kingdom" in value1.lower())
    )

class Benchmark():
    df = None

    def Model_Inference(self, model, question):
        if (model == 'gpt-one'):
            return GPT_Inference(question, "one")
        elif (model == "gpt-few"):
            return GPT_Inference(question, "few")
        elif (model == "gpt-few2"):
            return GPT_Inference(question, "few2")
        elif (model == "gpt-few3"):
            return GPT_Inference(question, "few3")
        elif (model == "gpt-few4"):
            return GPT_Inference(question, "few4")
        elif (model == "gpt-few5"):
            return GPT_Inference(question, "few5")
        elif (model == "gpt-few6"):
            return GPT_Inference(question, "few6")
        elif (model == "gpt-few7"):
            return GPT_Inference(question, "few7")
        elif (model == "gpt-few8"):
            return GPT_Inference(question, "few8")
        elif (model == "gpt-few9"):
            return GPT_Inference(question, "few9")
        elif (model == "custom1"):
            return GPT_Inference(question, "custom1")
        elif (model == "custom2"):
            return GPT_Inference(question, "custom2")
        elif (model == "custom3"):
            return GPT_Inference(question, "custom3")
        elif (model == "custom4"):
            return GPT_Inference(question, "custom4")
        elif (model == "custom5"):
            return GPT_Inference(question, "custom5")
        elif (model == "custom6"):
            return GPT_Inference(question, "custom6")
        elif (model == "custom7"):
            return GPT_Inference(question, "custom7")
        elif (model == "custom8"):
            return GPT_Inference(question, "custom8")
        elif (model == "custom9"):
            return GPT_Inference(question, "custom9")
        elif (model == "custom10"):
            return GPT_Inference(question, "custom10")
        elif (model == "custom11"):
            return GPT_Inference(question, "custom11")
        elif (model == "custom12"):
            return GPT_Inference(question, "custom12")
        elif (model == "custom13"):
            return GPT_Inference(question, "custom13")
        elif (model == "custom14"):
            return GPT_Inference(question, "custom14")
        
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
                if ' | ' in answer:
                    wiki1, answer = map(str.strip, answer.split(' | ', 1))
                else:
                    wiki1 = answer
                    stop = True

                if stop == False:
                    if ':' in answer:
                        toponym2, answer = map(str.strip, answer.split(':', 1))
                    if ' | ' in answer:
                        wiki2, answer = map(str.strip, answer.split(' | ', 1))
                    else:
                        wiki2 = answer
                        stop = True

                if stop == False:
                    if ':' in answer:
                        toponym3, answer = map(str.strip, answer.split(':', 1))
                    if ' | ' in answer:
                        wiki3, answer = map(str.strip, answer.split(' | ', 1))
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
        model_list = ["gpt-one", "gpt-few", "rel", "wat"]
        #model_list = ["custom1"]
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

                #answer = self.Model_Inference(model, "question")
                #print(answer)

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
                    if ' | ' in answer:
                        wiki1, answer = map(str.strip, answer.split(' | ', 1))
                    else:
                        wiki1 = answer
                        stop = True
    
                    if stop == False:
                        if ':' in answer:
                            toponym2, answer = map(str.strip, answer.split(':', 1))
                        if ' | ' in answer:
                            wiki2, answer = map(str.strip, answer.split(' | ', 1))
                        else:
                            wiki2 = answer
                            stop = True
    
                    if stop == False:
                        if ':' in answer:
                            toponym3, answer = map(str.strip, answer.split(':', 1))
                        if ' | ' in answer:
                            wiki3, answer = map(str.strip, answer.split(' | ', 1))
                        else:
                            wiki3 = answer

                    # Update DataFrame with answer
                    df = df._append({'key': key, 'toponym1': toponym1, 'wiki1': wiki1, 'toponym2': toponym2, 'wiki2': wiki2, 'toponym3': toponym3, 'wiki3': wiki3}, ignore_index=True)

            # Display the resulting DataFrame
            #print(df)

            # Now evaluate the models performance by comparing df to the ground truth dataframe (self.df)
            # Select only the relevant columns before merging.
            model_df = df[['key', 'toponym1', 'wiki1', 'toponym2', 'wiki2', 'toponym3', 'wiki3']]
            gt_df = self.df[['key', 'toponym1', 'wiki1', 'toponym2', 'wiki2', 'toponym3', 'wiki3']]

            # Merge DataFrames on the 'key' column.
            merged_df = pd.merge(model_df, gt_df, on='key', suffixes=('_mdl', '_gt'))

            # Compare predictions for every key.
            TP = 0
            FP = 0
            FN = 0
            correct_wiki_links = 0
            wrong_wiki_links = 0
            for index, row in merged_df.iterrows():
                initFP, initFN = TP, FN
                key = row['key']
                toponym1_gt = row['toponym1_gt']
                toponym1_mdl = row['toponym1_mdl']
                toponym2_gt = row['toponym2_gt']
                toponym2_mdl = row['toponym2_mdl']
                toponym3_gt = row['toponym3_gt']
                toponym3_mdl = row['toponym3_mdl']

                wiki1_gt = row['wiki1_gt']
                wiki1_mdl = row['wiki1_mdl']
                wiki2_gt = row['wiki2_gt']
                wiki2_mdl = row['wiki2_mdl']
                wiki3_gt = row['wiki3_gt']
                wiki3_mdl = row['wiki3_mdl']

                # List with predicted toponyms.
                predicted_toponyms = []
                if toponym1_mdl is not None:
                    predicted_toponyms.append(toponym1_mdl.lower())
                if toponym2_mdl is not None:
                    predicted_toponyms.append(toponym2_mdl.lower())
                if toponym3_mdl is not None:
                    predicted_toponyms.append(toponym3_mdl.lower())

                # List with ground truth toponyms.
                gt_toponyms = []
                if toponym1_gt is not None:
                    gt_toponyms.append(toponym1_gt.lower())
                if toponym2_gt is not None:
                    gt_toponyms.append(toponym2_gt.lower())
                if toponym3_gt is not None:
                    gt_toponyms.append(toponym3_gt.lower())

                for value in predicted_toponyms:
                    #if value in gt_toponyms:
                    if any(is_subset(value, gt_value) for gt_value in gt_toponyms):
                        TP += 1
                    else:
                        FP += 1

                for value in gt_toponyms:
                    #if value not in predicted_toponyms:
                    if not any(is_subset(value, pred_value) for pred_value in predicted_toponyms):
                        FN += 1

                # Now evaluate the wikipedia link predictions:
                # List with predicted links.
                predicted_wikis = []
                if wiki1_mdl is not None:
                    predicted_wikis.append(wiki1_mdl.lower())
                if wiki2_mdl is not None:
                    predicted_wikis.append(wiki2_mdl.lower())
                if wiki3_mdl is not None:
                    predicted_wikis.append(wiki3_mdl.lower())

                # List with ground truth wikis.
                gt_wikis = []
                if wiki1_gt is not None:
                    gt_wikis.append(wiki1_gt.lower())
                if wiki2_gt is not None:
                    gt_wikis.append(wiki2_gt.lower())
                if wiki3_gt is not None:
                    gt_wikis.append(wiki3_gt.lower())
                
                for value in predicted_wikis:
                    #if value in gt_toponyms:
                    if any(is_subset(value, gt_value, 1) for gt_value in gt_wikis):
                        correct_wiki_links+=1
                    else:
                        wrong_wiki_links+=1

                for value in gt_wikis:
                    #if value not in predicted_toponyms:
                    if not any(is_subset(value, pred_value, 1) for pred_value in predicted_wikis):
                        wrong_wiki_links+=1

                #if (FP > initFP or FN > initFN):
                    #print (row)

            # Calculate model metrics.
            precision = TP / (TP + FP)
            recall = TP / (TP + FN)
            F1 = (2 * precision * recall) / (precision + recall)
            wiki_accuracy = (correct_wiki_links / (correct_wiki_links + wrong_wiki_links)) * 100
            print(f"Model {filename} metrics: Precision: {precision}, Recall: {recall}, F1-Score: {F1}, Wikification Accuracy: {wiki_accuracy}.")

# First run the benchmark and generate model responses.
bench = Benchmark()
# Create a dataframe from the labaled dataset.
#bench.Create_Dataframe()
# Run inference on the selected models.
bench.Inference_Pipeline()
# Compare model responses to the ground truth. 
#bench.Evaluate_Pipeline()