import pyttsx3
import speech_recognition as sr
import json



# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
mic = sr.Microphone()
recognizer = sr.Recognizer()
def audio_input():
        try:
            with mic as source:
                recognizer.energy_threshold = 4000
                recognizer.adjust_for_ambient_noise(source, duration = 5)
                print("Listening.....")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio, language='en-in').lower()
                return command

        except sr.UnknownValueError:
            return " "

engine = pyttsx3.init('sapi5')
def tts(text):
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 175)
    return True







    


