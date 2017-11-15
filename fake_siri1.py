# The first program for HITES: Hello Android

import time
import android
d = android.Android()

##### Don't change anything above this line #####
y = 0
#d.mediaPlay("/sdcard/open.mp3")
#d.mediaPlayStart()
#time.sleep(6)
d.ttsSpeak("hello strangest stranger")
while y < 50:
    time.sleep(3)
    x = d.recognizeSpeech().result
    if "how are you" in x:
        d.ttsSpeak('Do not sass me but you better tell me how you are')
    elif "your name" in x:
        d.ttsSpeak("why would you ask that to me but whats your name")
    elif "mood" in x:
        d.ttsSpeak("im thinking about ponies and unicorns what is your mood")
    elif "good" in x:
        d.ttsSpeak("well thats too bad because im feeling fabulous")
    elif "mean" in x:
        d.ttsSpeak("dont worry about it")
    elif "crazy" in x:
        d.ttsSpeak("i would fight you but i have no hands")
    elif "the weather" in x:
        d.ttsSpeak("go outside and find out yourself")
    elif "bye bye" in x:
        d.ttsSpeak("bye bye")
        break
    else:
        d.ttsSpeak('keep asking me questions')
    y = y+1

