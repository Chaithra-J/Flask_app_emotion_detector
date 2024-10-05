import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    # emotion = formatted_response.get('emotionPredictions', {}).get('emotion', 'Unknown Emotion')
    if response.status_code == 200:
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        result = {key: value for key, value in emotion_data.items()}  
        result['dominant_emotion'] = max(emotion_data, key=emotion_data.get)  
    
    
    elif response.status_code == 400:
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        result = {key: None for key in emotion_data.keys()}
    
    else:
        # Handle other status codes as necessary (e.g., 500 errors)
        result = {'error': 'Unexpected error occurred'}

    return {'result': result}