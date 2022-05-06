from gpiozero import LED
from gpiozero import Button
from time import sleep
from google.cloud import speech
from Adafruit_CharLCD import Adafruit_CharLCD
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO

import os
import io
import sys
import subprocess
import signal
import time

lcd = Adafruit_CharLCD(rs=7, en=8, d4=25, d5=24, d6=23, d7=18, cols=16, lines=2)
#braille_letters.py

#pi zero ip for LEDs
#Ledlight = PiGPIOFactory(host='192.168.0.241') #home wifi ip
Ledlight = PiGPIOFactory(host='192.168.149.233') #hotspot ip
#pi zero ip for rumble motor
#motor = PiGPIOFactory(host='192.168.0.241')

#global variables
braille_speed_config = 2

#leds
#left column
led_1 = LED(25,pin_factory=Ledlight)
led_3 = LED(24,pin_factory=Ledlight)
led_5 = LED(23,pin_factory=Ledlight)
#right column
led_2 = LED(22,pin_factory=Ledlight)
led_4 = LED(27,pin_factory=Ledlight)
led_6 = LED(4,pin_factory=Ledlight)
def SpeedBrailleUp():
    global braille_speed_config 
    braille_speed_config += 1
    lcd.clear()
    lcd.message("Speed: " + braille_speed_config)
    sleep(1)

def SpeedBrailleDown():
    global braille_speed_config
    if (braille_speed_config == 1):
        lcd.clear()
        lcd.message("Speed: " + braille_speed_config)
        sleep(1)
        return
    else:
        braille_speed_config -= 1
        lcd.clear()
        lcd.message("Speed: " + braille_speed_config)
        sleep(1)

def Braille_Letter_A():
    led_1.on()
    sleep(braille_speed_config)
    led_1.off()
     
def Braille_Letter_B():
    led_1.on()
    led_3.on() 
    #lcd.clear()
    #lcd.message("     B    ")
    sleep(braille_speed_config)
    led_1.off()
    led_3.off()
    
def Braille_Letter_C(): 
    led_1.on()
    led_2.on() 
    #lcd.clear()
    #lcd.message("     C     ")
    sleep(braille_speed_config)
    led_1.off()
    led_2.off()
    
def Braille_Letter_D():  
    led_1.on()
    led_2.on() 
    led_4.on()
    sleep(braille_speed_config)
    led_1.off()
    led_2.off()
    led_4.off()
 
def Braille_Letter_E():
    led_1.on()
    led_4.on()
    sleep(braille_speed_config)
    led_1.off()
    led_4.off()
    
def Braille_Letter_F():
    led_1.on()
    led_2.on() 
    led_3.on()
    sleep(braille_speed_config)
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
 
def Braille_Letter_comma():
    led_3.on()
    sleep(2)
    led_3.off()

def Braille_Letter_period():
    led_3.on()
    led_4.on()
    led_6.on()
    sleep(2)
    led_3.off()
    led_4.off()
    led_6.off()

def Braille_Letter_colon():
    led_3.on()
    led_4.on()
    sleep(2)
    led_3.off()
    led_4.off()

def Braille_Letter_exclamation_mark():
    led_3.on()
    led_4.on()
    led_5.on()
    sleep(2)
    led_3.off()
    led_4.off()
    led_5.off()

def Braille_Letter_hyphen():
    led_5.on()
    led_6.on()
    sleep(2)
    led_5.off()
    led_6.off()

def Braille_Letter_question():
    led_3.on()
    led_5.on()
    led_6.on()
    sleep(2)
    led_3.off()
    led_5.off()
    led_6.off()

def Braille_Letter_semicolon():
    led_3.on()
    led_5.on()
    sleep(2)
    led_3.off()
    led_5.off()

def Braille_Letter_apostrophe():
    led_5.on()
    sleep(2)
    led_5.off()
    
def Braille_Letter_hash():
    led_2.on()
    led_4.on()
    led_6.on()
    led_5.on()
    sleep(2)
    led_2.off()
    led_4.off()
    led_5.off()
    led_6.off()

