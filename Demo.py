# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 12:07:24 2018

@author: vamsi
"""

# =============================================================================
# set path=%PATH%;C:\Users\vamsi\Anaconda3\Scripts;C:\Users\vamsi\Anaconda3;
# pip install gTTS
# pip install pyglet
# pip install speechrecognition
# pip install pyaudio
# =============================================================================

import speech_recognition as sr
import webbrowser as wb
import Speak_Demo

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"

r = sr.Recognizer()

with sr.Microphone() as source :
    print("Say Something..")
    audio = r.listen(source)
    print("Done...")

try :
    text = r.recognize_google(audio)
    print("Google thinks you said: \n" + text)
    lang = "en"

    Speak_Demo.tts(text, lang)
    
    f_text = "https://www.google.co.in/search?q=" + text
#    wb.get(chrome_path).open(f_text)
    wb.open(f_text);
    print("Task Accomplished...")
except Exception as e :
    print(e)