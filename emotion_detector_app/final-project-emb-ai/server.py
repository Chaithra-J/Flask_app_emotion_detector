from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion():
    textToAnalyze = request.args.get('textToAnalyze')
    if not textToAnalyze or textToAnalyze.strip() == "":
        return "Invalid text! Please try again!"
   
    response = emotion_detector(textToAnalyze)
    result = response['result']

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"
    else:
        scores_string = ', '.join([f"'{emotion}': {score}" for emotion, score in result.items() if emotion != 'dominant_emotion'])
        dominant_emotion = result.get('dominant_emotion', 'Unknown')
        return f"For the given statement, the system response is '{scores_string}'. The dominant emotion is '{dominant_emotion}'."

if __name__ == "__main__":
    app.run(host="0.0.0", port=5000)