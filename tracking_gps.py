# The second program for HITES: Wifi localization and Geocoding

import android
import time
d = android.Android()
source = open('polyline.temp', 'r')
lines = list(source)
source.close()

def gpsReady():
    d.startLocating(1000,1)
    while 1:
        time.sleep(0.1)
        print 'gps not ready'
        if 'gps' in d.readLocation().result:
            print 'gps ready!'
            d.makeToast('gps ready!')
            d.vibrate(7000)
            return

def getLocation(method):
    coordinates = []
    d.startLocating(1000, 1)
    tried = 0
    while tried < 20:
        time.sleep(0.1)
        locatingReadings = d.readLocation().result
        if method in locatingReadings:
            coordinates = [float(locatingReadings[method]['latitude']), float(locatingReadings[method]['longitude'])]
            break
        tried += 1
    d.stopLocating()
    return coordinates

def writeToFile(coordinates):
    lines.insert(20, '\tnew google.maps.LatLng({0},{1}),\n'.format(coordinates[0], coordinates[1]))
    out = open('trackingMap.html', 'w')
    for l in lines:
        out.write(l)
    out.close()

##### Don't change anything above this line #####
gpsReady()
coordinates = getLocation('gps')
writeToFile(coordinates)
