from flask import Flask, request, jsonify
from gtts import gTTS
import os
from io import BytesIO
from flask import send_file

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get("text")
    lang = data.get("lang", "si")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        tts = gTTS(text=text, lang=lang)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        return send_file(mp3_fp, mimetype="audio/mpeg", download_name="tts.mp3")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def hello():
    return "TTS API is running!"

if __name__ == '__main__':
    app.run()
