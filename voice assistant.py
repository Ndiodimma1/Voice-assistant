import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    time.sleep(1)
    playsound.playsound(filename)



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print("you said", said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

text = get_audio()
if "hello" in text:
    speak("Hello, how are you?")
elif "what is your name" in text:
    speak("my name is zee")
else:
    print("command not recognized")


