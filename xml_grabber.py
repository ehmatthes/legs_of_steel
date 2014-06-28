# Grab all the trackpoint data.
#  A trackpoint is a point on the track, not a waypoint?

import xml.etree.ElementTree as ET
import sys
from datetime import datetime

tree = ET.parse('tracks.gpx')
root = tree.getroot()

"""
print(root.tag)
print(root.attrib)
for child in root:
    pass#print(child)

print("---")
print(root[2])
for child in root[2]:
    pass#print(child)

for trkpt in root.findall('trkpt'):
    print trkpt.attrib
"""


lats, lons, timestamps, elevations = [], [], [], []


for desc in list(root.iter()):
    if 'trkpt' in desc.tag:
        #print('\n---')
        #print(desc.attrib)
        lat = float(desc.attrib['lat'])
        lon = float(desc.attrib['lon'])
        lats.append(lat)
        lons.append(lon)
        for desc_2 in list(desc.iter()):
            #print(desc_2)
            if 'time' in desc_2.tag:
                #print(desc_2.text)
                timestamp = desc_2.text
                timestamp = datetime.strptime(desc_2.text, '%Y-%m-%dT%H:%M:%SZ')
                timestamps.append(timestamp)
            if 'ele' in desc_2.tag:
                elevation = float(desc_2.text)
                elevations.append(elevation)

print(len(lats), len(lons), len(timestamps), len(elevations))



mdy_prev = (0,0,0)
for ts in timestamps:
    ts_prev = ts
    #print(ts.month)
    month = datetime.strftime(ts, '%B')
    day = datetime.strftime(ts, '%d')
    year = datetime.strftime(ts, '%Y')
    if (month, day, year) != mdy_prev:
        print month, day, year
    #print month, day, year
    mdy_prev = (month, day, year)
