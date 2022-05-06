from gpiozero import LED
from gpiozero import Button
from time import sleep
from google.cloud import speech
from Adafruit_CharLCD import Adafruit_CharLCD
from gpiozero.pins.pigpio import PiGPIOFactory

#importing functions from other file Braille_letters.py
from Braille_letters import *

import os
import io
import sys
import subprocess
import signal
import time


button_1 = Button(19) #Gpio 5
#voice input button
button_2 = Button(5) #Gpio 5
#start recording button
button_3 = Button(6) #Gpio 13
#text input button
button_4 = Button(26) #Gpio 26
#start locator
button_locator = Button(23)       # change this
#led_vibration = LED(24)          # change this

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=10, en=11, d4=9, d5=27, d6=22, d7=17, cols=16, lines=2, backlight=2)

#global variables
input_from_user = "No Previouse Message" #stores text to be translated to braille

def braille_config_controls():
    while True:
        if button_2.is_pressed: #braille speed up ++   
            #SpeedBrailleUp()
            lcd.clear()
            lcd.message("Braille Speed\n             <--")
            continue
        if button_3.is_pressed: #braille speed up --
            SpeedBrailleDown()
            lcd.clear()
            lcd.message("Braille Speed\n             <--")
            continue
        else: #back button
            break

def config():
  while True:
    if button_2.is_pressed: #braille speed controls
        lcd.clear()
        lcd.message("Braille Speed\n             <--")
        braille_config_controls()
        continue
    if button_3.is_pressed: #haptics intensity
        continue
    if button_4.is_pressed: #back button
    
    #might still be pressed when function ends maybe add a delay or check 
        return 
  
def text_input():
    global input_from_user
    #input from user taken from terminal
    input_from_user = input("enter a word to translate: ")
    while True:
        if (len(input_from_user) > 128):
            #global input_from_user
            print("over limit word limit, Enter again")
            lcd_display("over limit")
            input_from_user = input("enter a word to translate: ")
        else:
            break
    print ("word to translate: " + input_from_user)
    #input shown on diaplay
    lcd_display(input_from_user)
    #input sent to braille device for output
    word_interation(input_from_user)

def voice_input(): 
    lcd.clear()
    lcd.message("Press to record\nButton 3")
    while True:
        if button_3.is_pressed:
            print("Button is pressed")
            lcd.clear()
            lcd.message("  Recording\n  Started")
            print("recording started")
            #recording with 10 second duration
            #saves audio to test.wav
            record = 'arecord -d 10 --format=S16_LE --rate=16000 test.wav'
            p = subprocess.Popen(record, shell=True)
            #10 second delay so program waits for recording to finish
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
    #ads output from api into global variable
    input_from_user = output
    print(input_from_user)
    #outputs to display
    lcd_display(input_from_user)
    #outputs to braille device
    word_interation(input_from_user)

