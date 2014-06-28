# Grab cross-island trackpoint data.
#  A trackpoint is a point on the track only, not a waypoint?
# Make elevation profile of cross-island hike.


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
                # Convert meters to feet.
                elevation = 3.28084 * float(desc_2.text)
        # Have all data, store some of it.
        if timestamp.year == 2011 and timestamp.month == 7 and (timestamp.day == 9 or timestamp.day == 10):
            lats.append(lat)
            lons.append(lon)
            timestamps.append(timestamp)
            elevations.append(elevation)

# Assert all lists same length.
assert len(lats) == len(lons) == len(timestamps) == len(elevations)
print("Number of trackpoints: %d" % len(lats))


# Calculate distances between successive points.
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    # 6367 km is the radius of the Earth
    km = 6367 * c
    miles = km * 0.621371
    return miles

distances = []
cum_distances = []
for index, lat in enumerate(lats):
    if index == 0:
        distances.append(0)
        cum_distances.append(0)
        continue
    dist = haversine(lons[index], lats[index], lons[index-1], lats[index-1])
    distances.append(dist)
    cum_distance = sum(distances)
    cum_distances.append(cum_distance)

assert len(distances) == len(cum_distances) == len(lats)


import matplotlib.pyplot as plt
import numpy as np

plt.scatter(cum_distances, elevations, s=2, lw=0)
 
plt.show()
