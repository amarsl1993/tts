# app.py
from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get("text")
    lang = data.get("lang", "si")  # default to Sinhala

    if not text:
        return jsonify({"error": "No text provided"}), 400

    filename = f"{text[:50].replace(' ', '_')}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    return jsonify({"message": "Audio generated", "file": filename})

if __name__ == '__main__':
    app.run()

