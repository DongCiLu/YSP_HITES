import android 
import time 
d = android.Android()
d.startSensingTimed(1,000)
b = 0
for I in range(40):
	a = d.sensorsReadAccelerometer()
	a = a.result[0]
	if (a is None):
		continue	
	if a - b > 3 or a - b < -3: 
		d.vibrate(200)
	b = a  	
	time.sleep(1)
d.stopSensing
d.makeToast("finished!")
