def gost_extract_triples(query: str):
    data = {
        "query": query
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = 
requests.post
('
http://195.134.71.116:9090/triples
', headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.text
        # return "SELECT * WHERE { \n" + response.text + "}\n"
    else:
        print("Error:", response.text)
        
def gost_extract_uris(query: str):
    data = {
        "query": query
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = 
requests.post
('
http://195.134.71.116:9090/uris
', headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.text
        # return "SELECT * WHERE { \n" + response.text + "}\n"
    else:
        print("Error:", response.text) 


def gost_is_valid_query(query: str):
    data = {
        "query": query
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = 
requests.post
('
http://195.134.71.116:9090/validate-api
', headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.text) 