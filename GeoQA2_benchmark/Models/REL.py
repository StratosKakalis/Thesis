import requests

def REL_Inference(question):
    API_URL = "https://rel.cs.ru.nl/api"
    text_doc = question

    # Example EL.
    el_result = requests.post(API_URL, json={
        "text": text_doc,
        "spans": []
    }).json()

    response = ""
    for result in el_result:
        response += result[2] + ": https://en.wikipedia.org/wiki/" + result[3] + "\t"
    
    return response