# Grab all the trackpoint data.
#  A trackpoint is a point on the track, not a waypoint?

import xml.etree.ElementTree as ET
import sys
from datetime import datetime

tree = ET.parse('tracks.gpx')
root = tree.getroot()

lats, lons, timestamps, elevations = [], [], [], []

# Loop through all descendent elements in root tree.
for desc in list(root.iter()):
    # Focus on trackpoints.
    if 'trkpt' in desc.tag:
        # Store lat and lon of each trackpoint.
        lat = float(desc.attrib['lat'])
        lon = float(desc.attrib['lon'])
        lats.append(lat)
        lons.append(lon)
        # Loop through all descendents of each trackpoint.
        for desc_2 in list(desc.iter()):
            # Store timestamp and elevation of each trackpoint.
            if 'time' in desc_2.tag:
                timestamp = datetime.strptime(desc_2.text, '%Y-%m-%dT%H:%M:%SZ')
                timestamps.append(timestamp)
            if 'ele' in desc_2.tag:
                elevation = float(desc_2.text)
                elevations.append(elevation)

# Assert all lists same length.
print(len(lats), len(lons), len(timestamps), len(elevations))

# Find unique days that have tracks.
mdy_prev = (0,0,0)
for ts in timestamps:
    month = datetime.strftime(ts, '%B')
    day = datetime.strftime(ts, '%d')
    year = datetime.strftime(ts, '%Y')
    if (month, day, year) != mdy_prev:
        print month, day, year
    mdy_prev = (month, day, year)