def lcd_display(input):
    #for i in input:
    temp_var1 = ""
    temp_var2 = "" 
    temp_var3 = "" 
    temp_var4 = "" 
    lcd.clear()
    print(len(input))
    #displays temp_var1 on top line and temp_var2 on bottom line
    if((len(input) > 16)and(len(input)<=32)):
        print("for loop 1")
        for i in range(16):#adds characters 0-16 to variable temp_var1
            temp_var1 += input[i]
        if(len(input)!=32):
            for j in range(16,(len(input))):#adds characters 16- size of input to variable temp_var2
                temp_var2 += input[j]
        else:
            for j in range(16,32):#adds characters 16-31 to variable temp_var2
                temp_var2 += input[j]
        lcd.message(temp_var1 + "\n" + temp_var2)
        sleep(3)
    #shows characters 0-31 on top line and scrolls to the left
    #then shows characters 32-63 on top line and scrolls to the left
    elif((len(input)>32)and(len(input)<=64)):
        print("for loop 2")
        for i in range(32):#adds characters 0-31 to variable temp_var1
            temp_var1 += input[i]
        print (temp_var1)
        if(len(input)!=64):
            for j in range(32,(len(input))):#adds characters 32- size or input to variable temp_var2
                temp_var2 += input[j]         
        else:       
            for j in range(32, 64):#adds characters 32-63 to variable temp_var2
                temp_var2 += input[j]
        print (temp_var2)
        lcd.message(temp_var1)#displays temp_var1 on top row then scrolls left
        sleep(3)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(3)
        lcd.clear()
        lcd.message(temp_var2)#displays temp_var2 on top row then scrolls left
        sleep(3)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        lcd.clear()
    #shows characters 0-31 on top line and scrolls to the left
    #then shows characters 32-63 on top line and scrolls to the left
    #then shows characters 64-95 on top line and scrolls to the left
    elif((len(input)>64)and(len(input)<=96)):
        print("for loop 3")
        for i in range(32):#adds characters 0-31 to variable temp_var1
            temp_var1 += input[i]
        print (temp_var1)
        for j in range(32, 64):#adds characters 32-63 to variable temp_var2
            temp_var2 += input[j]
        print (temp_var2)
        if(len(input)!=96):
            for j in range(64,(len(input))):#adds characters 32- size or input to variable temp_var2
                temp_var3 += input[j] 
        else:
            for k in range(64, 96):#adds characters 64-95 to variable temp_var3
                temp_var3 += input[k]
        print (temp_var3)
        lcd.message(temp_var1)#displays temp_var1 on top row then scrolls left
        sleep(3)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(3)
        lcd.clear()
        lcd.message(temp_var2)#displays temp_var2 on top row then scrolls left
        sleep(3)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(3)
        lcd.clear()
        lcd.message(temp_var3)#displays temp_var3 on top row then scrolls left
        sleep(3)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(3)
        lcd.clear()
    #shows characters 0-31 on top line and scrolls to the left
    #then shows characters 32-63 on top line and scrolls to the left
    #then shows characters 64-95 on top line and scrolls to the left
    #then shows characters 96-127 on top line and scrolls to the left
    elif((len(input)>96)and(len(input)<=128)):
        print("for loop 4")
        for i in range(32):#adds characters 0-31 to variable temp_var1
            temp_var1 += input[i]
        print (temp_var1)
        for j in range(32, 64):#adds characters 32-63 to variable temp_var2
            temp_var2 += input[j]
        print (temp_var2)
        for k in range(64, 96):#adds characters 64-95 to variable temp_var3
            temp_var3 += input[k]
        print (temp_var3)
        if(len(input)!=128):
            for j in range(96,(len(input))):#adds characters 32- size or input to variable temp_var2
                temp_var4 += input[j] 
        else:
            for l in range(96, 128):#adds characters 96-127 to variable temp_var4
                temp_var4 += input[l]
        print (temp_var4)
        
        lcd.message(temp_var1)#displays temp_var1 on top row then scrolls left
        sleep(3)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(3)
        lcd.clear()
        lcd.message(temp_var2)#displays temp_var2 on top row then scrolls left
        sleep(3)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(3)
        lcd.clear()
        lcd.message(temp_var3)#displays temp_var3 on top row then scrolls left
        sleep(3)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(3)
        lcd.clear()
        lcd.message(temp_var4)#displays temp_var4 on top row then scrolls left
        sleep(3)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(3)
        lcd.clear()
    #if input is less than 16 characters it is displayed but does not scroll
    elif(len(input) <= 16):
        lcd.message(input)
        sleep(3)
    sleep(3)
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
lcd.message("Input Options      Input Options\nConfig 1 Text 2 Repeat 3 Voice 4")
sleep(2)
for x in range(0, 16):
    lcd.move_left()
    sleep(.5)
sleep(3)
for x in range(0, 16):
    lcd.move_right()
    sleep(.5)
while True:
    if button_2.is_pressed: #Text Input function 
        print("input text")
        lcd.clear()
        lcd.message("  Input Text")
        text_input()
        lcd.clear()
        lcd.message("Input Options      Input Options\nConfig 1 Text 2 Repeat 3 Voice 4")
        sleep(.5)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(1)
        for x in range(0, 16):
            lcd.move_right()
            sleep(.5)
        continue
    if button_4.is_pressed: #Voice Input function
        print("input voice")
        lcd.clear()
        lcd.message("  Input Voice")
        sleep(1)
        voice_input()
        lcd.clear()
        lcd.message("Input Options      Input Options\nConfig 1 Text 2 Repeat 3 Voice 4")
        sleep(.5)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(1)
        for x in range(0, 16):
            lcd.move_right()
            sleep(.5)
        continue
    if button_locator.is_pressed: #Locator not finished
        print("Locator")
        lcd.clear()
        lcd.message("locator enabled")
        locator_func()
        lcd.clear()
        lcd.message("Input Options      Input Options\nConfig 1 Text 2 Repeat 3 Voice 4")
        sleep(.5)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(1)
        for x in range(0, 16):
            lcd.move_right()
            sleep(.5)       
        continue
    if button_3.is_pressed: #repeat function #changed number from 3 to 4
        print("repeat")
        lcd.clear()
        lcd.message("repeating message")
        sleep(3)
        if (input_from_user != "No Previouse Message"):
            lcd.message(input_from_user)
            sleep(3)
            repeat_func()
            continue
        else:
            lcd.message(input_from_user)
            sleep(3)
        lcd.clear()
        lcd.message("Input Options      Input Options\nConfig 1 Text 2 Repeat 3 Voice 4")
        sleep(.5)
        for x in range(0, 16):
            lcd.move_left()
            sleep(.5)
        sleep(1)
        for x in range(0, 16):
            lcd.move_right()
            sleep(.5)        
        continue
    if button_1.is_pressed:
        print("Configerations")
        lcd.clear()
        lcd.message(" Configerations")
        sleep(1)
        lcd.clear()
        lcd.message("Braille Speed(2)\nHaptics(3)   <--")
        config()
        continue
                
#main