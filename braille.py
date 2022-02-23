from gpiozero import LED
from time import sleep
from google.cloud import speech

import os
import io
import sys


#left column
led_1 = LED(17)
led_3 = LED(27)
led_5 = LED(22)
#right column
led_2 = LED(23)
led_4 = LED(24)
led_6 = LED(25)


def Braille_Letter_A():
    led_1.on()
    sleep(2)
    led_1.off()
     
def Braille_Letter_B():
    led_1.on()
    led_3.on() 
    sleep(2)
    led_1.off()
    led_3.off()
    
def Braille_Letter_C(): 
    led_1.on()
    led_2.on() 
    sleep(2)
    led_1.off()
    led_2.off()
    
def Braille_Letter_D():  
    led_1.on()
    led_2.on() 
    led_4.on()
    sleep(2)
    led_1.off()
    led_2.off()
    led_4.off()
 
def Braille_Letter_E():
    led_1.on()
    led_4.on()
    sleep(2)
    led_1.off()
    led_4.off()
    
def Braille_Letter_F():
    led_1.on()
    led_2.on() 
    led_3.on()
    sleep(2)
    led_1.off()
    led_2.off()
    led_3.off()
    
def Braille_Letter_G():
    led_1.on()
    led_2.on()
    led_3.on()
    led_4.on()
    sleep(2)
    led_1.off()
    led_2.off()
    led_3.off()
    led_4.off()

def Braille_Letter_H():
    led_1.on()
    led_4.on() 
    led_3.on()
    sleep(2)
    led_1.off()
    led_4.off()
    led_3.off()
    
def Braille_Letter_I():
    led_2.on() 
    led_3.on()
    sleep(2)
    led_2.off()
    led_3.off()
    
def Braille_Letter_J():
    led_2.on() 
    led_3.on()
    led_4.on()
    sleep(2)
    led_4.off()
    led_2.off()
    led_3.off()
    
def Braille_Letter_K():
    led_1.on() 
    led_5.on()
    sleep(2)
    led_1.off()
    led_5.off()
    
def Braille_Letter_L():
    led_1.on() 
    led_3.on()
    led_5.on()
    sleep(2)
    led_1.off()
    led_3.off()
    led_5.off()
    
def Braille_Letter_M():
    led_2.on() 
    led_1.on()
    led_5.on()
    sleep(2)
    led_1.off()
    led_2.off()
    led_5.off()
    
def Braille_Letter_N():
    led_1.on()
    led_2.on() 
    led_4.on()
    led_5.on()
    sleep(2)
    led_1.off()
    led_2.off()
    led_4.off()
    led_5.off()
    
def Braille_Letter_O():
    led_1.on()
    led_4.on()
    led_5.on()
    sleep(2)
    led_1.off()
    led_4.off()
    led_5.off()
    
def Braille_Letter_P():
    led_1.on()
    led_2.on() 
    led_3.on()
    led_5.on()
    sleep(2)
    led_1.off()
    led_2.off()
    led_3.off()
    led_5.off()
    
def Braille_Letter_Q():
    led_1.on()
    led_2.on() 
    led_3.on()
    led_4.on()
    led_5.on()
    sleep(2)
    led_1.off()
    led_2.off()
    led_3.off()
    led_4.off()
    led_5.off()
    
def Braille_Letter_R():
    led_1.on()
    led_3.on()
    led_4.on()
    led_5.on()
    sleep(2)
    led_1.off()
    led_3.off()
    led_4.off()
    led_5.off()
    
def Braille_Letter_S():
    led_2.on() 
    led_3.on()
    led_5.on()
    sleep(2)
    led_2.off()
    led_3.off()
    led_5.off()
    
def Braille_Letter_T():
    led_2.on() 
    led_3.on()
    led_4.on()
    led_5.on()
    sleep(2)
    led_2.off()
    led_3.off()
    led_4.off()
    led_5.off()
    
