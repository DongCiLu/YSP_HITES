import android
import time 
d = android.Android()
d.makeToast("start!")
d.startSensingTimed(1,100)
for I in range(40):
	a = d.sensorsReadMagnetometer()
	mag = a.result[2]
	if not mag:
		continue
	print mag
	if (int(mag) < -30):
		d.ttsSpeak("Doctor Chen we found metal")
		time.sleep(5)	
	time.sleep(1)
d.stopSensing()
d.makeToast("finished!")