def word_interation(string_translate):
    print("outputting braille")
    for i in range (0, len(string_translate)):
        #letters
        if string_translate[i] == 'a' or string_translate[i] == 'A':
            Braille_Letter_A()
        elif string_translate[i] == 'b' or string_translate[i] == 'B':
            Braille_Letter_B()
        elif string_translate[i] == 'c' or string_translate[i] == 'C':
            Braille_Letter_C()
        elif string_translate[i] == 'd' or string_translate[i] == 'D':
            Braille_Letter_D()
        elif string_translate[i] == 'e' or string_translate[i] == 'E':
            Braille_Letter_E()
        elif string_translate[i] == 'f' or string_translate[i] == 'F':
            Braille_Letter_F()
        elif string_translate[i] == 'g' or string_translate[i] == 'G':
            Braille_Letter_G()
        elif string_translate[i] == 'h' or string_translate[i] == 'H':
            Braille_Letter_H()
        elif string_translate[i] == 'i' or string_translate[i] == 'I':
            Braille_Letter_I()
        elif string_translate[i] == 'j' or string_translate[i] == 'J':
            Braille_Letter_J()
        elif string_translate[i] == 'k' or string_translate[i] == 'K':
            Braille_Letter_K()
        elif string_translate[i] == 'l' or string_translate[i] == 'L':
            Braille_Letter_L()
        elif string_translate[i] == 'm' or string_translate[i] =='M':
            Braille_Letter_M()
        elif string_translate[i] == 'n' or string_translate[i] =='N':
            Braille_Letter_N()
        elif string_translate[i] == 'o' or string_translate[i] =='O':
            Braille_Letter_O()
        elif string_translate[i] == 'p' or string_translate[i] =='P':
            Braille_Letter_P()
        elif string_translate[i] == 'q' or string_translate[i] =='Q':
            Braille_Letter_Q()
        elif string_translate[i] == 'r' or string_translate[i] =='R':
            Braille_Letter_R()
        elif string_translate[i] == 's' or string_translate[i] =='S':
            Braille_Letter_S()
        elif string_translate[i] == 't' or string_translate[i] =='T':
            Braille_Letter_T()
        elif string_translate[i] == 'u' or string_translate[i] =='U':
            Braille_Letter_U()
        elif string_translate[i] == 'v' or string_translate[i] =='V':
            Braille_Letter_V()
        elif string_translate[i] == 'w' or string_translate[i] =='W':
            Braille_Letter_W()
        elif string_translate[i] == 'x' or string_translate[i] =='X':
            Braille_Letter_X()
        elif string_translate[i] == 'y' or string_translate[i] =='Y':
            Braille_Letter_Y()
        elif string_translate[i] == 'z' or string_translate[i] =='Z':
            Braille_Letter_Z()
        #symbols
        elif string_translate[i] == ' ':
            Braille_Letter_space()
        elif string_translate[i] == ',':
            Braille_Letter_comma()
        elif string_translate[i] == '.':
            Braille_Letter_period()
        elif string_translate[i] == ':':
            Braille_Letter_colon()
        elif string_translate[i] == '!':
            Braille_Letter_exclamation_mark()
        elif string_translate[i] == '-':
            Braille_Letter_hyphen()
        elif string_translate[i] == '?':
            Braille_Letter_question()
        elif string_translate[i] == ';':
            Braille_Letter_semicolon()
        elif string_translate[i] == "'":
            Braille_Letter_apostrophe()
        #numbers
        elif string_translate[i] == '1':
            tempnum = string_translate[i-1]
            #if index before i is a number and not first index of string
            if tempnum.isnumeric() == True and (i != 0):
                Braille_Letter_A()
            else:
                Braille_Letter_hash()
                Braille_Letter_A()
        elif string_translate[i] == '2':
            tempnum = string_translate[i-1]
            if tempnum.isnumeric() == True and i != 0:
                Braille_Letter_B()
            else:
                Braille_Letter_hash()
                Braille_Letter_B()
        elif string_translate[i] == '3':
            tempnum = string_translate[i-1]
            if tempnum.isnumeric() == True and i != 0:
                Braille_Letter_C()
            else:
                Braille_Letter_hash()
                Braille_Letter_C()
        elif string_translate[i] == '4':
            tempnum = string_translate[i-1]
            if tempnum.isnumeric() == True and i != 0:
                Braille_Letter_D()
            else:
                Braille_Letter_hash()
                Braille_Letter_D()
        elif string_translate[i] == '5':
            tempnum = string_translate[i-1]
            if tempnum.isnumeric() == True and i != 0:
                Braille_Letter_E()
            else:
                Braille_Letter_hash()
                Braille_Letter_E()
        elif string_translate[i] == '6':
            tempnum = string_translate[i-1]
            if tempnum.isnumeric() == True and i != 0:
                Braille_Letter_F()
            else:
                Braille_Letter_hash()
                Braille_Letter_F()
        elif string_translate[i] == '7':
            tempnum = string_translate[i-1]
            if tempnum.isnumeric() == True and i != 0:
                Braille_Letter_G()
            else:
                Braille_Letter_hash()
                Braille_Letter_G()
        elif string_translate[i] == '8':
            tempnum = string_translate[i-1]
            if tempnum.isnumeric() == True and i != 0:
                Braille_Letter_H()
            else:
                Braille_Letter_hash()
                Braille_Letter_H()
        elif string_translate[i] == '9':
            tempnum = string_translate[i-1]
            if tempnum.isnumeric() == True and i != 0:
                Braille_Letter_I()
            else:
                Braille_Letter_hash()
                Braille_Letter_I()
        elif string_translate[i] == '0':
            tempnum = string_translate[i-1]
            if tempnum.isnumeric() == True and i != 0:
                Braille_Letter_J()
            else:
                Braille_Letter_hash()
                Braille_Letter_J()

        else:
            Braille_Letter_space()
        #needs else for if not letter or symbol
    #lcd.clear()
    #lcd.message(" Input Options\nText Repeat Voice")

