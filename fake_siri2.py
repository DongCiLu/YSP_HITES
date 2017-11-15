 # The first program for HITES: Hello Android

import android
import time
d = android.Android()

##### Don't change anything above this line #####
x=0

while (x<5):
    d.ttsSpeak('Hello')
    s = d.recognizeSpeech().result
    print s
    if 'name' in s:
        d.ttsSpeak('Hi I am fake siri nice to meet you')
    elif 'weather' in s:
        d.ttsSpeak('Go Outside and figure it out yourself')
    elif 'time' in s:
        z = time.strftime('%H:%M:%S')
        d.ttsSpeak('You think i am a watch, i am an extremely high tech device made strictly for communication but ok ')
        d.ttsSpeak('it is' + z)
        print z
    elif 'shut up' in s:
        d.ttsSpeak('Okay i will')
    break
    else:
        d.ttsSpeak('please shut up i am better')

       # d.mediaPlay('/sdcard/a.mp3')
       # d.mediaPlayStart()
    time.sleep(9)
    x+=1
 d.ttsSpeak('What is your favorite T V show')
    elif 'Doctor Who' in s:
        d.ttsSpeak('I love Doctor who to')
        d.ttsSpeak('Do you want to hear the theme song'
    elif 'Yes' in s:    
        d.mediaPlay('/sdcard/DW.mp3')
        d.mediaPlayStart()
        time.sleep(10)
        d.mediaPlayStop()




























 
        