# The second program for HITES: Wifi localization and Geocoding

import android
import time
d = android.Android()

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

def getStreetname(coordinates):
    r = []
    if coordinates:
        r = d.geocode(coordinates[0], coordinates[1]).result[0]['thoroughfare']
    return r

##### Don't change anything above this line #####

#location = getLocation('network')
#print location
#information = getStreetname(location)
#print information

x = 0
old_location = 'somewhere'
while x < 30:
    time.sleep(1)
    coord = getLocation('network')
    location = getStreetname(coord)
    if not location:
        continue
    if location != old_location:
        print location
        old_location = location
    x += 1