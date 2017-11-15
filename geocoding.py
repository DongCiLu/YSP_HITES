import android
import time 
d = android.Android()
d.startLocating()
for I in range(10):
	time.sleep(2)
	a = d.readLocation()
	print a
	if not a.result:
		continue
	x = a.result['network']['latitude']
	y = a.result['network']['longitude']
	print d.geocode(x,y)
	print "-------------------------------"
d.stopLocating()