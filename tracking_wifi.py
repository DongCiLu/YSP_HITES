# The second program for HITES: Wifi localization and Geocoding

import android
import time
d = android.Android()
source = open('polyline.temp', 'r')
lines = list(source)
source.close()

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
    if not coordinates:
        return
    lines.insert(20, '\tnew google.maps.LatLng({0},{1}),\n'.format(coordinates[0], coordinates[1]))
    out = open('./trackingMap.html', 'w+')
    for l in lines:
        out.write(l)
    out.flush()
    out.close()

##### Don't change anything above this line #####
z = 0
coordinates = getLocation('network')
x = coordinates[0]
y = coordinates[1]
while z < 120:
    coordinates = getLocation('network')
    if abs(coordinates[0]-x)>0.001:
        time.sleep(1)
        continue
    print coordinates
    writeToFile(coordinates)
    time.sleep(1)
    x = coordinates[0]
    y = coordinates[1]
    z += 1