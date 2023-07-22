from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

lang = ('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am',
        'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
        # Rest of the languages...
        'zulu', 'zu')

# Capture Voice
# takes command through the microphone
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query


query = listen()
while query == "None":
    query = listen()


def destination_language():
    print("Convert to: Ex. Hindi, English, etc.")
    print()

    to_lang = listen()
    while to_lang == "None":
        to_lang = listen()
    to_lang = to_lang.lower()
    return to_lang


to_lang = destination_language()

while to_lang not in lang:
    print("The language you want to convert to is currently not available. Please input some other language.")
    print()
    to_lang = destination_language()

to_lang = lang[lang.index(to_lang) + 1]

translator = Translator()

text_to_translate = translator.translate(query, dest=to_lang)
text = text_to_translate.text

speak = gTTS(text=text, lang=to_lang, slow=False)

# Speech
speak.save("from_voice.mp3")

# Using OS module to run the translated voice.
playsound('from_voice.mp3')
os.remove('from_voice.mp3')
print(text)



