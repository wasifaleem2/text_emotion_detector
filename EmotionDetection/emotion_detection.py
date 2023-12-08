import requests
import json

def emotion_detector(text_to_analyse):
    """
    this function ibm watson library to generate emotion response
    based on user text and return. this is for skills network.
    """
    url = ''
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        anger = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
        emotion_list = [anger, disgust, fear, joy, sadness]
        dominant_emotion_index = emotion_list.index(max(emotion_list))
        emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
        dominant_emotion_key = emotion_keys[dominant_emotion_index]
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion_key = None

    return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion_key
        }
