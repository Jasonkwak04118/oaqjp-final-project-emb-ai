
from flask import Flask , render_template
import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header ={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    formatted_response['emotionPredictions']
    resp = ((str(formatted_response['emotionPredictions'])[2:-2]).split('},')[0][12:-1]).split(",")
    e = []
    for i in range(5):
        e.append(float((resp[i].split(":")[1])[1:]))
    anger_score, disgust_score, fear_score, joy_score, sadness_score = e[0], e[1], e[2], e[3], e[4]
    emotions= ['anger', 'disgust', 'fear', 'joy', 'sadness']
    maxdict = dict()

    for j in range(len(e)):
        maxdict[e[j]] = emotions[j]
    dominant_emotion = maxdict[max(e)]
    
    #if response.status_code == 200:
    #    label = formatted_response['documentSentiment']['label'] 
    #    score = formatted_response['documentSentiment']['score']
    #elif response.status_code == 500:
    #    label = None
    #    score = None
    formatted = {'anger': anger_score, 
    'disgust': disgust_score, 
    'fear': fear_score, 
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }
    return  formatted
    


    


