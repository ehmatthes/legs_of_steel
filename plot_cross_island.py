# Grab cross-island trackpoint data.
#  A trackpoint is a point on the track only, not a waypoint?

import xml.etree.ElementTree as ET
import sys
from datetime import datetime

tree = ET.parse('tracks.gpx')
root = tree.getroot()

lats, lons, timestamps, elevations = [], [], [], []

# Loop through all descendent elements in root tree.
# Only store lat, lon for certain dates.
for desc in list(root.iter()):
    # Focus on trackpoints.
    if 'trkpt' in desc.tag:
        # Store lat and lon of each trackpoint.
        lat = float(desc.attrib['lat'])
        lon = float(desc.attrib['lon'])
        #lats.append(lat)
        #lons.append(lon)
        # Loop through all descendents of each trackpoint.
        for desc_2 in list(desc.iter()):
            # Store timestamp and elevation of each trackpoint.
            if 'time' in desc_2.tag:
                timestamp = datetime.strptime(desc_2.text, '%Y-%m-%dT%H:%M:%SZ')
            if 'ele' in desc_2.tag:
                elevation = float(desc_2.text)
        # Have all data, store some of it.
        if timestamp.year == 2011 and timestamp.month == 7 and (timestamp.day == 9 or timestamp.day == 10):
            lats.append(lat)
            lons.append(lon)
            timestamps.append(timestamp)
            elevations.append(elevation)

# Assert all lists same length.
assert len(lats) == len(lons) == len(timestamps) == len(elevations)
print("Number of trackpoints: %d" % len(lats))

def get_mdy(ts):
    month = datetime.strftime(ts, '%B')
    day = datetime.strftime(ts, '%d')
    year = datetime.strftime(ts, '%Y')
    return (month, day, year)


# Find unique days that have tracks.
mdy_prev = (0,0,0)
for ts in timestamps:
    mdy = get_mdy(ts)
    if mdy != mdy_prev:
        print mdy[0], mdy[1], mdy[2]
    mdy_prev = mdy




#sys.exit()




from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
map = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-136.25, llcrnrlat=56.0,
    urcrnrlon=-134.25, urcrnrlat=57.75)
    #llcrnrlon=-136.0, llcrnrlat=56.75,
    #urcrnrlon=-134.5, urcrnrlat=57.5)
 
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'coral')
map.drawmapboundary()
 


x,y = map(lons, lats)
map.plot(x, y, 'bo', markersize=10)
 
plt.show()
