import requests
import json
#1
# in the terminal call the python shell import this function and pass the validation of the string "anything you want"
# and it will be something like this {
    #'{"documentSentiment":{"score":0.996954, "label":"SENT_POSITIVE",
    # "mixed":false,
    # "sentimentMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"},
    # "sentimentprob":{"positive":0.9941229, "neutral":0.0028645627, "negative":0.0030124863}}]},
    # "targetedSentiments":{"targetedSentiments":{}, "producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}, 
    # "producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}'
#}

#2
#we should make it readable by passing it in json and make it dictionary


def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}