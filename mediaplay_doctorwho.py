 # The first program for HITES: Hello Android

import android
d = android.Android()

##### Don't change anything above this line #####

d.ttsSpeak('I love Doctor who')
d.ttsSpeak('Do you want to hear the theme song')
s = d.recognizeSpeech()
if 'Yes' in s:    
    d.mediaPlay('/sdcard/DW.mp3')
    d.mediaPlayStart()
    time.sleep(10)
    d.mediaPlayStop()
