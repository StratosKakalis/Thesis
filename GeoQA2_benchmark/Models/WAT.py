import requests
import json

MY_GCUBE_TOKEN = 'd9b71f2f-42d3-4286-95f3-e5775c538d61-843339462'

class WATAnnotation:
    # An entity annotated by WAT

    def __init__(self, d):

        # char offset (included)
        self.start = d['start']
        # char offset (not included)
        self.end = d['end']

        # annotation accuracy
        self.rho = d['rho']
        # spot-entity probability
        self.prior_prob = d['explanation']['prior_explanation']['entity_mention_probability']

        # annotated text
        self.spot = d['spot']

        # Wikpedia entity info
        self.wiki_id = d['id']
        self.wiki_title = d['title']


    def json_dict(self):
        # Simple dictionary representation
        return {'wiki_title': self.wiki_title,
                'wiki_id': self.wiki_id,
                'wiki_link': 'https://en.wikipedia.org/wiki/?curid=' + str(self.wiki_id),
                'start': self.start,
                'end': self.end,
                'rho': self.rho,
                'prior_prob': self.prior_prob
                }


def wat_entity_linking(text):
    # Main method, text annotation with WAT entity linking system
    wat_url = 'https://wat.d4science.org/wat/tag/tag'
    payload = [("gcube-token", MY_GCUBE_TOKEN),
               ("text", text),
               ("lang", 'en'),
               ("tokenizer", "nlp4j"),
               ('debug', 9),
               ("method",
                "spotter:includeUserHint=true:includeNamedEntity=true:includeNounPhrase=true,prior:k=50,filter-valid,centroid:rescore=true,topk:k=5,voting:relatedness=lm,ranker:model=0046.model,confidence:model=pruner-wiki.linear")]

    response = requests.get(wat_url, params=payload)
    return [WATAnnotation(a) for a in response.json()['annotations']]


def print_wat_annotations(wat_annotations):
    #json_list = [w.json_dict() for w in wat_annotations]
    result = ""
    for w in wat_annotations:
        result += w.json_dict()['wiki_title'] + ': ' + w.json_dict()['wiki_link'] + ' | '


    return result
    #print (json.dumps(json_list, indent=4))
        

def WAT_Inference(question):
    wat_annotations = wat_entity_linking(question)
    return print_wat_annotations(wat_annotations)