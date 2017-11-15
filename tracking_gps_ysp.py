import android
import time 
f = open("polyline.temp","r")
l = list(f)
f.close()
f = open("world's fair2.html", "w+")
d = android.Android()
d.startLocating(100,0.1)
for I in range(50):
	time.sleep(2)
	a = d.readLocation()
	print a
	if not a.result:
		continue
	if "gps" in a.result:
		x = a.result['gps']['latitude']
		y = a.result['gps']['longitude']
		l.insert(20, '\tnew google.maps.LatLng({0}, {1}),\n'.format(x,y))
	print "-------------------------------"
d.stopLocating()
for items in l:
	f.write(items)
f.close()
