# assistant.py

import openai
import speech_recognition as sr
import pyttsx3
from config import openai_api_key

openai.api_key = "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"
engine = pyttsx3.init()

def speak(text):
    print("🧠 AI:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("👦 You:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""

def get_response(prompt):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']

def main():
    while True:
        query = listen()
        if "exit" in query.lower():
            speak("Goodbye!")
            break
        if query:
            answer = get_response(query)
            speak(answer)

if __name__ == "__main__":
    main()
