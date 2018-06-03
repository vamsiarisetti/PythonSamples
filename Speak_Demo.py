# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 14:54:21 2018

@author: vamsi
"""

from gtts import gTTS
import pyglet
import time, os

def tts(text, lang) :
     file = gTTS(text = text, lang = lang)
     fileName = '/tmp/temp.mp3'
     file.save(fileName)
     
     music = pyglet.media.load(fileName, streaming = False)
     music.play()
     
     time.sleep(music.duration)
     os.remove(fileName)