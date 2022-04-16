from gpiozero import LED
from gpiozero import Button
from time import sleep
from google.cloud import speech
from Adafruit_CharLCD import Adafruit_CharLCD
from gpiozero.pins.pigpio import PiGPIOFactory

#importing functions from other file
from Braille_letters import *


import os
import io
import sys
import subprocess
import signal
import time

#voice input button
button_text = Button(5) #Gpio 5
#text input button
button_voice = Button(26) #Gpio 26
#start recording button
button_record = Button(6) #Gpio 13
#start locator
button_locator = Button(23)     # change this
led_vibration = LED(24)          # change this
button_repeat = Button(25)       # change this
# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=10, en=11, d4=9, d5=27, d6=22, d7=17, cols=16, lines=2, backlight=2)

#global input from user
input_from_user = ""

def text_input():
    global input_from_user
    input_from_user = input("enter a word to translate: ")
    print ("word to translate: " + input_from_user)
    lcd_display(input_from_user)
    word_interation(input_from_user)

def voice_input(): 
    lcd.clear()
    lcd.message("Press to record")
    while True:
        if button_record.is_pressed:
            print("Button is pressed")
            lcd.clear()
            lcd.message("  Recording\n  Started")
            print("recording started")
            record = 'arecord -d 10 --format=S16_LE --rate=16000 test.wav'
            p = subprocess.Popen(record, shell=True)
            sleep(10)
            print("recording over")
            lcd.clear()
            lcd_display("recording over")
            speech_api()
            break

def speech_api():
    global input_from_user
    # Creates google client
    client = speech.SpeechClient()
    # Full path of the audio file, Replace with your file name
    file_name = os.path.join(os.path.dirname(__file__),"test.wav")

    #Loads the audio file into memory
    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=1,
        language_code="en-US",
    )
    # Sends the request to google to transcribe the audio
    response = client.recognize(request={"config": config, "audio": audio})
    # Reads the response
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

    #takes response from google transcribe and converts to list
    final_transcripts = []
    for result in response.results:
        alternative = result.alternatives[0]
        final_transcripts.append(alternative.transcript)

    #takes list and makes it a string
    output = ""
    for i in final_transcripts:
        output += ' ' + i
    input_from_user = output
    print(input_from_user)
    lcd_display(input_from_user)
    word_interation(input_from_user)

def lcd_display(input):
    lcd.clear()
    lcd.message(input)
    sleep(10)
    lcd.clear()

def locator_func():
    led_vibration.on()
    sleep(10)
    led_vibration.off()
    print("Locator")

def repeat_func():
    #print("repeating the hello world")
    lcd_display(input_from_user)
    word_interation(input_from_user)
    #input_from_user is global variable that holds the text to translate
    
    
#main

#asking text or voice input on display
lcd.clear()
lcd.message(" Input Options\n Repeat Text Voice")
while True:
    if button_text.is_pressed:  
        print("input text")
        lcd.clear()
        lcd.message("  Input Text")
        text_input()
        lcd.clear()
        lcd.message(" Input Options\n Repeat Text Voice")
        continue
    if button_voice.is_pressed:
        print("input voice")
        lcd.clear()
        lcd.message("  Input Voice")
        voice_input()
        lcd.clear()
        lcd.message(" Input Options\n Repeat Text Voice")
        continue
    if button_locator.is_pressed:
        print("Locator")
        lcd.clear()
        lcd.message("locator enabled")
        locator_func()
        lcd.clear()
        lcd.message(" Input Options\n Repeat Text Voice")
        continue
    if button_record.is_pressed:
        print("repeat")
        lcd.clear()
        lcd.message("repeating message")
        repeat_func()
        lcd.clear()
        lcd.message(" Input Options\n Repeat Text Voice")
        continue
#main