def Braille_Letter_U():
    led_1.on()
    led_5.on()
    led_6.on()
    sleep(2)
    led_1.off()
    led_5.off()
    led_6.off()
    
def Braille_Letter_V():
    led_1.on()
    led_3.on()
    led_5.on()
    led_6.on()
    sleep(2)
    led_1.off()
    led_3.off()
    led_5.off()
    led_6.off()
    
def Braille_Letter_W():
    led_2.on()
    led_3.on()
    led_4.on()
    led_6.on()
    sleep(2)
    led_2.off()
    led_3.off()
    led_4.off()
    led_6.off()
    
def Braille_Letter_X():
    led_1.on()
    led_2.on()
    led_5.on()
    led_6.on()
    sleep(2)
    led_1.off()
    led_2.off()
    led_5.off()
    led_6.off()
    
def Braille_Letter_Y():
    led_1.on()
    led_2.on()
    led_4.on()
    led_5.on()
    led_6.on()
    sleep(2)
    led_1.off()
    led_2.off()
    led_4.off()
    led_5.off()
    led_6.off()
    
def Braille_Letter_Z():
    led_1.on()
    led_4.on()
    led_5.on()
    led_6.on()
    sleep(2)
    led_1.off()
    led_4.off()
    led_5.off()
    led_6.off()
 
def Braille_Letter_space():
    sleep(2)

def function_name(string_translate):
    for i in string_translate:
        #letters
        if i == 'a' or i == 'A':
            Braille_Letter_A()
        elif i == 'b' or i == 'B':
            Braille_Letter_B()
        elif i == 'c' or i == 'C':
            Braille_Letter_C()
        elif i == 'd' or i == 'D':
            Braille_Letter_D()
        elif i == 'e' or i == 'E':
            Braille_Letter_E()
        elif i == 'f' or i == 'F':
            Braille_Letter_F()
        elif i == 'g' or i == 'G':
            Braille_Letter_G()
        elif i == 'h' or i == 'H':
            Braille_Letter_H()
        elif i == 'i' or i == 'I':
            Braille_Letter_I()
        elif i == 'j' or i == 'J':
            Braille_Letter_J()
        elif i == 'k' or i == 'K':
            Braille_Letter_K()
        elif i == 'l' or i == 'L':
            Braille_Letter_L()
        elif i == 'm' or i == 'M':
            Braille_Letter_M()
        elif i == 'n' or i == 'N':
            Braille_Letter_N()
        elif i == 'o' or i == 'O':
            Braille_Letter_O()
        elif i == 'p' or i == 'P':
            Braille_Letter_P()
        elif i == 'q' or i == 'Q':
            Braille_Letter_Q()
        elif i == 'r' or i == 'R':
            Braille_Letter_R()
        elif i == 's' or i == 'S':
            Braille_Letter_S()
        elif i == 't' or i == 'T':
            Braille_Letter_T()
        elif i == 'u' or i == 'U':
            Braille_Letter_U()
        elif i == 'v' or i == 'V':
            Braille_Letter_V()
        elif i == 'w' or i == 'W':
            Braille_Letter_W()
        elif i == 'x' or i == 'X':
            Braille_Letter_X()
        elif i == 'y' or i == 'Y':
            Braille_Letter_Y()
        elif i == 'z' or i == 'Z':
            Braille_Letter_Z()
        elif i == ' ':
            Braille_Letter_space()
        #numbers
        else:
            Braille_Letter_space()
        #needs else for if not letter or symbol

#-----------------------functions^------------------------------------


#input_from_user = input("enter a word to translate: ")
#print ("word to translate: " + input_from_user)

#print(input_from_user[3])

#function_name(input_from_user)

#------------------------speech v--------------------------------------
# Creates google client
client = speech.SpeechClient()

# Full path of the audio file, Replace with your file name
file_name = os.path.join(os.path.dirname(__file__),"test_3.wav")

#Loads the audio file into memory
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    audio_channel_count=2,
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
print(output)

#outputs to braille led
function_name(output)